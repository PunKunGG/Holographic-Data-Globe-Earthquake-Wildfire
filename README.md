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
