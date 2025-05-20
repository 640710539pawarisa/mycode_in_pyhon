#คำสั่งเงื่อนไข
# -*- coding: utf-8 -*-


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
