z = 2
a = input("國文:")
b = input("英文:")
c = input("微積分:")
d = input("體育:")
e = input("程式設計:")
f = []
f.append(a)
f.append(b)
f.append(c)
f.append(d)
f.append(e)
l = 100
h = 0
ava = 0
for i in range(len(f)):
    ava += int(f[i])
    if int(f[i]) > int(h):
        h = f[i]
    if int(f[i]) < int(l):
        l = f[i]
ava /= 5
ava += 0.001
ava = ('%.2f'%ava) 
print(ava)
print("平均分數:",ava)
while z != 0 :
    if int(h) == int(a):
        print("最高分科目:","國文",h,"分")
        break
    elif int(h) == int(b):
        print("最高分科目:","英文",h,"分")
        break
    elif int(h) == int(c):
        print("最高分科目:","微積分",h,"分")
        break
    elif int(h) == int(d):
        print("最高分科目:","體育",h,"分")
        break
    elif int(h) == int(e):
        print("最高分科目:","程式設計",h,"分")
        break
    else:
        break
while z != 0 :
    if int(l) == int(a):
        print("最低分科目:","國文",l,"分")
        break
    elif int(l) == int(b):
        print("最低分科目:","英文",l,"分")
        break
    elif int(l) == int(c):
        print("最低分科目:","微積分",l,"分")
        break
    elif int(l) == int(d):
        print("最低分科目:","體育",l,"分")
        break
    elif int(l) == int(e):
        print("最低分科目:","程式設計",l,"分")
        break
    else:
        break
