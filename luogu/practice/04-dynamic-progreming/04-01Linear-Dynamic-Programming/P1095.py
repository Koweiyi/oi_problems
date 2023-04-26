m, s, t = map(int, input().split())

f0 = f1 = 0
for i in range(t):
    if m >= 10:
        f0 += 60
        m -= 10
    else:
        m += 4
    f1 = max(f1 + 17, f0)
    if f1 >= s:
        print("Yes")
        print(i + 1)
        break
else:
    print("No")
    print(f1)



