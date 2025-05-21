#แม่สูตรคูณแบบกำหนดช่วง

start=int(input("แม่สูตรคูณเริ่มต้น : "))
end=int(input("แม่สูตรคูณสุดท้าย : "))

for number in range(int(start),int(end)+1): #range(start,stop) คือ 1-12 ,end+1 คือ 1-11+1= 1- 12
    print("สูตรคูณแม่ ",number)#number คือ แม่สูตรคูณ
    print("-------------")
    for i in range(1,13): #range(start,stop) คือ 1-12 ,คือการแสดงแม่สูตรคูณ
        print(number,"x",i,"=",number*i)
    print("-------------")
        