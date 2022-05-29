a = input("輸入一整數序列為:").split(" ")
b = len(a)
d = (b/2)
c = 0
for i in range(b):
    if (a.count(a[i]) >= d):
        print("過半元素為:",a[i])
        c += 1
        break
if c == 0:
    print("過半元素為:NO")
    
