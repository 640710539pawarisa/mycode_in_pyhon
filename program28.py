#ฟังก์ชั่นจัดการ Dictionary

#สร้าง dictionary
color = {
    "red":"แดง",
    "yellow":"เหลือง",
    "green":"เขียว"
    }
#แสดงผลข้อมูล
print(color)

#สร้าง dictionary ก้อนใหม่
maincolor = color.copy() #ใช้ฟังก์ชั่น copy มาจาก dictionary color
print(maincolor)

#ส่วนของการดึงข้อมูล****************
#ดึงรายชื่อkeyทั้งหมดออกมา
print(color.keys())

#ดึงเฉพาะข้อมูลที่อยู่ในdictionaryเฉพาะvalueออกมา
print(color.values())

#อยากได้ทั้ง key และ value
print(color.items())

#ส่วนของการเข้าถึงข้อมูลkey,valueโดยการใช้ loop***********************
#ใช้ loop ในการดึงข้อมูลทั้งหมดทีละรายการออกมา
for key in color.keys():#ส่วนของ key
    print(key)
for value in color.values():#ส่วนของ value
    print(value)
for key,value in color.items():#ได้ส่วนของ key และ value คือ tupleนั้นเอง
    print(key," = ",value)
    
#ใช้ฟังก์ชั่น get ในการดึงข้อมูลที่ต้องการ
print(color.get("red"))
#หรือ
print(color["red"]) #ใช้แบบนี้ได้เหมือนกัน

#การจัดการข้อมูลใน dictionaryเช่น การลบ และการเพิ่มและอื่นๆ************ 

#แสดงผลข้อมูลที่มี
print(color)
#การลบข้อมูลใน dictionary
color.pop("green")
print(color)
#ต้องการลบทุกตัว
color.clear()
print(color)

#การเพิ่มข้อมูลใน dictionary
color.update({"orange":"ส้ม"})
print(color)

#เพิ่มข้อมูลใน dictionary
color["black"] = "ดํา" #เพิ่มแบบนี้ก็ได้
print(color)

#แก้ไขข้อมูลใน dictionary
color.update({"red":"แดงเข้ม"})#แก้ไขข้อมูลที่มีอยู่แล้ว
print(color)
#หรือใช้แบบนี้ก็ได้
color["black"] = "เทา" #แก้ไขข้อมูลที่มีอยู่แล้ว
print(color)

