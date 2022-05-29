a = int(input(""))
if a >= 100:
    b = int(a / 100)
    c = a % 100
    d = int(c / 50)
    e = c % 50
    f = int(e / 10)
    g = e % 10
    h = int(g / 5)
    i = g % 5
    print(b+d+f+h+i)
elif a >= 50 and a < 100:
    d = int(a / 50)
    e = a % 50
    f = int(e / 10)
    g = e % 10
    h = int(g / 5)
    i = g % 5
    print(d+f+h+i)
elif a >= 10 and a < 50:
    f = int(a / 10)
    g = a % 10
    h = int(g / 5)
    i = g % 5
    print(f+h+i)
elif a >= 5 and a < 10:
    h = int(a / 5)
    i = a % 5
    print(h+i)
else:
    i = a % 5
    print(i)