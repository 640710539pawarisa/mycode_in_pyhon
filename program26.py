#set
#เก็บข้อมูลของสัตว์ ใส่ใน set
animals={"หมา","แมว","สิงโต","เสือ",True,100}
print(animals)
#set ไม่สามารถเรียงลําดับได้

animals={"หมา","แมว","สิงโต","เสือ",True,100,"หมา","หมู"}
print(animals)
#set ไม่สามารถใส่ข้อมูลซ้ํากันได้ มันแสดงออกหน้าจอมาแค่่อันเดียว

#เช็คชนิดข้อมูล
print(type(animals),"ทดสอบเช็คชนิดข้อมูล")

#จํานวนข้อมูลใน set
print(len(animals),"จํานวนข้อมูลใน set")

#การเข้าถึงข้อมูลทุกตัว ใช้ for loop
for item in animals:
    print(item)
    
#การค้นหาข้อมูลในsetโดยใช้คำสั่ง in
print("สิงโต" in animals)
print("กบ" in animals)

#ต้องการเพิ่มข้อมูลใน set
animals.add("เป็ด")
print(animals,"เพิ่มข้อมูลใน set")

#ต้องการเพิ่มข้อมูลใน set แบบมีลําดับหรือ เพิ่มมากกว่า 1 รายการ
animals.update(("กบ","แฮมเตอร์","จิงโจ้"))
print(animals,"เพิ่มข้อมูลใน set แบบมีลําดับหรือ เพิ่มมากกว่า 1 รายการ")

#ต้องการลบข้อมูลใน set
animals.remove("กบ")
print(animals,"ลบข้อมูลใน set")

#ต้องการลบข้อมูลใน set แบบระบุออกจากset
animals.discard("กบ")
print(animals,"ลบข้อมูลใน set แบบระบุออกจากset")

#สร้างset ใหม่เพิ่ม
pet=set(("ยีราฟ","นก","ไก่","ห่าน","หมา","แมว","สิงโต","เสือ"))
print(pet,"สร้างset ใหม่เพิ่ม")

#แล้วต้องการเอา2เซตมารวมสมาชิกกัน เซตanimals และ pet
data =animals.union(pet) #รวมสมาชิก ด้วยคำสั่ง union
print(data,"รวมสมาชิก")

#แล้วต้องการเอา2เซตมาดูสมาชิกที่เหมือนกัน เซตanimals และ pet
data =animals.intersection(pet) #เอาสมาชิกที่เหมือนกัน ด้วยคำสั่ง intersection
print(data,"เอาสมาชิกที่เหมือนกัน")

#แล้วต้องการเอา2เซตมาดูสมาชิกที่ไม่เหมือนกัน ที่มีแค่ใน เซตanimals เท่านั้น แต่ไม่มีอยู่ใน pet
data =animals.difference(pet) #เอาสมาชิกที่ไม่เหมือนกัน ด้วยคำสั่ง difference
print(data,"เอาสมาชิกที่ไม่เหมือนกัน")

