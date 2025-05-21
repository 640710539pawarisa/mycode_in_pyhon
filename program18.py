#หาผลรวมของตัวเลขไม่จํากัดจำนวน
total = 0

while True: #คือรับมาเรื่อยๆ หรือ ทำซ้ำไม่สิ้นสุด
    number = int(input("ป้อนตัวเลข: "))
    if number<=0: #เช็คว่าเป็น0หรือ ติดลบหรือไม่
        break #ถ้าเป็น0หรือติดลบให้หยุด
    total += number #คือ total = total + number , total คือ ผลรวม ของตัวเลขทั้งหมด, number คือ ตัวเลขที่เราป้อน,
    #total + number คือ เอาค่าที่เก็บไว้ในตัวแปร total มาบวกกับ number
print("ผลรวม = ",total) 
print("จบการทำงาน")