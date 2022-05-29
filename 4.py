from cmath import sqrt


x = int(input("X軸座標:"))
y = int(input("Y軸座標:"))
a = x**2 + y**2
if x > 0 and y > 0 :
    print("該點位於第一象限，離原點距離為根號",a)
elif x > 0 and y < 0 :
    print("該點位於第四象限，離原點距離為根號",a)
elif x < 0 and y > 0 :
    print("該點位於第二象限，離原點距離為根號",a)
elif x < 0 and y < 0 :
    print("該點位於第三象限，離原點距離為根號",a)
elif x == 0 and y == 0 :
    print("該點位於原點")
elif x > 0 and y == 0 :
    print("該點位於右半面X軸上，離原點距離為根號",a)
elif x < 0 and y == 0 :
    print("該點位於左半面X軸上，離原點距離為根號",a)
elif x == 0 and y > 0 :
    print("該點位於上半面Y軸上，離原點距離為根號",a)
elif x == 0 and y < 0 :
    print("該點位於下半面Y軸上，離原點距離為根號",a)