a = int(input("請輸入階乘值M:"))
n = 1
tatle = 1
while tatle < a:
    tatle = tatle * n
    n += 1

print("超過M為",a,"的最小階層N值為:",n-1)