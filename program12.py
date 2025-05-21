#Macth Statement

sevice = input("กรุณาป้อนหมายเลขบริการ(1-3): ")

match sevice: #เอาตัวแปรseviceเป็นมาเช็คเงื่อนไข
    case "1": print("ฝากเงิน")
    case "2": print("ถอนเงิน")
    case "3": print("ยอดเงินคงเหลือ")
    case _: print("หมายเลขบริการไม่ถูกต้อง")
    #case "":print("หมายเลขบริการไม่ถูกต้อง") #วิธีเชียนค่าว่างอีกแบบ

        

