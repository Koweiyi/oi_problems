'''
https://www.luogu.com.cn/problem/P1048
'''
t, m = map(int, input().split())
c = []
w = []
for i in range(m):
    x, y = map(int, input().split())
    c.append(x)
    w.append(y)

f = [0] * (t + 1)
for i in range(m):
    for j in range(t, c[i] - 1, -1):
        f[j] = max(f[j], f[j - c[i]] + w[i])
print(f[t])
