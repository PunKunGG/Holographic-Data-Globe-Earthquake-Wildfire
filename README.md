# 🌏 Holographic Data Globe — Earthquake & Wildfire
เป็นโปรแกรมจำลองข้อมูลเชิงภูมิศาสตร์ในรูปแบบ Globe Visualization โดยเน้นแสดงข้อมูลภัยพิบัติ เช่น แผ่นดินไหวและไฟป่า ผ่านการใช้ Data Visualization แบบโฮโลกราฟิก (Holographic/3D Globe)

## ⚙️ Features
- ดึงข้อมูลภัยพิบัติจาก API ภายนอก (เช่น Earthquake และ Wildfire API)
- เก็บและปรับแต่งข้อมูลให้อยู่ในรูปแบบ CSV
- กรองข้อมูล (Filtering) ตามเงื่อนไข เช่น วันที่, พื้นที่, ความรุนแรง
- แสดงผลข้อมูลบน Globe พร้อมปุ่มควบคุม
- แสดง Heatmap และ Insight จากข้อมูล
- มีส่วนติดต่อผู้ใช้ (GUI) สำหรับควบคุมการแสดงผล

## Project Structure
Holographic-Data-Globe-Earthquake-Wildfire-main/
- │
- ├── [Script] Code_FinalProj/
- │   ├── cell_1.py                # ส่วนเริ่มต้นของโปรเจกต์ เช่น import libraries / setup
- │   ├── cell_2.py                # การเตรียมข้อมูลเบื้องต้น
- │   ├── cell_3_API&CSVappend.py  # การดึงข้อมูลจาก API และบันทึกลง CSV
- │   ├── cell_4_Filter_CSV.py     # การกรองข้อมูล CSV
- │   ├── cell_5_Globe&Button.py   # ส่วนของ globe visualization และปุ่มควบคุม
- │   ├── cell_6_Insigh&Heatmap.py # การสร้าง Heatmap และ Insight Visualization
- │   ├── cell_7_GUI.py            # ส่วนของ GUI / main application interface
- │
- └── README.md                    # (มีอยู่ แต่ไม่ได้ใช้ในการสรุป)

## ⚙️ Requirements

- Python >= 3.8  
- Dependencies:
  ```bash
  pandas
  numpy
  requests
  plotly
  gradio
  datetime

## Installation & Setup
1.Clone Repository
 git clone https://github.com/PunKunGG/Holographic-Data-Globe-Earthquake-Wildfire.git
 cd Holographic-Data-Globe-Earthquake-Wildfire/[Script]\ Code_FinalProj

2.Install Dependencies
 pip install -r requirements.txt
(หากไม่มีไฟล์ requirements.txt ให้ใช้ pip install pandas numpy requests plotly gradio)

3.Run the Application
 python cell_7_GUI.py

4.เปิดใช้งานผ่าน Browser
โปรแกรมจะเปิดอินเทอร์เฟซ Gradio ที่ [http://localhost:7860/](https://e71dad4accb66ff9b8.gradio.live/)

## API Reference
- USGS Earthquake API
- NASA EONET API

## Note
- หาก API มีข้อจำกัดด้านจำนวนการดึงข้อมูล (Rate Limit) ให้ตั้ง limit ใน cell_3_API&CSVappend.py ให้เหมาะสม
- ค่าพื้นที่ (REGIONS) สามารถเพิ่มได้ใน cell_2.py

## Dependencies
- pandas
- numpy
- requests
- plotly.graph_objects
- gradio
- datetime

# 🧩 Contributors
- ศิวภาส ภูศรีอ่อน	  เขียนโค้ดหลัก, สร้าง GUI, เขียนระบบ Animation และ Export
- ภควรรธ บุญเรือง  ทดสอบ API และตรวจสอบข้อมูล, จัดการโครงสร้าง CSV
- รัชภูมิ ทองแดง   จัดทำรายงาน, สร้าง README และเตรียมสไลด์นำเสนอ
