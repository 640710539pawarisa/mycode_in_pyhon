#ternary operator
#เขียนเงื่อนไขภายใน1บรรทัดทำงานได้เลย
# -*- coding: utf-8 -*-

# #คำสั่งเปลี่ยนเป็นภาษาไทย
# import sys
# import io 

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# print("เปลี่ยนเป็นภาษาไทย")

#ยกตัวอย่างเขียนแยกตัวเลขคู่หรือเลขคี่
number = int(input("กรุณาป้อนตัวเลขของคุณ:"))#รับตัวเลขผ่านkeybord
print("เลขของคุณ คือ ",number)

#เขียนแบบเงื่อนไขธรรมดา
if number%2==0:
    print("เลขคู่")
else:
    print("เลขคี่")

print("-------------")

#เขียนแบบลดรูป
print("เลขคู่") if number%2==0 else print("เลขคี่")


#     #วิธี run คือ python program9.py
# #หรือ กด วิธีที่ 1: ใช้ Terminal แทนการกด Run ปกติ
# เปิดไฟล์ .py

# กดขวาบนไฟล์ แล้วเลือก
# ✅ "Run Python File in Terminal" (อย่ากดปุ่ม ▶ ด้านบน)