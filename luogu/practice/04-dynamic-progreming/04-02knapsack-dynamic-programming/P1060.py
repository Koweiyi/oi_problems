'''
https://www.luogu.com.cn/problem/P1060
'''
n, m = map(int, input().split())
c = []
w = []
for i in range(m):
    v, p = map(int, input().split())    
    c.append(v)
    w.append(v * p)

f = [0] * (n + 1)
for i in range(m):
    for j in range(n, c[i] - 1, -1):
        f[j] = max(f[j], f[j - c[i]] + w[i])
print(f[n])