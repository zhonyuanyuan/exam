a = ["飢餓遊戲3","解憂雜貨店","怪獸與牠門的產地","哈利波特6","我的阿富汗筆友","祈念之樹","樓下的房客","小王子"]
b = ["房思琪的初戀樂園","等一個人咖啡","鬼滅之刃 14","神農嘗百草","麥田捕手","老人與海","傲慢與偏見","與神同行"]
c = input("請輸入欲租借的書籍:")
d = 0
for i in range(len(a)):
    if c == a[i]:
        print("在書架A的第",i+1,"本")
        d += 1
for i in range(len(b)):
    if c == b[i]:
        print("在書架B的第",i+1,"本")
        d += 1
if d == 0 :
    print("查無此書籍")