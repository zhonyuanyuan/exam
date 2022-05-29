a = int(input("搭了幾次電梯"))
c = 1
cost = 0
for i in range(a):
    b = int(input(""))
    if b > c :
        cost += (b-c)*20
        c = b
    else:
        cost += (c-b)*10
        c = b
print(cost,"元")