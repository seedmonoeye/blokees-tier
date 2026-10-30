const express = require('express');
const Database = require('better-sqlite3');
const path = require('path');
const crypto = require('crypto');

const PORT = process.env.PORT || 3000;
const ADMIN_KEY = process.env.ADMIN_KEY || 'change-this-admin-key';
const DB_FILE = process.env.DB_FILE || path.join(__dirname, 'votes.db');
const TIERS = ['S', 'A', 'B', 'C', 'D'];

const DEFAULT_ITEMS = [
  { id:'spiderman', name:'Spider-Man',            no:'06', img:'https://m.media-amazon.com/images/I/81BlopGI1dL._AC_UF1000,1000_QL80_.jpg' },
  { id:'venom',     name:'Venom',                 no:'07', img:'https://m.media-amazon.com/images/I/81vl+wZxWJL._AC_UF350,350_QL80_.jpg' },
  { id:'peni',      name:'Peni Parker & SP//DR',  no:'08', img:'https://m.media-amazon.com/images/I/81Wi4XUmc-L._AC_UF894,1000_QL80_.jpg' },
  { id:'rocket',    name:'Rocket Raccoon',        no:'09', img:'https://m.media-amazon.com/images/I/81T7BBwkISL._AC_UF894,1000_QL80_.jpg' },
  { id:'moonknight',name:'Moon Knight',           no:'10', img:'https://m.media-amazon.com/images/I/81OVKzlNKJL._AC_UF1000,1000_QL80_.jpg' },
  { id:'invisible', name:'Invisible Woman',       no:'11', img:'https://m.media-amazon.com/images/I/81v7Ub892lL._AC_UF1000,1000_QL80_.jpg' },
  { id:'jeff',      name:'Jeff the Land Shark',   no:'12', img:'https://m.media-amazon.com/images/I/81xkWJV8cKL._AC_UF894,1000_QL80_.jpg' },
];

/* ===================== DATABASE ===================== */
const db = new Database(DB_FILE);
db.pragma('journal_mode = WAL');
db.pragma('foreign_keys = ON');

db.exec(`
  CREATE TABLE IF NOT EXISTS items (
    id   TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    no   TEXT,
    img  TEXT,
    sort INTEGER DEFAULT 0
  );
  CREATE TABLE IF NOT EXISTS votes (
    voter_id   TEXT NOT NULL,
    item_id    TEXT NOT NULL REFERENCES items(id) ON DELETE CASCADE,
    tier       TEXT NOT NULL CHECK (tier IN ('S','A','B','C','D')),
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (voter_id, item_id)
  );
  CREATE INDEX IF NOT EXISTS idx_votes_item ON votes(item_id);
`);

// Seed default models on first run
if (db.prepare('SELECT COUNT(*) AS c FROM items').get().c === 0) {
  const ins = db.prepare('INSERT INTO items (id, name, no, img, sort) VALUES (?, ?, ?, ?, ?)');
  db.transaction(() => DEFAULT_ITEMS.forEach((it, i) => ins.run(it.id, it.name, it.no, it.img, i)))();
  console.log('Seeded default items.');
}

const toTier = a => a >= 4.5 ? 'S' : a >= 3.5 ? 'A' : a >= 2.5 ? 'B' : a >= 1.5 ? 'C' : 'D';

/* ===================== APP ===================== */
const app = express();
app.use(express.json({ limit: '50kb' }));
app.use(express.static(path.join(__dirname, 'public')));

const requireAdmin = (req, res, next) =>
  req.get('x-admin-key') === ADMIN_KEY ? next() : res.status(401).json({ error: 'Invalid admin key' });

// List models
app.get('/api/items', (req, res) => {
  res.json(db.prepare('SELECT id, name, no, img FROM items ORDER BY sort, no').all());
});

// Get one voter's current vote
app.get('/api/votes/:voterId', (req, res) => {
  const rows = db.prepare('SELECT item_id, tier FROM votes WHERE voter_id = ?').all(req.params.voterId);
  res.json(Object.fromEntries(rows.map(r => [r.item_id, r.tier])));
});

