a = input("輸入月及日為:").split(" ")
if a[0] == "01" or a[0] == "1":
    if int(a[1]) >= 21 :
        print("星座為:Aquarius")
    else:
        print("星座為:Capricorn")
if a[0] == "02" or a[0] == "2":
    if int(a[1]) >= 19 :
        print("星座為:Pisces")
    else:
        print("星座為:Aquarius")
if a[0] == "03" or a[0] == "3":
    if int(a[1]) >= 21 :
        print("星座為:Aries")
    else:
        print("星座為:Pisces")
if a[0] == "04" or a[0] == "4":
    if int(a[1]) >= 21 :
        print("星座為:Taurus")
    else:
        print("星座為:Aries")
if a[0] == "05" or a[0] == "5":
    if int(a[1]) >= 22 :
        print("星座為:Gemini")
    else:
        print("星座為:Taurus")
if a[0] == "06" or a[0] == "6":
    if int(a[1]) >= 22 :
        print("星座為:Cancer")
    else:
        print("星座為:Gemini")
if a[0] == "07" or a[0] == "7":
    if int(a[1]) >= 23 :
        print("星座為:Leo")
    else:
        print("星座為:Cancer")
if a[0] == "08" or a[0] == "8":
    if int(a[1]) >= 24 :
        print("星座為:Virgo")
    else:
        print("星座為:Leo")
if a[0] == "09" or a[0] == "9":
    if int(a[1]) >= 24 :
        print("星座為:Libra")
    else:
        print("星座為:Virgo")
if a[0] == "10":
    if int(a[1]) >= 24 :
        print("星座為:Scorpio")
    else:
        print("星座為:Libra")
if a[0] == "11":
    if int(a[1]) >= 23 :
        print("星座為:Sagittarius")
    else:
        print("星座為:Scorpio")
if a[0] == "12":
    if int(a[1]) >= 22 :
        print("星座為:Capricorn")
    else:
        print("星座為:Sagittarius")