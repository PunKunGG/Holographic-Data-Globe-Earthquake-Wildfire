# 🌍 Holographic Data Globe
โปรแกรมจำลองลูกโลกอินเทอร์แอคทีฟแสดงข้อมูล แผ่นดินไหว (Earthquake) และ ภัยธรรมชาติ/ไฟป่า (Wildfire) จาก USGS และ NASA EONET API
รันได้บน Google Colab โดยใช้ Python + Plotly + Gradio พร้อมระบบ Animation, Export

Mini Project นี้เป็นงาน Final Project ของรายวิชา CP352301 Script Programming ภาคเรียนที่ 1 ปีการศึกษา 2568

# ความคืบหน้าของแต่ละสัปดาห์
# 🌀 Sprint 1 (Week 1)
# เป้าหมาย
- กำหนดขอบเขตโปรเจกต์และแหล่งข้อมูล API ที่จะใช้
- ทดลองเรียกข้อมูลจาก USGS Earthquake API และ NASA EONET API
- แปลงข้อมูลให้อยู่ในรูป DataFrame พร้อมเขียนลงไฟล์ .csv
- ออกแบบโครงสร้างโฟลเดอร์และเตรียม data pipeline เบื้องต้น
# Deliverables สัปดาห์ที่ 1
- ดึงข้อมูลจาก API ได้สำเร็จ ✅
- บันทึกและอ่านข้อมูลจาก CSV ✅
- สร้างไฟล์ earthquakes.csv และ eonet_events.csv ✅
- วางแผน GUI Layout เบื้องต้น (ใน Gradio) ✅

# 🌏 Sprint 2 (Week 2)
# เป้าหมาย
- สร้างระบบแสดงผลแบบ Interactive Globe ด้วย Plotly
- วางเลเยอร์แยก Earthquake และ Wildfire
- เพิ่มปุ่ม Dropdown สำหรับเลือกเลเยอร์
- เพิ่ม filter control: วันที่, Magnitude, Region
# Deliverables สัปดาห์ที่ 2
- ลูกโลกแสดงข้อมูล Earthquake/Wildfire ✅
- ปรับสีและขนาดจุดตาม magnitude ✅
- Dropdown: All / Earthquake / Wildfire ✅
- Region Presets (Global / SEA / Japan / US West) ✅

# 🔥 Sprint 3 (Week 3)
# เป้าหมาย
- สรุปข้อมูลเชิงสถิติ: จำนวน EQ ต่อวัน, Magnitude เฉลี่ย, Bins สำหรับ heatmap
# Deliverables สัปดาห์ที่ 3
- ตารางสรุปสถิติ + Daily Stats ✅
- Lat/Lon Bins พร้อมนำไปทำ Heatmap ต่อได้ ✅

# 🚀 Sprint Final (Week 4)
# เป้าหมาย
- รวมทุกระบบเข้าด้วยกันใน GUI (Gradio)
- เพิ่มปุ่ม Export เป็นไฟล์ globe_export.html
- เพิ่มหน้า Summary และสถิติแบบ DataFrame
- ปรับให้ทำงานได้บน Colab 100% (CSV-only, ไม่ใช้ SQLite)
# Deliverables Sprint Final
- GUI ทำงานครบทุกส่วน ✅
- Export HTML พร้อมใช้นำเสนอ ✅
- ระบบ Alert พร้อมทดสอบจริง ✅
- โครงรายงานและ README.md ครบ ✅

# 📘 วิธีการติดตั้งและใช้งาน
หมายเหตุ: ใช้ Google Colab ในการรันโปรแกรม

# ขั้นตอนการรันโปรแกรม
1. อัปโหลดโฟลเดอร์โปรเจกต์ทั้งหมดขึ้น Colab
2. รันเซลล์ติดตั้งไลบรารี (pandas, numpy, plotly, gradio, requests)
3. รันเซลล์ที่มีโค้ดโปรแกรม (globe.ipynb)
4. ในหน้าต่าง GUI (Gradio):
   - ตั้งวันที่เริ่มต้น/สิ้นสุด
   - Region = Global
   - Min Magnitude = 4.5
   - ติ๊ก ✅ Fetch & append to CSV now
   - กด Render/Update
5. เมื่อโหลดข้อมูลเสร็จ จะปรากฏลูกโลก 3D หมุนได้
6. (ออปชัน) ตั้งค่า Alert เมื่อ EQ ≥ 6.0
7. กด Export HTML เพื่อบันทึกลูกโลกไว้เป็นไฟล์

# 🧠 ฟีเจอร์ทั้งหมด
✅ ดึงข้อมูลจาก USGS & NASA API
✅ เก็บข้อมูลใน CSV
✅ แสดงลูกโลก 3D Interactive
✅ Filter: Date / Region / Magnitude / Depth
✅ Timeline Animation (ปุ่ม Play/Pause)
✅ Summary Stats + Daily Stats + Lat/Lon Heat Bins
✅ Export HTML

# 🌐 ตัวอย่างแหล่งข้อมูล

- USGS Earthquake API: https://earthquake.usgs.gov/fdsnws/event/1/
- NASA EONET API: https://eonet.gsfc.nasa.gov/api/v3/events

# 🧩 ทีมพัฒนา
- ศิวภาส ภูศรีอ่อน	  เขียนโค้ดหลัก, สร้าง GUI, เขียนระบบ Animation และ Export
- ภควรรธ บุญเรือง  ทดสอบ API และตรวจสอบข้อมูล, จัดการโครงสร้าง CSV
- รัชภูมิ ทองแดง   จัดทำรายงาน, สร้าง README และเตรียมสไลด์นำเสนอ

# 🗓️ แหล่งรันจริง (Google Colab)
- 🌍 Final Version: https://colab.research.google.com/drive/16e3xX0SCINoUltBs4CfmZZSrQMQtEKWq?usp=sharing
- ⚙️ Public Link: https://32d69206df7281e6c6.gradio.live/
