n = int(input())
res = 0
for i in range(n):
    b = int(input())
    b = str(b)
    res += pow(int(b[:-1]), int(b[-1]))
print(res)
