a = int(input("輸入一組四位數字為:"))
b = int(a / 1000)
c = int(a % 1000 / 100)
d = int(a %1000 %100 /10)
e = int(a %1000 %100 %10)
b = (b + 7)%10
c = (c + 7)%10
d = (d + 7)%10
e = (e + 7)%10
f = str(d)+str(e)+str(b)+str(c)
print("輸出加密後的數字為:",f) 