n = int(input())
pre = int(input())
p = q = 0
for i in range(n - 1):
    x = int(input())
    d = x - pre 
    pre = x
    if d > 0:
        p += d 
    else:
        q -= d
print(max(p, q))
print(abs(p - q) + 1)
