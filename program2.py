#การสร้างตัวแปร และ ชนิดของข้อมูล
#-*- coding: utf-8 -*-
#เก็บข้อมูลนักเรียน(input)

# #คำสั่งเปลี่ยนเป็นภาษาไทย
# import sys
# import io 

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# print("เปลี่ยนเป็นภาษาไทย")

#เขียนแบบธรรมดา
#name="เอ๊ะ"
#age=22
#grade = 2.5 #เว้นวรรคทีละ1
#status = True #trueคือกำลังศึกษาอยู่,falseคือเรียนจบแล้ว

#สร้างตัวแปรหลายตัวแปรในบรรทัดเดียว
name,age,grade,status = "เอ๊ะ",22,2.5,True

#แก้ไขข้อมูล
age=23
grade=3.10

#แสดงข้อมูล (output)
print("ชื่อนักเรียน = ",name)
print("อายุ = ",age," ปี")
print("เกรด = ",grade)
print("สถานะ = ",status)

#แสดงชนิดข้อมูล
print(type(name),"ชนิดของชื่อ")
print(type(age),"ชนิดชองอายุ")
print(type(grade),"ชนิดของเกรด")
print(type(status),"ชนิดของสถานะ")
#หรืออยากตรวจสอบข้อมูลว่าเป็นชนิดอะไรก็โยนข้อมูลเข้าไปเลย ,ไม่จำเป็นว่าต้องเก็บลงตัวแปรอย่างเดียว
print(type(3.10),"ทดสอบเช็คชนิดของเกรด")


#     #วิธี run คือ python program9.py
# #หรือ กด วิธีที่ 1: ใช้ Terminal แทนการกด Run ปกติ
# เปิดไฟล์ .py

# กดขวาบนไฟล์ แล้วเลือก
# ✅ "Run Python File in Terminal" (อย่ากดปุ่ม ▶ ด้านบน)