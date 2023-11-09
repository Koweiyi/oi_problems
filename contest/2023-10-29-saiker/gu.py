n = int(input())

res = 0
for i in range(1, n + 1):
    if i & 1:
        res += 1 
    else:
        if i % 4:
            continue
        else:
            res += 1
print(res)
