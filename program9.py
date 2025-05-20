#ตัวดำเนินการทางตรรกศาสตร์
# -*- coding: utf-8 -*-


username =input("ป้อนชื่อผู้ใช้: ")
password =input("ป้อนรหัสผ่าน: ")

#เช็คชื่อผู้ใช้และรหัสผ่าน กรณีของ AND
if username == "admin" and password == "1234":
    print("เข้าสู่ระบบสําเร็จ")
else:
    print("ข้อมูลไม่ถูกต้อง")
    
#เช็คชื่อผู้ใช้และรหัสผ่าน กรณีของ OR
if username == "admin" or password == "1234":
    print("เข้าสู่ระบบสําเร็จ")
else:
    print("ข้อมูลไม่ถูกต้อง")
    
#เช็คชื่อผู้ใช้และรหัสผ่าน กรณีของ NOT
if not username == "admin" :
    print("เข้าสู่ระบบสําเร็จ")
else:
    print("ข้อมูลไม่ถูกต้อง")