// Submit / update a vote  { voterId, votes: { itemId: 'S' | 'A' | ... } }
app.post('/api/vote', (req, res) => {
  const { voterId, votes } = req.body || {};
  if (typeof voterId !== 'string' || !/^[\w-]{8,64}$/.test(voterId))
    return res.status(400).json({ error: 'Invalid voter ID' });
  if (!votes || typeof votes !== 'object')
    return res.status(400).json({ error: 'Invalid votes payload' });

  const validIds = new Set(db.prepare('SELECT id FROM items').all().map(r => r.id));
  const entries = Object.entries(votes).filter(([id, t]) => validIds.has(id) && TIERS.includes(t));
  if (!entries.length) return res.status(400).json({ error: 'No valid votes' });

  const del = db.prepare('DELETE FROM votes WHERE voter_id = ?');
  const ins = db.prepare('INSERT INTO votes (voter_id, item_id, tier) VALUES (?, ?, ?)');
  db.transaction(() => {
    del.run(voterId);
    entries.forEach(([id, t]) => ins.run(voterId, id, t));
  })();

  res.json({ ok: true, count: entries.length });
});

// Aggregated community results
app.get('/api/results', (req, res) => {
  const rows = db.prepare(`
    SELECT i.id, i.name, i.no, i.img,
      COUNT(v.tier) AS total,
      SUM(v.tier = 'S') AS S, SUM(v.tier = 'A') AS A, SUM(v.tier = 'B') AS B,
      SUM(v.tier = 'C') AS C, SUM(v.tier = 'D') AS D,
      AVG(CASE v.tier WHEN 'S' THEN 5 WHEN 'A' THEN 4 WHEN 'B' THEN 3
                      WHEN 'C' THEN 2 WHEN 'D' THEN 1 END) AS avg
    FROM items i
    LEFT JOIN votes v ON v.item_id = i.id
    GROUP BY i.id
    ORDER BY avg IS NULL, avg DESC, total DESC, i.sort
  `).all();

  const items = rows.map(r => ({
    id: r.id, name: r.name, no: r.no, img: r.img,
    total: r.total,
    avg: r.avg ?? 0,
    counts: Object.fromEntries(TIERS.map(t => [t, r[t] || 0])),
    communityTier: r.total ? toTier(r.avg) : null,
  }));
  const totalVoters = db.prepare('SELECT COUNT(DISTINCT voter_id) AS c FROM votes').get().c;
  res.json({ totalVoters, items });
});

/* ===================== ADMIN ===================== */
app.get('/api/admin/check', requireAdmin, (req, res) => res.json({ ok: true }));

app.post('/api/items', requireAdmin, (req, res) => {
  const { name, no, img } = req.body || {};
  if (typeof name !== 'string' || !name.trim())
    return res.status(400).json({ error: 'Name is required' });
  if (img && !/^https?:\/\//i.test(img))
    return res.status(400).json({ error: 'Image URL must start with http:// or https://' });

  const slug = name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 30) || 'item';
  const item = {
    id: `${slug}-${crypto.randomBytes(3).toString('hex')}`,
    name: name.trim().slice(0, 60),
    no: String(no || '??').slice(0, 6),
    img: img || '',
  };
  const sort = db.prepare('SELECT COALESCE(MAX(sort), 0) + 1 AS s FROM items').get().s;
  db.prepare('INSERT INTO items (id, name, no, img, sort) VALUES (?, ?, ?, ?, ?)')
    .run(item.id, item.name, item.no, item.img, sort);
  res.status(201).json(item);
});

app.delete('/api/items/:id', requireAdmin, (req, res) => {
  const r = db.prepare('DELETE FROM items WHERE id = ?').run(req.params.id); // votes cascade
  if (!r.changes) return res.status(404).json({ error: 'Item not found' });
  res.json({ ok: true });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
  if (ADMIN_KEY === 'change-this-admin-key') console.warn('WARNING: set ADMIN_KEY env variable!');
});