a = input("組數為:")
for i in range(int(a)):
    print("第",i+1,"組為:",end="")
    b = input("").split(" ")
    c = int(b[0]) * 250
    d = int(b[1]) * 175
    e = c + d
    print("第",i+1,"組應收費用:",e)
    c = 0
    d = 0
    e = 0