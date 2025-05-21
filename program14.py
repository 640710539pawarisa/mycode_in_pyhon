#for loop
#แบบอยากทำซำ 5 รอบ
for counter in range(3):
    print("Hello World")
    
print("จบการทำงาน")
#อยากปริ้นจำนวนรอบ
for counter in range(3):
    print(counter)
    
print("จบการทำงาน")
#อยากเปลี่ยนจาก 0-2 เป็น 1-3 สรุปเปลี่ยนค่าเริ่มต้น
for counter in range(1,4): #range(start,stop)
    print(counter)
    
print("จบการทำงาน")

#แบบเพิ่ม step เช่น เริมที่ 1 จนถึง  6 เพิ่มขึ้นที่ 2
for counter in range(1,6,2): #range(start,stop,step)
    print(counter)
    
print("จบการทำงาน")

#แบบลดค่าทีละ1 คือ 6 ถึง 1
for counter in range(6,1,-1): #range(start,stop,step)
    print(counter)
    
print("จบการทำงาน")