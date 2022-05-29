a = input("輸入五張牌").split(" ")
b = 0
for i in range(len(a)):
    if a[i] == "A":
        b += 1
    elif a[i] == '2':
        b += 2
    elif a[i] == '3':
        b += 3
    elif a[i] == '4':
        b += 4
    elif a[i] == '5':
        b += 5
    elif a[i] == '6':
        b += 6
    elif a[i] == '7':
        b += 7
    elif a[i] == '8':
        b += 8
    elif a[i] == '9':
        b += 9
    elif a[i] == '10':
        b += 10
    elif a[i] == 'J':
        b += 11
    elif a[i] == 'Q':
        b += 12
    elif a[i] == 'K':
        b += 13
print(b)