a = int(input("輸入第一行正整數為:"))
b = input("第二行中數列中的數字為:").split(" ")
c = 0
d = 0
e = 0
for i in range(a):
    if b.count(b[i]) == 1:
        c += 1
    else:
        if b.count(b[i]) > d :
            d = b.count(b[i])
            e = b[i]
if c == a :
    print("每個數字剛好只出現一次")
else:
    print("最大出現的數字為:",e)
    print("出現次數為:",d)
    

