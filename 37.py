a = int(input("整數n:"))
print("數列:",end=" ")
while a != 1:
    print(int(a),end=" ")
    if int(a) % 2 == 0 :
        a /= 2
    else:
        a = a * 3 + 1
print("1")