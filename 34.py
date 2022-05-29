a = input("輸入一正整數(11~1000):")
if int(a)%2 == 0 and int(a)%11 == 0:
    if int(a)%5 != 0 and int(a)%7 != 0:
        print(a,"為新公倍數?:YES")
    else:
        print(a,"為新公倍數?:NO")
else:
    print(a,"為新公倍數?:NO")