#break / continue

#แบบปกติ
for counter in range(1, 11): #counter เก็บหมายเลขรอบ
    print(counter)
    
print("จบการทำงาน")
#แบบ break 
for counter in range(1, 11): #counter เก็บหมายเลขรอบ
    if counter == 5:
        break
    print(counter)
    
print("จบการทำงาน")

#แบบ continue มันคือการกระโดดข้าม
for counter in range(1, 11): #counter เก็บหมายเลขรอบ
    if counter == 5:
        continue
    print(counter)
    
print("จบการทำงาน")

#วิธีกระโดดข้ามเลขที่เป็นเลขคู่
for counter in range(1, 11): #counter เก็บหมายเลขรอบ
    if counter % 2 == 0:
        continue
    print(counter)
    
print("จบการทำงาน")