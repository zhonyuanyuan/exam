a = input("輸入值為(，隔開)").split(",")
a.sort()
c = ""
e = ""
z = 0
for i in a:
    c = c + i
d = a
d.reverse()
for i in d:
    e = e + i
z = int(e) - int(c)
print("最大值數列與最小值數列差值為:",z)