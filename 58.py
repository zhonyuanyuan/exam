b = []
c = []
d = []
for i in range(10):
    print("請輸入第",i+1,"個數字:",end="")
    a = int(input())
    b.append(a)
d = sorted(b,reverse=True)
print("最大的3個數字為:",end="")
for i in range(3):
    if i == 2 :
        print(d[i],end="")
    else:
        print(d[i],end=",")
print()
c = sorted(b)
print("最小的3個數字為:",end="")
for i in range(3):
    if i == 2 :
        print(c[2-i])
    else:
        print(c[2-i],end=",")