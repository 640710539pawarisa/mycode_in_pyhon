#ฟังก์ชั่นจัดการ list
color = ["แดง","เหลือง","เขียว","ดํา","ขาว","ฟ้า","ส้ม"]
print(color)
#การเพิ่มข้อมูลใน list เพิ่มแค่1รายการ
color.append("ม่วง")
print(color)
#การเพิ่มข้อมูลใน list เพิ่มหลายรายการ
color.extend(["ชมพู","น้ําเงิน","เทา"])
print(color)
#ถ้าอยากเพิ่มสีในตำแหน่งที่ต้องการ
color.insert(3,"กรม")
#เราเก็บข้อมุลซ้ำกันได้
color.append("แดง")
print(color)
#นับข้อมูลที่ซ้ำกัน
print(color.count("แดง"))
#การลบข้อมูลใน list
color.remove("แดง")
print(color)
#การเรียงข้อมูลใน list ,เช่นมันจะเรียงตามพยัญชนะ ตามด้วยสระ ถ้าเป็นตัวเลขจะเรียงจากน้อยไปมาก
color.sort()
print(color)
#เราอยากเรียงข้อมูลแบบย้อนกลับ
color.reverse()
print(color)
#ถ้าเราอยากลบทุกตัว
color.clear()
print(color)

#************88
#ลองยกตัวอย่างข้อมูลที่เป้นแบบตัวเลข
number=[10,20,30,40,50,1,8]
#เรีาอยากเรียงข้อมูลจากน้อยไปมาก
number.sort()
print(number)
#เราอยากเรียงข้อมูลย้อนกลับ
number.reverse()
print(number)