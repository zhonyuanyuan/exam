a = input("測試的資料量")
for i in range(int(a)):
    b = input("輸入血型(大寫)").split(" ")
    if b[0] == "O" and b[1] == "O":
        if b[2] == "O":
            print("YES")
        else:
            print("IMPOSSIBLE")
    if b[0] == "O" and b[1] == "A":
        if b[2] == "O" or b[2] == "A":
            print("YES")
        else:
            print("IMPOSSIBLE")
    if b[0] == "A" and b[1] == "O":
        if b[2] == "O" or b[2] == "A":
            print("YES")
        else:
            print("IMPOSSIBLE")
    if b[0] == "B" and b[1] == "O":
        if b[2] == "O" or b[2] == "B":
            print("YES")
        else:
            print("IMPOSSIBLE")
    if b[0] == "O" and b[1] == "B":
        if b[2] == "O" or b[2] == "B":
            print("YES")
        else:
            print("IMPOSSIBLE")
    if b[0] == "AB" and b[1] == "O":
        if b[2] == "A" or b[2] == "B":
            print("YES")
        else:
            print("IMPOSSIBLE")
    if b[0] == "O" and b[1] == "AB":
        if b[2] == "A" or b[2] == "B":
            print("YES")
        else:
            print("IMPOSSIBLE")
    if b[0] == "A" and b[1] == "A":
        if b[2] == "A" or b[2] == "O":
            print("YES")
        else:
            print("IMPOSSIBLE")
    if b[0] == "A" and b[1] == "B":
        if b[2] == "A" or b[2] == "O" or b[2] == "B" or b[2] == "AB":
            print("YES")
        else:
            print("IMPOSSIBLE")
    if b[0] == "B" and b[1] == "A":
        if b[2] == "A" or b[2] == "O" or b[2] == "B" or b[2] == "AB":
            print("YES")
        else:
            print("IMPOSSIBLE")
    if b[0] == "A" and b[1] == "AB":
        if b[2] == "A" or b[2] == "B" or b[2] == "AB":
            print("YES")
        else:
            print("IMPOSSIBLE")
    if b[0] == "AB" and b[1] == "A":
        if b[2] == "A" or b[2] == "B" or b[2] == "AB":
            print("YES")
        else:
            print("IMPOSSIBLE")
    if b[0] == "B" and b[1] == "B":
        if b[2] == "O" or b[2] == "B":
            print("YES")
        else:
            print("IMPOSSIBLE")
    if b[0] == "B" and b[1] == "AB":
        if b[2] == "A" or b[2] == "B" or b[2] == "AB":
            print("YES")
        else:
            print("IMPOSSIBLE")
    if b[0] == "AB" and b[1] == "B":
        if b[2] == "A" or b[2] == "B" or b[2] == "AB":
            print("YES")
        else:
            print("IMPOSSIBLE")
    if b[0] == "AB" and b[1] == "AB":
        if b[2] == "A" or b[2] == "B" or b[2] == "AB":
            print("YES")
        else:
            print("IMPOSSIBLE")