#สร้าง Function

#การสร้างฟังก์ชัน แบบปกติ
#สมมติว่า เราทำแอปเกี่ยวกับการเล่นเพลง
#การทำงานเช่น เราสามารถเปิดเพลงได้ หยิบเพลงได้ และเลือกเพลงได้ และเล่นเพลงได้ เปิดแอปได้ ปิดแอปได้

#เราจะลองสร้างฟังก์ชันเพื่อทำงานง่ายๆดูก่อนเช่น
def sayhello(): #ชื่อฟังก์ชัน
    print("สวัสดีค่ะ")#กระบวนการทำงาน
    
    
#---------------------------------------------------------------
#สร้างฟังก์ชันเพื่อทำงานการเล่นเพลง
def playmusic(): #ชื่อฟังก์ชัน
    print("เล่นเพลง")
def stopmusic(): #ชื่อฟังก์ชัน
    print("หยุดเพลง")

def openapp(): #ชื่อฟังก์ชัน
    print("เปิดแอป")
def closeapp(): #ชื่อฟังก์ชัน
    print("ปิดแอป")
    
#---------------------------------------------------------------

#สร้างฟังก์ชันแสดงตารางแม่สูตรคูณ
def showtable(): #ชื่อฟังก์ชัน
    print("------------------") #ห้ามปล่อยว่างเด็ดขาด มันจะ error ให้เราใส่ คำสั่ง pass ก้ได้
    for i in range(1,13): #range(start,stop) คือ 1-12
        print("2x",i,"=",2*i) #number*i คือ แม่สูตรคูณ และ i คือ หมายเลขรอบคูณกับตัวเลขที่เราป้อน
    print("------------------")
    

#---------------------------------------------------------------
#การเรียกใช้ฟังก์ชัน ทุกอันที่เราสร้าง
sayhello()  
showtable()
playmusic()
stopmusic()
openapp()
closeapp()
    

    