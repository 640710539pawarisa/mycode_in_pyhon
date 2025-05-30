#ขอบเขตตัวแปร

#สมมติเราอยากทเขียนโปรแกรมที่เกี่ยวกับธนาคาร 
# เช่น ต้องการที่จะฝากเงินและถอนเงินที่ธนาคาร มันจะมีการคำนวณยอดเงินคงเหลือในบัญชี

#เป็นการประยุกต์ใช้ความรู้เรื่อง global variable และ local variable

#variable scope : มีจัดการเงินในบัญชีธนาคาร จะมีการกำหนด เช่น ยอดเงินในบัญชีมีกี่บาท 
# หรือถ้าต้องการฝากเงิน,ถอนเงิน เข้าบัญชีต้องทำอย่างไร เลยจะมีการกำหนดเงื่อนไขการทำงานภายในตัวบัญชีธนาคาร
#โดยการกําหนดการทำงานผ่าน function ,การแสดงยอดเงินคงเหลือในบัญชีธนาคารจะให้ฟังก์ชั่น display_balance() มารับหน้าที่
#display_balance() จะแสดงยอดเงินคงเหลือในบัญชีธนาคาร ,deposit() จะทําการฝากเงินเข้าบัญชีธนาคาร ,withdraw() จะทําการถอนเงินจากบัญชีธนาคาร

balance=0 #ตัวแปรแบบ สามารถใช้ได้ทุกๆที่ในโปรแกรม หรือตัวแปรสาธารณะ global variable
def display_balance():
    print("ยอดเงินคงเหลือในบัญชีธนาคารของคุณ: ",balance ,"บาท")
    
def deposit(value): #value คือตัวแปรที่รับค่าจากการฝากเงิน
    #ดึงตัวแปร balance มาใช้ หรือคือตัวแปรที่เก็บยอดเงินคงเหลือ
    global balance
    money =value #money คือตัวแปรที่ใช้เก็บค่าในการฝากเงิน เป็นแบบlocal variable
    balance = balance + money #balance คือตัวแปรที่ใช้เก็บค่าในการฝากเงิน เป็นแบบglobal variable หรือ balance คือตัวแปรที่ใช้เก็บยอดเงินคงเหลือในบัญชีธนาคาร
    print("ฝากเงินจำนวน ",money,"บาท ")
    
def withdraw(value): #value คือตัวแปรที่รับค่าจากการถอนเงิน
    global balance
    amount = value #amount คือตัวแปรที่ใช้เก็บค่าในการถอนเงิน เป็นแบบlocal variable
    balance = balance - amount #balance คือตัวแปรที่ใช้เก็บค่าในการถอนเงิน เป็นแบบglobal variable
    print("ถอนเงินจำนวน ",amount,"บาท ")

#เรียกใช้ฟังก์ชั่น
display_balance()
deposit(1000) #ฝากเงิน เข้าไปในบัญชี จะใช้ฟังก์ชั่น deposit จำนวน 1000 บาท ,value คือเลขที่ใสเข้าไป
display_balance() #แสดงยอดเงินคงเหลือในบัญชี
withdraw(500)#ถอนเงิน จะใช้ฟังก์ชั่น withdraw จำนวน 500 บาท
display_balance()#แสดงยอดเงินคงเหลือในบัญชี