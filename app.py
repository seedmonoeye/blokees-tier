
แชทใหม่
ค้นหาแชท
พรีพรอมต์
ชุดคำสั่งที่บันทึกไว้
คลัง
เรียนรู้เกี่ยวกับ AI
ผู้ช่วยอัจฉริยะ
โฟลเดอร์

รายการแชท
วิธีสร้างเอไอเอเจนท์เบื้องต้น
Exclusive Versus Limited Product Comparison
ขอคำแปลภาษาไทย
ข้อมูลสตอร์มทรูปเปอร์ในสตาร์วอร์ส
สร้างภาพท่าไม้ตาย Nox Knight
การจัดกลุ่มรูปภาพตามตำแหน่ง
SAP Material Lock Management
Animate source image with movement

คำตอบ

ลิงก์

รูปภาพ

Auto
สอนวิธีทำ Ai Agent หน่อย


Gemini 3.5 Flash Lite
gemini-3.5-flash-lite
เลือกอัตโนมัติ: Gemini 3.5 Flash Lite
การสร้าง AI Agent หรือระบบ AI ที่สามารถคิด วางแผน และลงมือทำภารกิจแทนเราได้ด้วยตัวเอง มีขั้นตอนหลักๆ ที่เข้าใจง่ายดังนี้ครับ

องค์ประกอบหลักของ AI Agent
LLM (สมองส่วนกลาง): โมเดลภาษาขนาดใหญ่ เช่น GPT-4o หรือ Claude เพื่อใช้ในการคิด วิเคราะห์ และตัดสินใจ
Planning (การวางแผน): ความสามารถในการแตกงานใหญ่เป็นงานย่อยๆ และลำดับขั้นตอนการทำ
Memory (ความจำ): ทั้งความจำระยะสั้น (บริบทในการสนทนา) และความจำระยะยาว (การดึงข้อมูลจากฐานข้อมูลหรือ Vector DB)
Tools (เครื่องมือ/ความสามารถเสริม): การเชื่อมต่อกับ API ค้นหาข้อมูลบนเว็บ อ่านไฟล์ หรือสั่งงานโปรแกรมอื่นๆ
ขั้นตอนการสร้าง AI Agent เบื้องต้น
กำหนดเป้าหมายของ Agent: ว่าต้องการให้ทำอะไร เช่น แอดมินตอบแชท, ตัวช่วยค้นหาข้อมูลสรุปบทความ, หรือผู้ช่วยเขียนโค้ด
เลือกเครื่องมือและ Framework:
Python: ภาษาหลักที่นิยมใช้
Framework ยอดนิยม: LangChain, LlamaIndex, หรือ CrewAI (ช่วยให้สร้าง Multi-Agent ได้ง่ายขึ้น)
เขียน Prompt ควบคุมพฤติกรรม: กำหนดบทบาท ขอบเขต และเงื่อนไขการทำงานให้ชัดเจน
เชื่อมต่อ Tool (Function Calling): เปิดให้ AI สามารถเรียกใช้ฟังก์ชันภายนอก เช่น การค้นหาเว็บ (Google Search) หรือคำนวณเลข
ทดสอบและปรับปรุง: รันลองดูว่า Agent ทำตามแผนที่เราวางไว้ไหม ติดลูปตรงไหน แล้วปรับปรุง Prompt หรือระบบจัดการความจำให้ดีขึ้น
สนใจเริ่มต้นสร้าง Agent สำหรับงานด้านไหนเป็นพิเศษไหมครับ ผมจะได้แนะนำเครื่องมือหรือตัวอย่างโค้ดที่เจาะจงให้ได้ครับ


Auto
สามารถสร้าง Promp ในนี้เลยได้ใช่ไหม


Gemini 3.5 Flash Lite
gemini-3.5-flash-lite
เลือกอัตโนมัติ: Gemini 3.5 Flash Lite
ใช่ครับ สามารถพิมพ์บอกรายละเอียดงานที่ต้องการให้ AI Agent ทำมาได้เลย เดี๋ยวผมช่วยออกแบบและเขียน System Prompt ที่มีโครงสร้างชัดเจน (เช่น กำหนดบทบาท หน้าที่ ขั้นตอนการทำงาน และข้อจำกัด) ให้คุณนำไปปรับใช้ได้ทันทีครับ

อยากให้ Agent ทำหน้าที่อะไรและมีเงื่อนไขแบบไหน ลองเล่าให้ฟังได้เลยครับ


Auto
สร้าง AI Agent ในสร้างทำข่าว Event Blokees ที่จะเกิดขึ้น(มีประกาศตาม Social ต่างๆ) จากทั่วโลกมารายงานในนี้ทุกวัน   ทำเป็น การ์ดแบ่งตามเดือน  และเรียงลำดับแต่ละเดือน พร้อมมี อัพเดตให้รายวัน


