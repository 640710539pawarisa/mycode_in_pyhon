#แม่สูตรคูณ

number = int(input("ป้อนแม่สูตรคูณของคุณ: "))

#2x1 - 2x12 

for i in range(1,13): #range(start,stop) คือ 1-12
    print(number,"x",i,"=",number*i) #number*i คือ แม่สูตรคูณ และ i คือ หมายเลขรอบคูณกับตัวเลขที่เราป้อน