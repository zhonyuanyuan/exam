a = int(input("請輸入一個正整數(<10):"))
for i in range(a):
    b = 0
    for j in range(i+1):
        if b == 0:
            print('%2d' % (i+1),end=" ")
            c = i+1
            b += 1
        else:
            print('%2d' % (c*(j+1)),end=" ")
            
    print()
