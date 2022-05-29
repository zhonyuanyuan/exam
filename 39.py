a = int(input(""))
b = int(a / 2)
c = a - b
print(b)
print(c)
if a % 2 == 1:
    for i in range(0,int(c)+1,1):
        for k in range(int(c)-i):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
        for l in range(i-1):
            print("*",end="")
        print()
    for i in range(0,int(b),1):
        for k in range(i+1):
            print(" ",end="")
        for j in range(int(b)-i):
            print("*",end="")
        for l in range(int(b)-i-1):
            print("*",end="") 
        print()
else:
    for i in range(0,int(c)+1,1):
        for k in range(int(c)-i):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
        for l in range(i-1):
            print("*",end="")
        print()
    for i in range(0,int(b),1):
        for k in range(i):
            print(" ",end="")
        for j in range(int(b)-i):
            print("*",end="")
        for l in range(int(b)-i-1):
            print("*",end="") 
        print()