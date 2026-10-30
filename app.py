import streamlit as st

st.set_page_config(page_title="Blokees Marvel Champion Class Tier List", layout="wide")

if "all_items" not in st.session_state:
    st.session_state.all_items = [
        {"name": "Iron Man Mark 85", "image": ""},
        {"name": "Spider-Man", "image": ""},
        {"name": "Captain America", "image": ""},
        {"name": "Thanos", "image": ""}
    ]

if "tier_data" not in st.session_state:
    st.session_state.tier_data = {
        "S Tier (สุดยอด / หายาก)": [],
        "A Tier (ยอดเยี่ยม)": [],
        "B Tier (มาตรฐาน)": [],
        "C Tier (ทั่วไป)": [],
        "Unassigned (ยังไม่จัดอันดับ)": [item["name"] for item in st.session_state.all_items]
    }

def get_item_image(name):
    for item in st.session_state.all_items:
        if item["name"] == name:
            return item["image"]
    return ""

def sync_tiers():
    current_assigned = []
    for t in st.session_state.tier_data:
        current_assigned.extend(st.session_state.tier_data[t])
    
    all_names = [item["name"] for item in st.session_state.all_items]
    
    for name in all_names:
        if name not in current_assigned:
            st.session_state.tier_data["Unassigned (ยังไม่จัดอันดับ)"].append(name)
            
    for t in list(st.session_state.tier_data.keys()):
        st.session_state.tier_data[t] = [name for name in st.session_state.tier_data[t] if name in all_names or t == "Unassigned (ยังไม่จัดอันดับ)"]
        
    st.session_state.tier_data["Unassigned (ยังไม่จัดอันดับ)"] = [name for name in st.session_state.tier_data["Unassigned (ยังไม่จัดอันดับ)"] if name in all_names]

sync_tiers()

tab1, tab2 = st.tabs(["🏆 หน้าจัดอันดับ Tier List", "⚙️ หน้า Admin Config"])

with tab1:
    st.title("🏆 Blokees Marvel Champion Class Tier List")
    st.markdown("จัดอันดับตัวละครโมเดล Blokees พร้อมรูปภาพขนาดใหญ่สะใจ")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### 📦 คลังตัวละคร (Unassigned)")
        unassigned = st.session_state.tier_data["Unassigned (ยังไม่จัดอันดับ)"]
        if not unassigned:
            st.info("จัดอันดับครบทุกตัวละครแล้ว!")
        for name in unassigned:
            img = get_item_image(name)
            if img:
                st.image(img, width=80)
            st.markdown(f"**- {name}**")

    with col2:
        all_flatten_names = [name for sublist in st.session_state.tier_data.values() for name in sublist]
        if all_flatten_names:
            selected_item = st.selectbox("เลือกตัวละครที่ต้องการย้าย:", all_flatten_names, key="move_selectbox")
            target_tier = st.selectbox("เลือก Tier ปลายทาง:", list(st.session_state.tier_data.keys()), key="tier_selectbox")
            
            if st.button("ย้ายตัวละครเข้า Tier", type="primary"):
                for t in st.session_state.tier_data:
                    if selected_item in st.session_state.tier_data[t]:
                        st.session_state.tier_data[t].remove(selected_item)
                st.session_state.tier_data[target_tier].append(selected_item)
                st.rerun()
        else:
            st.warning("ยังไม่มีตัวละครในระบบ กรุณาเพิ่มที่หน้า Admin Config")

    st.divider()

    st.subheader("📊 ผลลัพธ์ Tier List ปัจจุบัน")
    for tier_name, names in st.session_state.tier_data.items():
        if tier_name == "Unassigned (ยังไม่จัดอันดับ)":
            continue
        st.markdown(f"### **{tier_name}**")
        if names:
            # ปรับให้แสดงผลแถวละ 3 การ์ดขนาดใหญ่
            cols = st.columns(min(len(names), 3))
            for i, name in enumerate(names):
                with cols[i % 3]:
                    img = get_item_image(name)
                    st.markdown(f"<div style='background-color: #1e272e; color: white; padding: 15px; border-radius: 8px; text-align: center; margin-bottom: 10px; border: 2px solid #485460;'>", unsafe_allow_html=True)
                    if img:
                        st.image(img, use_container_width=True)
                    else:
                        st.markdown("<p style='color: #808e9b; font-size: 14px;'>(ไม่มีรูปภาพ)</p>", unsafe_allow_html=True)
                    st.markdown(f"<h4 style='margin: 10px 0 0 0; color: #ffdd59;'>{name}</h4></div>", unsafe_allow_html=True)
        else:
            st.write("- (ยังไม่มีตัวละครใน Tier นี้)")
        st.write("")

with tab2:
    st.title("⚙️ Admin Configuration")
    st.markdown("เพิ่มตัวละครใหม่พร้อมใส่ลิงก์รูปภาพ")

    with st.form("add_master_form"):
        new_char = st.text_input("➕ ชื่อตัวละคร:")
        new_img_url = st.text_input("🖼️ ลิงก์รูปภาพตัวละคร (Image URL):")
        submitted_add = st.form_submit_button("เพิ่มตัวละครเข้าฐานข้อมูล")
        if submitted_add and new_char:
            exists = any(item["name"] == new_char for item in st.session_state.all_items)
            if not exists:
                st.session_state.all_items.append({"name": new_char, "image": new_img_url})
                st.success(f"เพิ่ม '{new_char}' เรียบร้อยแล้ว!")
                st.rerun()
            else:
                st.warning("มีตัวละครชื่อนี้อยู่แล้ว")

    st.divider()

    st.subheader("🗑️ จัดการ / ลบตัวละคร")
    if st.session_state.all_items:
        char_names = [item["name"] for item in st.session_state.all_items]
        char_to_delete = st.selectbox("เลือกตัวละครที่ต้องการลบ:", char_names, key="delete_selectbox")
        if st.button("ลบตัวละครนี้", type="primary"):
            st.session_state.all_items = [item for item in st.session_state.all_items if item["name"] != char_to_delete]
            for t in st.session_state.tier_data:
                if char_to_delete in st.session_state.tier_data[t]:
                    st.session_state.tier_data[t].remove(char_to_delete)
            st.success(f"ลบ '{char_to_delete}' เรียบร้อยแล้ว!")
            st.rerun()
    else:
        st.info("ไม่มีตัวละครในระบบ")

    st.divider()
    st.markdown("### 📋 รายชื่อและรูปภาพทั้งหมดในระบบ")
    for idx, item in enumerate(st.session_state.all_items, 1):
        c1, c2 = st.columns([1, 4])
        with c1:
            if item["image"]:
                st.image(item["image"], width=80)
            else:
                st.write("ไม่มีรูป")
        with c2:
            st.write(f"**{idx}. {item['name']}**")
            st.text(f"URL: {item['image'] if item['image'] else '-'}")
        st.divider()
