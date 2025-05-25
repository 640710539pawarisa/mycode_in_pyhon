#Module
#โปรแกรมหลัก  เอาไว้run โปรแกรมอย่างเดียว
#ถัดมา เราสร้าง โปรแกรมย่อยหรือ โมดูล
#โมดูลสามารถเรียกใช้ได้ โปรแกรมหลัก สามารถเรียกใช้ได้ 
#โดยการสร้างไฟล์ .py ชื่อไฟล์ว่า database.py และ calculator.py

#เพิ่ม อันนี้ เป็นเรื่องการนำ module ที่เราสร้างมาใช้งาน ******8
# #--------------------------------------------------------------------------------------
# #เรียกใช้งาน Module (import)แบบที่ 1
# import calculator as mycal #แบบเรียกทุกคำสั่งในไฟล์ database.py ,as mycal เป็นการตั้งชื่อเล่นให้มันเรียกใช้งานได้แบบสั้นๆ
# import database as db


# #การเรียกใช้งาน 
# #ชื่อmodule.ชื่อคําสั่ง
# print(mycal.add(10,20))#การบวก
# print(mycal.subtract(10,20))#การลบ
# print(mycal.multiply(10,20))#การคูณ
# print(mycal.divide(10,20))#การหาร
# print(mycal.power(2,3))#การยกกําลัง

# print(db.name)#การดึงข้อมูล ,db.ชื่อคําสั่ง , name เป็นชื่อตัวแปร ที่อยู่ในไฟล์ database ต้องเอา parameter มาด้วย ไม่งั้น error
# db.insert()#การบันทึก
# db.delete()#การลบ
# db.update()#การอัปเดต

#-------------------------------------------------------------------------------------

##การเรียกใช้งาน Module (from ..... import)แบบที่ 2  < ให้เราเลือกแบบใดแบบหนึ่ง แล้วเรียกใช้งาน>

# from calculator import multiply,add as plus,subtract,power #ตั้งชื่อเล่นให้มันเรียกใช้งานได้แบบสั้นๆ
#
# 
# # ถ้าอยากหยิบมาทุกตัวละ ใช้ * เช่น from calculator import *

# print(multiply(10,20))#การคูณ
# print(plus(10,20))#การบวก
# print(subtract(10,20))#การลบ
# print(power(2,3))#การยกกําลัง

#กรณีใช้คำสั่ง  from calculator import *
from calculator import *
from database import *
#ถ้าอยากเอาฟังก์ชั่น insert มาอย่างเดียว ใช้คําสั่ง from database import insert

print(add(10,20))#การบวก
print(subtract(10,20))#การลบ
print(multiply(10,20))#การคูณ
print(divide(10,20))#การหาร
print(power(2,3))#การยกกําลัง

print(name) #เข้าถึงข้อมูลได้โดยตรงเลย
insert()
delete()
update()


