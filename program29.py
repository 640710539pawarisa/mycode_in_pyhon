#dictionary ตัวดำเนินการเอกลักษณ์ ,identity operator

colorA=["red","green","blue"]
colorB=["red","green","blue"]
#เปรียบเทียบข้อมูล ว่าเหมือนกันหรือไม่
#ค่าที่ได้จะมีแค่ True หรือ False 

print(colorA==colorB)
#หรือ
print(colorA is colorB)
#ตอบไม่เหมือน เพราะเก็บคนละตัวแปร

#สร้าง dictionary มาใหม่
data = colorA

print(data is colorA)
#ตอบเหมือนdกัน เพราะเก็บตัวแปร หรือมันชี้ไปที่เดียวกัน

#เช็คว่าไม่เหมือนกันหรื่อไม่
print(data is not colorA)
print(data is not colorB)
print(colorA is not colorB)
#หรือ
print(colorA != colorB)

