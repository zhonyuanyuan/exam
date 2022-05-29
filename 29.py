a = list(input("甲方的數字:"))
b = list(input("乙方的數字:"))
print("洗刷刷結果:  ",end="")
for i in range(len(a)):
    if a[i] == "1":
        if b[i] == "5":
            print("贏",end="")
        elif b[i] == "2":
            print("輸",end="")
        else:
            print("和",end="")
    if a[i] == "2":
        if b[i] == "1":
            print("贏",end="")
        elif b[i] == "3":
            print("輸",end="")
        else:
            print("和",end="")
    if a[i] == "3":
        if b[i] == "2":
            print("贏",end="")
        elif b[i] == "4":
            print("輸",end="")
        else:
            print("和",end="")
    if a[i] == "4":
        if b[i] == "3":
            print("贏",end="")
        elif b[i] == "5":
            print("輸",end="")
        else:
            print("和",end="")
    if a[i] == "5":
        if b[i] == "4":
            print("贏",end="")
        elif b[i] == "1":
            print("輸",end="")
        else:
            print("和",end="")