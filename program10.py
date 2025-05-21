#โปรแกรมตัดเกรดอย่างง่าย

score = int(input("กรุณาป้อนคะแนนสอบของคุณ: "))#รับข้อมูลผ่านคีย์บอร์ด

print("คะแนนสอบของคุณ = ",score)

grade = None #ตัวแปรเก็บเกรด
#process
if score >=80 and score <=100: #80-100
    grade = "A"
elif score >=70 and score <=79:#70-79
    grade = "B"
elif score >=0 and score <=69:#0-69
    grade = "F"
else :#score<0
    grade = "N (invalid)"

#output
print("เกรดของคุณคือ = ",grade)