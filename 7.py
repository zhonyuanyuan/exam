a = input("輸入月租費形式及通話時間為:").split(",")
p = 0
if int(a[0]) == 186:
    if int(a[1])*0.09 < 186:
        p = round(int(a[1])*0.09 *0.9)
        print("通話費為:",p)
    elif int(a[1])*0.09 > 186:
        p = round(int(a[1])*0.09 *0.8)
        print("通話費為:",p)
elif int(a[0]) == 386:
    if int(a[1])*0.08 < 386:
        p = round(int(a[1])*0.08 *0.8)
        print("通話費為:",p)
    elif int(a[1])*0.08 > 386:
        p = round(int(a[1])*0.08 *0.7)
        print("通話費為:",p)
elif int(a[0]) == 586:
    if int(a[1])*0.07 < 586:
        p = round(int(a[1])*0.07 *0.7)
        print("通話費為:",p)
    elif int(a[1])*0.07 > 586:
        p = round(int(a[1])*0.07 *0.6)
        print("通話費為:",p)
elif int(a[0]) == 986:
    if int(a[1])*0.06 < 986:
        p = round(int(a[1])*0.06 *0.6)
        print("通話費為:",p)
    elif int(a[1])*0.06 > 986:
        p = round(int(a[1])*0.06 *0.5)
        print("通話費為:",p)