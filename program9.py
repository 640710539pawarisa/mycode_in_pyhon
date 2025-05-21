#ตัวดำเนินการทางตรรกศาสตร์
# -*- coding: utf-8 -*-

# #คำสั่งเปลี่ยนเป็นภาษาไทย
# import sys
# import io 

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# print("เปลี่ยนเป็นภาษาไทย")

username =input("ป้อนชื่อผู้ใช้: ")
password =input("ป้อนรหัสผ่าน: ")

#เช็คชื่อผู้ใช้และรหัสผ่าน กรณีของ AND
if username == "admin" and password == "1234":
    print("เข้าสู่ระบบสําเร็จ")
else:
    print("ข้อมูลไม่ถูกต้อง")
    
#เช็คชื่อผู้ใช้และรหัสผ่าน กรณีของ OR
if username == "admin" or password == "1234":
    print("เข้าสู่ระบบสําเร็จ")
else:
    print("ข้อมูลไม่ถูกต้อง")
    
#เช็คชื่อผู้ใช้และรหัสผ่าน กรณีของ NOT
if not username == "admin" :
    print("เข้าสู่ระบบสําเร็จ")
else:
    print("ข้อมูลไม่ถูกต้อง")
    
#     #วิธี run คือ python program9.py
# #หรือ กด วิธีที่ 1: ใช้ Terminal แทนการกด Run ปกติ
# เปิดไฟล์ .py

# กดขวาบนไฟล์ แล้วเลือก
# ✅ "Run Python File in Terminal" (อย่ากดปุ่ม ▶ ด้านบน)