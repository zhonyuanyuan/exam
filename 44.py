a = int(input(""))
ans = 0
for i in range(a):
    c = int(input(""))
    if c > ans:
        ans = c
print(ans)