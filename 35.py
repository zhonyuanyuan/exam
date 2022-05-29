a = input("sA:")
b = input("sB:").split(" ")
c = 0
for  i in range(len(b)):
    if b[i] == a :
        print("子字串判斷為:YES")
        c += 1
        break
if c == 0 :
    print("子字串判斷為:NO")