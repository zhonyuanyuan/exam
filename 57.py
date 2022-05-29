a = input("請選擇主餐及升級的套餐:")
b = input("是否升級成大杯飲料:")
c = input("是否換成大薯:")
d = 0
if a.count("A") == 1:
    if a.count("1") == 1:
        d += 127
    elif a.count("2") == 1:
        d += 117
    elif a.count("3") == 1:
        d += 137
    elif a.count("4") == 1:
        d += 99
    elif a.count("5") == 1:
        d += 115
else:
    if a.count("1") == 1:
        d += 140
    elif a.count("2") == 1:
        d += 130
    elif a.count("3") == 1:
        d += 150
    elif a.count("4") == 1:
        d += 112
    elif a.count("5") == 1:
        d += 128
if b == "是":
    d += 7
if c == "是":
    d += 13
print("總共為",d,"元")