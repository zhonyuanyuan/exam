a = list(input())
z = 1
while z != 0 :
    t = 0
    f = 0
    b = input()
    if b == "0000":
        break
    v = list(b)
    for i in range(len(a)):
        if a[i] == v[i]:
            t += 1
        for j in range(len(a)):
            if v[j] == a[i]:
                f += 1
    print(t,"A",f-t,"B")