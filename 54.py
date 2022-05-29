a = float(input("請輸入路程公里數(KM):"))
b = 75
if a <= 1.5 :
    print("所需車資為:",b)
else:
    a -= 1.5
    if a < 0.25 :
        print("所需車資為:",b+5)
    else:
        c = int(a /0.25)
        if a % 0.25 > 0 :
            d = 5
            b = b + c * 5 + d 
        else:
            b = b + c * 5 
        print("所需車資為:",b)