Gemini 3.5 Flash Lite
gemini-3.5-flash-lite
เลือกอัตโนมัติ: Gemini 3.5 Flash Lite
นี่คือ System Prompt สำหรับนำไปใส่ใน AI Agent เพื่อทำหน้าที่รวบรวมและรายงานข่าว Event ของ Blokees จากทั่วโลก โดยจัดรูปแบบเป็นการ์ดแบ่งตามเดือน เรียงลำดับ และอัปเดตแบบรายวันครับ


Markdown

Markdown

Open
คุณสามารถคัดลอก Prompt ด้านบนนี้ไปวางในระบบ AI หรือ Custom GPT ของคุณได้เลยครับ เมื่อตั้งค่าเสร็จแล้ว ในแต่ละวันคุณสามารถพิมพ์ทักทายเพื่อให้ Agent เริ่มค้นหาและอัปเดตข่าวสารของ Blokees ล่าสุดได้ทันทีครับ อยากให้ปรับแต่งเงื่อนไขส่วนไหนเพิ่มเติมไหมครับ?


Auto
สร้างโปรแกรมสำหรัย จัด Tier สินค้า Blokees Champion Class Marvel ทั้งหมด ให้หน่อย


Gemini 3.5 Flash Lite
gemini-3.5-flash-lite
เลือกอัตโนมัติ: Gemini 3.5 Flash Lite
นี่คือโค้ดโปรแกรม Python (ใช้ Streamlit สำหรับทำเว็บแอปง่ายๆ) ที่คุณสามารถนำไปรันเพื่อสร้างระบบ Tier List สำหรับจัดอันดับสินค้า Blokees Champion Class (Marvel) ได้ทันครับ โดยโปรแกรมนี้จะมีข้อมูลตั้งต้นของซีรีส์ Marvel Champion Class มาให้ และเปิดให้คุณลากจัดอันดับ หรือเพิ่มตัวละครใหม่เข้าไปได้

วิธีใช้งานเบื้องต้น
ติดตั้งไลบรารีที่จำเป็นผ่าน Terminal: pip install streamlit
เซฟโค้ดด้านล่างนี้ลงในไฟล์ชื่อ app.py
รันคำสั่ง: streamlit run app.py
โค้ดโปรแกรม (app.py)

Code

Code · PY

Open
คุณสามารถนำโค้ดนี้ไปลองรันและปรับแต่งชื่อตัวละครในกลุ่ม Champion Class ของ Marvel เพิ่มเติมได้ตามต้องการเลยครับ!


Auto
วางใน Stramlite pังไง


Gemini 3.5 Flash Lite
gemini-3.5-flash-lite
เลือกอัตโนมัติ: Gemini 3.5 Flash Lite
วิธีนำโค้ด Streamlit ไปรันบนเครื่องของคุณทีละขั้นตอน มีดังนี้ครับ:

ติดตั้ง Python (ถ้ายังไม่มี)
โหลดจากเว็บไซต์ทางการ 
Python
 มาติดตั้ง (อย่าลืมติ๊กเลือกคำว่า Add Python to PATH ตอนติดตั้งด้วยนะครับ)
เปิดโปรแกรม Command Prompt (Windows) หรือ Terminal (Mac)
ติดตั้งไลบรารี Streamlit
พิมพ์คำสั่งนี้แล้วกด Enter:
bash


pip install streamlit
สร้างไฟล์โค้ด
สร้างไฟล์ Text ขึ้นมาใหม่ (ใช้ Notepad หรือ VS Code ก็ได้)
คัดลอกโค้ด Python ที่ผมให้ไปก่อนหน้ามาวางทั้งหมด
บันทึกไฟล์เป็นชื่อ app.py (เลือก Save as type เป็น All Files หรือตั้งชื่อให้ลงท้ายด้วย .py)
รันโปรแกรม
ที่ Command Prompt / Terminal ให้พิมพ์ cd ตามด้วยโฟลเดอร์ที่คุณเก็บบันทึกไฟล์ app.py ไว้ (เช่น cd Desktop)
พิมพ์คำสั่งรัน:
bash


