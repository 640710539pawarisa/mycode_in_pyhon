#tuple

#สร้างtuple แบบ สัญลักษณ์
product=("กางเกง",150,10,True)
#แสดงผล
print(product,"แสดงผลtuple product")
#เข้าถึงเฉพาะข้อมูลที่สนใจ เช่น
#ทำแบบซ้ายไปขวา
print(product[0],"แสดงผลข้อมูลตัวแรก")
print(product[1],"แสดงผลข้อมูลตัวที่ 2")
print(product[2],"แสดงผลข้อมูลตัวที่ 3")
print(product[3],"แสดงผลข้อมูลตัวที่ 4")
print("-------------------------------------------------------------------")
#ทำแบบขวาไปซ้าย
print(product[-1],"แสดงผลข้อมูลตัวสุดท้าย")
print(product[-2],"แสดงผลข้อมูลตัวที่ 2")
print(product[-3],"แสดงผลข้อมูลตัวที่ 3")
print(product[-4],"แสดงผลข้อมูลตัวที่ 4")
print("-------------------------------------------------------------------")
# #เปลี่ยนข้อมูลจากกางเกงเป็นเสื้อ
# product[0]="เสื้อ"
# print(product,"แทรกแก้ไขข้อมูล") #แก้ไขข้อมูลในtupleไม่ได้ ระบบจะแจ้ง error ต้องใช้ list

#อยากตรวจสอบชนิดข้อมูล
print(type(product),"ทดสอบเช็คชนิดข้อมูล")
print("-------------------------------------------------------------------")
#อยากตรวจสอบจํานวนข้อมูล
print(len(product),"ทดสอบเช็คจํานวนข้อมูล")
print("-------------------------------------------------------------------")
#การแจกแจงข้อมูลใน tuple product โดยเก็บไว้ในตัวแปรโดยเฉพาะ
#ประกาศตัวแปรตามจํานวนข้อมูลที่มาเรามี
name,price,stock,status=product
print(name)
print(price)
print(stock)
print(status)
print("-------------------------------------------------------------------")

#หรืออยากหยิบทุกตัวมาใช้มาทีตัว ให้เราใช้loop
for item in product:
    print(item)

print("-------------------------------------------------------------------")

#ถ้าเราเชื่อมข้อมูลกลุ่ม tupleเข้าด้วยกัน

color1=("แดง","เหลือง","เขียว")#เขียนแบบ1
color2=tuple(("ขาว","ฟ้า","ส้ม"))#เขียนแบบ2
fullcolors=color1+color2
print(fullcolors,"รวมlist ในตัวแปรชื่อ fullcolors")
print("-------------------------------------------------------------------")

#ตรวจสอบชนิดข้อมูล
print(type(fullcolors),"ทดสอบเช็คชนิดข้อมูล")
print("-------------------------------------------------------------------")

#ตรวจสอบจํานวนข้อมูลทั้งหมด
print(len(fullcolors),"ทดสอบเช็คจํานวนสมาชิกทั้งหมด")
print("-------------------------------------------------------------------")

#การทำซ้ำในสมาชิก
print(fullcolors*2,"ทดสอบการทำซ้ำในสมาชิก")
print("-------------------------------------------------------------------")

#ทำซ้ำ3รอบ
print(fullcolors*3,"ทดสอบการทำซ้ำในสมาชิก")
print("-------------------------------------------------------------------")

#การเข้าถึงสมาชิกtupleแบบช่วง ,เหมือนlistเลย

color3=("แดง","เหลือง","เขียว","ดํา","ขาว","ฟ้า","ส้ม")
#จากข้างหน้าไปข้างหลัง
print(color3[2:],"(เขียว)")#อยากได้สีเขียว
#จากข้างหลังไปข้างหน้า
print(color3[-3:],"(ขาว)")#อยากได้สีขาว
#ทำจากตำแน่งไปสุดท้าย
print(color3[:],"(ทั้งหมด)")
#ทำจากตำแน่งไปสุดท้าย
print(color3[-6:],"(ทั้งหมด)")

print("-------------------------------------------------------------------")
#การเข้าถึงข้อมูลโดยกำหนดช่วงจุดเริ่มต้นและสุดท้าย
#แบบจากข้างหน้าไปข้างหลัง , index แบบค่าบวก

#อยากได้สี เขียวกับดำ
print(color3[2:4],"(เขียวกับดำ)")
#อยากได้สี เขียวกับดำและฟ้า
print(color3[2:5],"(เขียวกับดำและฟ้า)")
#อยากได้สี เขียวกับดำและฟ้าและขาว
print(color3[2:6],"(เขียวกับดำและฟ้าและขาว)")

print("-------------------------------------------------------------------")
#แบบจากหลังไปหน้า , index แบบค่าลบ
#อยากได้สี ฟ้ากับขาว
print(color3[-3:-1])
#อยากได้สี ดำกับขาวและฟ้า
print(color3[-3:-2])
#อยากได้สี ดำกับขาวและฟ้าและส้ม
print(color3[-3:])

print("-------------------------------------------------------------------")

#การใช้ฟังก์ชั่นจัดการสมาชิกในtuple มี2ตัวคือ ฟังกืชั่นสำหรับค้นหาข้อมูล และ ฟังก์ชั่นนับข้อมูลซ้ํา

#การค้นหาข้อมูลในtuple
color4=("แดง","เหลือง","เขียว","ดํา","ขาว","ฟ้า","ส้ม","ส้ม")
print(color4)
#ฟังก์ชั่นสำหรับค้นหาข้อมูล
print(color4.index("ดํา"))#ถ้ามีสีดำมันจะบอกตำแหน่งของindex
print(color4.count("เทา")) 
print("-------------------------------------------------------------------")    
#ฟังก์ชั่นนับข้อมูลซ้ํา
print(color4.count("เขียว"))
print(color4.count("ส้ม"))
print("-------------------------------------------------------------------")


