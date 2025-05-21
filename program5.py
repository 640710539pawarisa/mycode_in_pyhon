#ตัวดำเนินการกำหนดค่า
# -*- coding: utf-8 -*-

# #คำสั่งเปลี่ยนเป็นภาษาไทย
# import sys
# import io 

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# print("เปลี่ยนเป็นภาษาไทย")

x,y=10,2
print("x = ",x)
print("y = ",y)

x=x+y #10+2 =12จะถูกเก็บลงในตัวแปร x
print("ผลลัพธ์ = ",x)
print("===================")
#เขียนแบบกระชับ
x+=y 
print("ผลลัพธ์+ = ",x)
print("===================")
x-=y
print("ผลลัพธ์- = ",x)
print("===================")
x*=y
print("ผลลัพธ์* = ",x)
print("===================")
x/=y
print("ผลลัพธ์/ = ",x)
print("===================")
x**=y
print("ผลลัพธ์** = ",x)
print("===================")
x%=y
print("ผลลัพธ์% = ",x)
print("===================")


#     #วิธี run คือ python program9.py
# #หรือ กด วิธีที่ 1: ใช้ Terminal แทนการกด Run ปกติ
# เปิดไฟล์ .py

# กดขวาบนไฟล์ แล้วเลือก
# ✅ "Run Python File in Terminal" (อย่ากดปุ่ม ▶ ด้านบน)