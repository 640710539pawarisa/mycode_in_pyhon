#คำสั่งเงื่อนไข
# -*- coding: utf-8 -*-

# #คำสั่งเปลี่ยนเป็นภาษาไทย
# import sys
# import io 

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# print("เปลี่ยนเป็นภาษาไทย")

#input
score = int(input("กรุณาป้อนคะแนนสอบของคุณ: "))#รับข้อมูลผ่านคีย์บอร์ด

print("คะแนนสอบของคุณ = ",score)

#process
if score<0:
    print("คะแนนไม่ถูกต้อง")
elif score>=50:
    print("คุณได้เกรด A")
else:
    print("คุณได้เกรด F")


#     #วิธี run คือ python program9.py
# #หรือ กด วิธีที่ 1: ใช้ Terminal แทนการกด Run ปกติ
# เปิดไฟล์ .py

# กดขวาบนไฟล์ แล้วเลือก
# ✅ "Run Python File in Terminal" (อย่ากดปุ่ม ▶ ด้านบน)