#return keyword หรือ เพื่อกระโดดออกจาก function ที่เราสร้าง

#*****
#ปํญหาของเราคือถ้ากรอกฝากเงินเข้าไป -500ละ ผลลัพธ์จะเป็น -500บาท แต่ความจริงไม่สามารถทำได้
#และในกรณีฝากงิน 0บาท มันก็ขึ้น 0 บาทและความจริงไม่สมารถทำได้เช่นกัน
#*****
#ปัญหาในกรณีถอนเงิน เช่นเรามีเงินบัญชี1000แล้วเราถอน 0บาท ผลลัพธ์จะเป็น 1000บาท แต่ความจริงไม่สามารถทำได้ จะไปถอนทำไม!
#ปัญหาถัดมากรณีถอนเงินเข้าไปมากกว่าเงินที่มีในบัญชี เช่น มีเงินบัญชี1000 แล้วถอน 1500บาท ผลลัพธ์จะเป็น -500บาท
# แต่ความจริงไม่สามารถทำได้ เราอยากให้ระบบแจ้งว่า ยอดเงินในบัญชีไม่เพียงพอ

#**************

balance=0 #ตัวแปรแบบ สามารถใช้ได้ทุกๆที่ในโปรแกรม หรือตัวแปรสาธารณะ global variable
def display_balance():
    print("ยอดเงินคงเหลือในบัญชีธนาคารของคุณ: ",balance ,"บาท")
    
def deposit(value): #value คือตัวแปรที่รับค่าจากการฝากเงิน
    #ดึงตัวแปร balance มาใช้ หรือคือตัวแปรที่เก็บยอดเงินคงเหลือ
    global balance
    money =value #money คือตัวแปรที่ใช้เก็บค่าในการฝากเงิน เป็นแบบlocal variable   
    print("ฝากเงินจำนวน ",money,"บาท ")

    if (money <= 0):#ถ้าmoney น้อยกว่า 0
        print("ไม่สามารถฝากเงินได้ กรุณาฝากเงินมากกว่า 0บาท")
        return #เป็นกeyword ที่ใช้ในการหยุดการทํางานให้มัน กระโดออกจากfunction นี้
    balance = balance + money #balance คือตัวแปรที่ใช้เก็บค่าในการฝากเงิน เป็นแบบglobal variable หรือ balance คือตัวแปรที่ใช้เก็บยอดเงินคงเหลือในบัญชีธนาคาร

def withdraw(value): #value คือตัวแปรที่รับค่าจากการถอนเงิน
    global balance  
    amount = value #amount คือตัวแปรที่ใช้เก็บค่าในการถอนเงิน เป็นแบบlocal variable    
    print("ถอนเงินจำนวน ",amount,"บาท ")

#ใช้ or เพราะถ้าvalue น้อยกว่า 0 และ value มากกว่า balance แสดงว่า ยอดเงินในบัญชีไม่เพียงพอ หรือถ้าเข้าเงื่อนไขใดอันนึง 
# ก็แสดงว่า ยอดเงินในบัญชีไม่เพียงพอ
    if amount <= 0 or amount  > balance: #ถ้าvalue น้อยกว่า 0 หรือ value มากกว่า balance แสดงว่า ยอดเงินในบัญชีไม่เพียงพอ 
        print("ไม่สามารถถอนเงินได้ ยอดเงินในบัญชีไม่เพียงพอ")
        return
    balance = balance - amount #balance คือตัวแปรที่ใช้เก็บค่าในการถอนเงิน เป็นแบบglobal variable

#เรียกใช้ฟังก์ชั่น
display_balance()
deposit(1000) #ฝากเงิน เข้าไปในบัญชี จะใช้ฟังก์ชั่น deposit จำนวน 1000 บาท ,value คือเลขที่ใสเข้าไป
display_balance() #แสดงยอดเงินคงเหลือในบัญชี
withdraw(500)#ถอนเงิน จะใช้ฟังก์ชั่น withdraw จำนวน 500 บาท
display_balance()#แสดงยอดเงินคงเหลือในบัญชี
#กรณีเพิ่มเติม
deposit(-1000)
display_balance()
withdraw(5000)
display_balance()
