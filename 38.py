a = input("")
c = 0
b = []
for i in range(int(a)):
    b.append(int(input()))
for i in range(int(a)):
    if b[i] % 9 == 0 or b[i] % 11 == 0 :
        c += 1
        print("第",i+1,"個點 ",b[i])
if c == 0 :
    print("0")