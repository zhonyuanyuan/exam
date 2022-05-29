a = input("小明身上有幾元:")
c = 0
d = 0
can = 0
while c != 30:
    if int(a) < 0 or int(a) > 100:
        print("小明金額超出題意")
        break
    b = input("販賣機有幾種飲料:")
    if b == "50":
        break
    if int(a) >= int(b):
        can += 1
    c += 1
if int(a) < 0 or int(a) > 100:
    a = 0
else:
    print(can)