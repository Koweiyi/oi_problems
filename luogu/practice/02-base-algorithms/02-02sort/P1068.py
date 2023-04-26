n, m = map(int, input().split())

p = []
for i in range(n):
    x, y = map(int, input().split())
    p.append((x, y))

p.sort(key=lambda x:(-x[1], x[0]))
m = int(m * 1.5)
s = int(p[m - 1][1])
while m < n and p[m][1] == s:
    m += 1
print(s, m)
for x, y in p[:m]:
    print(x, y)