streamlit run app.py
ระบบจะเปิดหน้าเว็บเบราว์เซอร์ขึ้นมาให้อัตโนมัติ (หรือคลิก Links ที่ขึ้นมาในหน้า Terminal เช่น http://localhost:8501) เพื่อใช้งานโปรแกรม Tier List ได้เลยครับ!

Auto
จากโปรแกรมเดิมด้านบน ทำให้มีหน้าจอ Admin สำหรับใส่ Config เพิ่มลดตัวละครให้หน่อย เพราะตัวละครที่ให้มาไม่ถุกนะ


Gemini 3.5 Flash Lite
gemini-3.5-flash-lite
เลือกอัตโนมัติ: Gemini 3.5 Flash Lite
จัดการเพิ่มระบบ Admin Panel สำหรับจัดการ (เพิ่ม/ลบ) รายชื่อตัวละครตั้งต้นได้แบบเรียลไทม์เรียบร้อยครับ โดยจะมีการแบ่งแท็บระหว่างหน้า "🏆 Tier List (หน้าจัดอันดับ)" กับหน้า "⚙️ Admin Config (ตั้งค่าตัวละคร)" ให้ใช้งานได้สะดวกขึ้นครับ

โค้ดโปรแกรม app.py (เวอร์ชันอัปเดต)

Code

Code · PY

Open
สิ่งที่เพิ่มเข้ามาในเวอร์ชันนี้:
แบ่งเป็น 2 Tab ชัดเจน:
Tab แรกสำหรับจัดอันดับตัวละคร
Tab สองคือ หน้า Admin Config สำหรับจัดการเพิ่ม/ลบรายชื่อตัวละคร
ระบบจัดการฐานข้อมูลชั่วคราว: เมื่อคุณกดเพิ่มหรือลบตัวละครในหน้า Admin รายชื่อในหน้าจัดอันดับจะอัปเดตตามทันที ทำให้คุณสามารถเคลียร์รายชื่อเก่าที่ผิดออก แล้วใส่รายชื่อจริงของ Blokees Champion Class Marvel เข้าไปใหม่ได้ทั้งหมดครับ

Auto
เอาแบบใส่ภาพได้ด้วยนะ


Gemini 3.5 Flash Lite
gemini-3.5-flash-lite
เลือกอัตโนมัติ: Gemini 3.5 Flash Lite
เพิ่มความสามารถในการ อัปโหลดและแสดงรูปภาพ สำหรับแต่ละตัวละครเข้าไปในโปรแกรมแล้วครับ โดยตอนนี้ทั้งหน้า Admin และหน้าจัดอันดับจะรองรับการแสดงรูปภาพประกอบโมเดล Blokees เพื่อความสวยงามสมจริงในการทำ Tier List ครับ

โค้ดโปรแกรม app.py (เวอร์ชันรองรับรูปภาพ)

Code

Code · PY

Open
วิธีใช้งานส่วนรูปภาพ:
ในหน้า Admin Config คุณสามารถใส่ชื่อตัวละครพร้อมกับวาง Image URL (ลิงก์รูปภาพ) ของตัวละครนั้นๆ ได้ทันที (เช่น คลิกขวาที่รูปสินค้าในเว็บแล้วเลือก Copy Image Address มาวาง)
เมื่อกดเพิ่ม รูปภาพจะไปแสดงผลร่วมกับการ์ดจัดอันดับในหน้า Tier List ทันทีครับ

Auto
มีลิ้งสอนวิธีลงโปรแกรมไหม


Gemini 3.5 Flash Lite
gemini-3.5-flash-lite
เลือกอัตโนมัติ: Gemini 3.5 Flash Lite
คุณสามารถศึกษาคู่มือและวิธีติดตั้งโปรแกรมอย่างละเอียดจากเว็บไซต์หลักและบทความแนะนำด้านล่างนี้ได้เลยครับ:

อ่านคู่มือและวิธีติดตั้งอย่างเป็นทางการได้ที่ 
Streamlit Installation Docs
ดูบทความสอนเริ่มต้นใช้งานภาษาไทย เข้าใจง่าย ได้ที่ 
DataRockie - สอนวิธีทำ Web App ด้วย Streamlit
หลักๆ จะมีขั้นตอนสั้นๆ คือติดตั้ง Python ลงในเครื่อง เปิดคอมมานด์พาสแล้วพิมพ์คำสั่ง pip install streamlit เพื่อติดตั้งตัวโปรแกรม จากนั้นก็สร้างไฟล์โค้ดแล้วรันคำสั่ง streamlit run ชื่อไฟล์.py ตามที่แนะนำไปได้เลยครับ มีตรงไหนติดขัดหรืออยากให้ช่วยอธิบายเพิ่ม สอบถามได้เลยนะครับ!



แหล่งข้อมูล (4)

Auto
มี Run Python ที่ง่ายกว่านี้มะ


Gemini 3.5 Flash Lite
gemini-3.5-flash-lite
เลือกอัตโนมัติ: Gemini 3.5 Flash Lite
มีวิธีที่ง่ายและสะดวกกว่าการลง Python และพิมพ์คำสั่งเองในเครื่องมากๆ ครับ โดยคุณ ไม่ต้องติดตั้งอะไรเลย สามารถรันโค้ดผ่านเว็บไซต์บนมือถือหรือคอมพิวเตอร์ได้ทันทีผ่านเครื่องมือเหล่านี้:

Google Colab (แนะนำสำหรับรันและทดลอง)
เป็นบริการจาก Google ที่ให้รันโค้ด Python บนคลาวด์ฟรีผ่านเบราว์เซอร์
วิธีใช้: เข้าไปที่เว็บไซต์ 
Google Colab
 แล้วสร้างไฟล์ใหม่ (New Notebook)
วางโค้ด Python ลงไป (แต่ตัว Streamlit อาจจะต้องปรับรูปแบบนิดหน่อยให้แสดงผลใน Colab หรือใช้เครื่องมืออื่นแทน)
Streamlit Community Cloud (สำหรับทำเว็บแอปแจกเพื่อนใช้)
ถ้าคุณต้องการแชร์ลิงก์เว็บ Tier List ให้คนอื่นเข้ามาเล่นด้วยได้ คุณสามารถเอาโค้ดไปฝากไว้ที่ GitHub แล้วเชื่อมต่อกับ 
Streamlit Community Cloud
 ฟรี
มันจะสร้างเว็บไซต์ให้คุณแบบอัตโนมัติ โดยที่คุณไม่ต้องตั้งค่าเซิร์ฟเวอร์เองเลยครับ
ใช้ AI หรือเครื่องมือ No-Code ช่วยสร้างเว็บ
ถ้าต้องการทำเว็บแอปแบบลากวางรูปภาพจัด Tier ได้ง่ายๆ โดยไม่ต้องเขียนโค้ดเลย แนะนำให้ใช้เว็บไซต์ประเภท Website Builder หรือเครื่องมือสร้าง Tier List สำเร็จรูป เช่น 
Tiermaker
 ซึ่งคุณสามารถอัปโหลดรูปตัวละคร Blokees เข้าไปแล้วกดจัดอันดับได้ทันทีโดยไม่ต้องเขียนโปรแกรมครับ
สะดวกทางไหนลองเลือกดูได้เลยครับ หรือถ้าอยากให้แนะนำวิธีใช้ Google Colab เพิ่มเติมบอกได้นะครับ!


Auto
ทำ Code สำหรับใช้ใน 
Google Colab


Gemini 3.5 Flash Lite
gemini-3.5-flash-lite
เลือกอัตโนมัติ: Gemini 3.5 Flash Lite
นี่คือโค้ดสำหรับนำไปรันบน Google Colab โดยใช้ไลบรารี streamlit ร่วมกับ localtunnel เพื่อสร้างลิงก์หน้าเว็บให้คุณคลิกเข้าไปใช้งานแอปจัด Tier Blokees ได้ทันทีผ่านเบราว์เซอร์ครับ

วิธีใช้งานใน Google Colab:
เข้าไปที่ 
Google Colab
 แล้วกด New Notebook
คัดลอกโค้ดด้านล่างนี้ไปวางทั้งหมดในช่อง Code Cell
กดปุ่ม Play (รัน)
รอสักครู่จนกว่าจะมีลิงก์ (เช่น https://...loca.lt) ปรากฏขึ้นมา ให้คลิกเข้าไปใช้งานได้เลยครับ (ตอนเข้าเว็บครั้งแรกอาจจะมีหน้าจอเตือนความปลอดภัย ให้กดปุ่ม Proceed เพื่อข้ามไปหน้าเว็บได้เลย)
โค้ดสำหรับรันใน Colab (app.py)

Code

Code · PY

Open
เมื่อรันโค้ดชุดนี้ใน Colab แล้ว จะมีลิงก์ขึ้นมาให้กดเข้าไปใช้งานได้ทันทีครับ สะดวกและไม่ต้องลงโปรแกรมอะไรในเครื่องเลย!


Auto
ลองแล้ว error นะ ERROR: Ignored the following versions that require a different python version: 0.55.2 Requires-Python <3.5
ERROR: Could not find a version that satisfies the requirement localtunnel (from versions: none)
ERROR: No matching distribution found for localtunnel


Gemini 3.5 Flash Lite
gemini-3.5-flash-lite
เลือกอัตโนมัติ: Gemini 3.5 Flash Lite
อ๋อ ข้อผิดพลาดนี้เกิดขึ้นเพราะแพ็กเกจ localtunnel บน Python ไม่มีอยู่จริงครับ (เพราะตัว localtunnel ต้นฉบับเป็นของฝั่ง Node.js)

ทางแก้ที่ง่ายและเสถียรที่สุดใน Google Colab ตอนนี้คือเปลี่ยนมาใช้ pyngrok แทนครับ ซึ่งใช้งานได้ง่ายและสร้างลิงก์เว็บได้เสถียรมากๆ

วิธีแก้ไขใน Google Colab:
ให้ลบโค้ดเก่าในช่อง Code ออกทั้งหมด แล้วเปลี่ยนมาใช้โค้ดชุดนี้แทนครับ:


Code

Code · PY

Open
พอนำไปรันแล้ว มันจะแสดงลิงก์ https://xxxx.ngrok-free.app ขึ้นมาที่ด้านล่าง ให้คลิกเข้าไปใช้งานได้ทันทีเลยครับ!


Auto
ยัง Error UsageError: Line magic function `%%writefile` not found.


Gemini 3.5 Flash Lite
gemini-3.5-flash-lite
เลือกอัตโนมัติ: Gemini 3.5 Flash Lite
Ah ขออภัยด้วยครับ! อาการนี้เกิดจากการวางรหัสใน Google Colab แบบพิมพ์ธรรมดา ทำให้ Colab มองไม่เห็นคำสั่งระบบอย่าง %%writefile (เพราะไปรันผ่านช่องแชทหรือเก็บบล็อกโค้ดผิดประเภท)

วิธีแก้ที่ง่ายและชัวร์ที่สุดโดยไม่ต้องใช้คำสั่งเขียนไฟล์ซับซ้อนใน Colab คือ ให้สร้างไฟล์ผ่านหน้าต่าง File Explorer ด้านซ้ายมือของ Colab แทนครับ ทำตามนี้ได้เลยครับ:

วิธีทำใน Google Colab แบบไม่ให้ Error:
สร้างไฟล์ชื่อ app.py ด้วยมือ:
มองไปที่แถบเมนูด้านซ้ายของ Google Colab
คลิกที่ไอคอน รูปแฟ้มเอกสาร (Files)
คลิกขวาที่พื้นที่ว่างๆ เลือก New file แล้วตั้งชื่อว่า app.py
คัดลอกโค้ดด้านล่างนี้ไปวาง:
ดับเบิลคลิกไฟล์ app.py ที่เพิ่งสร้าง แล้วคัดลอกโค้ด Python นี้ไปวางทั้งหมด แล้วกด Save (Ctrl+S หรือ Cmd+S)

Code

Code · PY

Open
สร้าง Cell ใหม่เพื่อรันโปรแกรม:
กลับมาที่หน้าจอหลักของ Colab แล้วสร้าง Code Cell ใหม่ขึ้นมา (กดปุ่ม + Code)
ใส่โค้ดติดตั้งไลบรารีและรัน ngrok ด้านล่างนี้ลงไปแล้วกดรัน:

Code

Code · PY

Open
วิธีนี้จะสะอาดและไม่ติดปัญหาเรื่องคำสั่งลัด %%writefile แน่นอนครับ ลองดูนะครับ!


Auto
เจอ Error นี้แทน 
ERROR:pyngrok.process.ngrok:t=2026-10-30T02:53:42+0000 lvl=eror msg="failed to reconnect session" obj=tunnels.session err="authentication failed: This ngrok session is not authenticated. ngrok requires an account and a valid credential to start a session.\n\nSign up for an account: https://dashboard.ngrok.com/signup\nGet your credential: https://dashboard.ngrok.com/get-started/your-authtoken\r\n\r\nERR_NGROK_4018\r\n"
ERROR:pyngrok.process.ngrok:t=2026-10-30T02:53:42+0000 lvl=eror msg="session closing" obj=tunnels.session err="authentication failed: This ngrok session is not authenticated. ngrok requires an account and a valid credential to start a session.\n\nSign up for an account: https://dashboard.ngrok.com/signup\nGet your credential: https://dashboard.ngrok.com/get-started/your-authtoken\r\n\r\nERR_NGROK_4018\r\n"
CRITICAL:pyngrok.process.ngrok:t=2026-10-30T02:53:42+0000 lvl=crit msg="command failed" err="authentication failed: This ngrok session is not authenticated. ngrok requires an account and a valid credential to start a session.\n\nSign up for an account: https://dashboard.ngrok.com/signup\nGet your credential: https://dashboard.ngrok.com/get-started/your-authtoken\r\n\r\nERR_NGROK_4018\r\n"
---------------------------------------------------------------------------
PyngrokNgrokError                         Traceback (most recent call last)
/tmp/ipykernel_4327/406256299.py in <cell line: 0>()
     13 
     14 # สร้าง Public URL
---> 15 public_url = ngrok.connect(8501)
     16 print(f"👉 คลิก Link ด้านล่างนี้เพื่อเข้าใช้งานหน้าเว็บ Tier List ได้เลยครับ:\n{public_url}")

3 frames
/usr/local/lib/python3.13/dist-packages/pyngrok/process.py in _start_process(pyngrok_config)
    459 
    460         if ngrok_process.startup_error is not None:
--> 461             raise PyngrokNgrokError(f"The ngrok process errored on start: {ngrok_process.startup_error}.",
    462                                     ngrok_process.logs,
    463                                     ngrok_process.startup_error)

PyngrokNgrokError: The ngrok process errored on start: authentication failed: This ngrok session is not authenticated. ngrok requires an account and a valid credential to start a session.\n\nSign up for an account: https://dashboard.ngrok.com/signup\nGet your credential: https://dashboard.ngrok.com/get-started/your-authtoken\r\n\r\nERR_NGROK_4018\r\n.

ERROR:pyngrok.process.ngrok:t=2026-10-30T02:53:42+0000 lvl=eror msg="failed to reconnect session" obj=tunnels.session err="authentication failed: This ngrok session is not authenticated. ngrok requires an account and a valid credential to start a session.\n\nSign up for an account: https://dashboard.ngrok.com/signup\nGet your credential: https://dashboard.ngrok.com/get-started/your-authtoken\r\n\r\nERR_NGROK_4018\r\n"
ERROR:pyngrok.process.ngrok:t=2026-10-30T02:53:42+0000 lvl=eror msg="session closing" obj=tunnels.session err="authentication failed: This ngrok session is not authenticated. ngrok requires an account and a valid credential to start a session.\n\nSign up for an account: https://dashboard.ngrok.com/signup\nGet your credential: https://dashboard.ngrok.com/get-started/your-authtoken\r\n\r\nERR_NGROK_4018\r\n"
CRITICAL:pyngrok.process.ngrok:t=2026-10-30T02:53:42+0000 lvl=crit msg="command failed" err="authentication failed: This ngrok session is not authenticated. ngrok requires an account and a valid credential to start a session.\n\nSign up for an account: https://dashboard.ngrok.com/signup\nGet your credential: https://dashboard.ngrok.com/get-started/your-authtoken\r\n\r\nERR_NGROK_4018\r\n"
------------


Gemini 3.5 Flash Lite
gemini-3.5-flash-lite
เลือกอัตโนมัติ: Gemini 3.5 Flash Lite
อ๋อ ช่วงหลังๆ มานี้ ngrok บังคับให้ต้องใส่ Token (สมัครบัญชีฟรีแล้วเอา Token มาใส่) ครับ ถึงจะเปิดใช้งานได้

เพื่อให้ง่ายและไม่ต้องไปสมัครบัญชี ngrok ใหม่ ผมแนะนำให้เปลี่ยนไปใช้ localtunnel ผ่านคำสั่ง Node.js (ตัวนี้ไม่ต้องใช้ Token และเปิดใช้งานได้เลยทันที) แทนครับ

ทำตามนี้ได้เลยครับ:

วิธีแก้: ใช้ localtunnel (แบบรันผ่าน Node.js ใน Colab)
ให้เปลี่ยนโค้ดในช่องรัน (Cell ที่ใช้รันเว็บ) เป็นชุดนี้แทนครับ:


Code

Code · PY

Open
วิธีเข้าใช้งานหลังจากรันเสร็จ:
พอมันรันเสร็จ จะมีลิงก์เว็บขึ้นมา (เช่น https://red-tigons-jump.loca.lt) ให้คลิกเข้าไป
ถ้ามันเด้งไปหน้าจอสีเทาที่มีคำว่า "Password" หรือ "Tunnel Password" ให้เอารหัสผ่านที่เป็น IP ตัวเลข (ที่พิมพ์โชว์ไว้ด้านบนช่องรัน) ไปกรองใส่ แล้วกด Click to Submit ก็จะเข้าหน้าเว็บแอปของเราได้ทันทีครับ!

Auto
web ขึ้นแล้วแต่ Error TypeError: Failed to fetch dynamically imported module: https://full-wings-lie.loca.lt/static/js/Selectbox.DYo6P43Q.js


Gemini 3.5 Flash Lite
gemini-3.5-flash-lite
เลือกอัตโนมัติ: Gemini 3.5 Flash Lite
อาการนี้เกิดจากกลไกความปลอดภัยของ localtunnel ที่มักจะบล็อกหรือดึงไฟล์ JavaScript/Static บางตัวของ Streamlit ไม่ผ่าน ทำให้เบราว์เซอร์โหลดโมดูลไม่ได้ครับ

วิธีแก้ที่เสถียรที่สุดและไม่ต้องเจอปัญหาเรื่องไฟล์ Static หลุดแบบนี้ คือเปลี่ยนมาใช้ Streamlit Community Cloud (ฟรี) หรือถ้าต้องการรันบน Google Colab แบบไร้ปัญหาเรื่องหน้าเว็บพัง แนะนำให้ใช้เครื่องมือเปิดพอร์ตตัวอื่นอย่าง lt แบบกำหนด config หรือใช้ Streamlit Native sharing ครับ

แต่ถ้าอยากแก้ปัญหาเฉพาะหน้าบน Colab ให้จบในคลิกเดียว แนะนำให้ลองเปลี่ยนมาใช้บริการ localtunnel แบบไม่ผ่านเบราว์เซอร์กลาง หรือเปลี่ยนไปใช้ FastAPI / Gradio แทน ซึ่งเหมาะกับการรันบน Colab มากกว่า Streamlit ครับ

หรือทางเลือกที่ง่ายและสวยงามที่สุดสำหรับการทำเว็บแอปไว้ใช้เองหรือแชร์ให้เพื่อน โดย ไม่ต้องมานั่งแก้โค้ดแก้ Error เรื่องลิงก์หลุด คือเอาไฟล์ app.py ไปขึ้น Streamlit Cloud ตามขั้นตอนนี้ครับ:

นำโค้ด Python ที่เราทำกันไปอัปโหลดขึ้น GitHub ของตัวเอง (สร้าง Repository ใหม่ แล้วอัปโหลดไฟล์ app.py)
เข้าไปที่เว็บไซต์ 
Streamlit Community Cloud
 แล้วกด Login ด้วย GitHub ฟรี
กดปุ่ม New app -> เลือก Repository และไฟล์ app.py ของคุณ -> กด Deploy
ระบบจะสร้างลิงก์เว็บไซต์ถาวร (เช่น https://your-app.streamlit.app) ให้คุณใช้งานได้ตลอด 24 ชั่วโมง โดยไม่มีวันหมดอายุ และไม่มีปัญหาเรื่องหน้าเว็บพังหรือ Error โหลดไฟล์ไม่ได้แบบ localtunnel แน่นอนครับ! ลองวิธีนี้ดูนะครับ สะดวกและจบปัญหาในระยะยาวเลยครับ


Auto
Streamlit Community Cloud ทำยังไง


Gemini 3.5 Flash Lite
gemini-3.5-flash-lite
เลือกอัตโนมัติ: Gemini 3.5 Flash Lite
การนำแอปขึ้น Streamlit Community Cloud เพื่อให้ได้เว็บไซต์ใช้งานจริงแบบถาวร (มีลิงก์แชร์ให้เพื่อนเล่นได้ฟรีตลอด 24 ชั่วโมง) มีขั้นตอนง่ายๆ ดังนี้ครับ:

ขั้นตอนที่ 1: เตรียมไฟล์โค้ด (บนคอมพิวเตอร์ของคุณ)
สร้างโฟลเดอร์เปล่าๆ บนคอมพิวเตอร์ของคุณ (เช่น ตั้งชื่อว่า blokees-tier)
สร้างไฟล์โค้ดแอปของคุณแล้วบันทึกชื่อเป็น app.py (ใช้โค้ดตัวเดิมที่เราทำกันไว้ได้เลย)
สร้างไฟล์เพิ่มอีก 1 ไฟล์ชื่อ requirements.txt เพื่อบอกให้ระบบรู้ว่าต้องลงไลบรารีอะไรบ้าง โดยเปิดไฟล์นี้ขึ้นมาแล้วพิมพ์คำว่า:
text


streamlit
แล้วกดบันทึก (ไฟล์นี้สำคัญมาก เพื่อให้เว็บรันไลบรารี Streamlit ได้ครับ)
ขั้นตอนที่ 2: อัปโหลดโค้ดขึ้น GitHub
สมัครสมาชิกหรือเข้าใช้งานเว็บไซต์ 
Github
 (ฟรี)
ที่มุมขวาบน ให้คลิกเครื่องหมาย + แล้วเลือก New repository
ตั้งชื่อ Repository (เช่น blokees-tier) เลือกเป็น Public แล้วกด Create repository
ในหน้าจอที่ ให้นำไฟล์ app.py และ requirements.txt ที่เตรียมไว้ลากวาง (Drag & Drop) อัปโหลดขึ้นไปบนเว็บ GitHub แล้วกดปุ่ม Commit changes ด้านล่างสุด
ขั้นตอนที่ 3: Deploy ขึ้น Streamlit Cloud
เข้าไปที่เว็บไซต์ 
Streamlit Community Cloud
กดปุ่ม Sign in แล้วเลือกเข้าสู่ระบบด้วยบัญชี GitHub ของคุณ (อนุญาตการเชื่อมต่อให้เรียบร้อย)
เมื่อเข้าสู่หน้าแดชบอร์ด ให้กดปุ่ม New app
ในหน้าตั้งค่าการ Deploy ให้เลือกข้อมูลดังนี้:
Repository: เลือก ชื่อบัญชีของคุณ/blokees-tier (อันที่เราเพิ่งสร้าง)
Branch: main (หรือ master)
Main file path: ระบบจะเลือก app.py ให้ให้อัตโนมัติ
กดปุ่ม Deploy! ด้านล่างได้เลยครับ
รอระบบติดตั้งสักครู่ (ประมาณ 1-2 นาที) เว็บไซต์ Tier List ของคุณก็จะรันขึ้นมาพร้อมใช้งาน และจะได้ลิงก์เว็บถาวร (เช่น https://blokees-tier.streamlit.app) สามารถก็อปปี้ลิงก์ไปเปิดในมือถือหรือส่งให้คนอื่นดูได้ทันทีเลยครับ!


Auto
ในหน้าจอที่ ให้นำไฟล์ app.py และ requirements.txt ที่เตรียมไว้ลากวาง (Drag & Drop) อัปโหลดขึ้นไปบนเว็บ GitHub แล้วกดปุ่ม Commit changes ด้านล่างสุด 

วางตรงไหน


Gemini 3.5 Flash Lite
gemini-3.5-flash-lite
เลือกอัตโนมัติ: Gemini 3.5 Flash Lite
ในหน้าจอสร้าง Repository ใหม่ของ GitHub หลังจากที่คุณตั้งชื่อและกด Create เรียบร้อยแล้ว มันจะพามาที่หน้าจอแนะนำวิธีอัปโหลดโค้ดครับ

ให้สังเกตตรงกลางหน้าจอ จะมีข้อความภาษาอังกฤษว่า:

"Quick setup — if you’ve done this kind of thing before..." (หรือสังเกตลิงก์ย่อยๆ)

ให้มองหาประโยคสั้นๆ ที่มีขีดเส้นใต้คำว่า "uploading an existing file" แล้วคลิกที่ลิงก์นั้นครับ

พอลิกก์เข้าไปแล้ว หน้าจอจะเปลี่ยนเป็นช่องสี่เหลี่ยมใหญ่ๆ ที่มีข้อความบอกว่า "Drag files here to add them to your repository"

ทีนี้คุณก็สามารถลากไฟล์ app.py และ requirements.txt มาวางในช่องนั้นได้เลยครับ พ่าวางเสร็จแล้วเลื่อนลงมาด้านล่างสุด จะเจอปุ่มสีเขียวเขียนว่า "Commit changes" ให้กดปุ่มนั้นเป็นอันเสร็จขั้นตอนการอัปโหลดครับ!


Auto
ปรับหน้าจอแสดงตัวละครให้ใหญ่นี้หน่อย


Gemini 3.5 Flash Lite
gemini-3.5-flash-lite
เลือกอัตโนมัติ: Gemini 3.5 Flash Lite
อัปเดตโค้ดในไฟล์ app.py ของคุณให้แสดงผลรูปภาพและชื่อตัวละครในหน้าจัดอันดับให้มี ขนาดใหญ่ขึ้นและดูเด่นชัดขึ้น เรียบร้อยครับ โดยปรับใช้การจัดคอลัมน์ใหม่ (เหลือ 3 คอลัมน์ต่อแถวแทนที่จะเป็น 4) และขยายขนาดการแสดงผลให้เต็มตาขึ้นครับ

คุณสามารถคัดลอกโค้ดชุดนี้ไปแทนที่ไฟล์ app.py เดิมของคุณได้เลยครับ:


Code

Code · PY

Open
หากคุณใช้งานบน Streamlit Cloud อยู่แล้ว เมื่อวางโค้ดนี้ทับลงใน GitHub ตัวเว็บจะทำการอัปเดตให้อัตโนมัติ (หรือกด Reboot ในหน้าแดชบอร์ด) รูปการ์ดตัวละครจะใหญ่และดูสวยงามขึ้นทันทีครับ!

ถามได้เลย

AI อาจผิดพลาดได้ หลีกเลี่ยงการใส่ข้อมูลส่วนตัวหรือความลับ

Code
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
