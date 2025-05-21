#หาผลรวมของตัวเลข 5 จํานวน
total = 0
for i in range(1,6):
    number = int(input("ลำดับที่ "+str(i)+":")) # str(i)คือ แปลงตัวเลขเป็นข้อความ
    total+=number #คือ total = total + number , total คือ ผลรวม ของตัวเลขทั้งหมด
    print(number)
    
print("ผลรวม = ",total)