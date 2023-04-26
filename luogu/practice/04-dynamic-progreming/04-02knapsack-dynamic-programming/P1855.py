'''
https://www.luogu.com.cn/problem/P1855
'''
n, M, T = map(int, input().split())
m = []
t = []
for i in range(n):
    x, y = map(int, input().split())
    m.append(x)
    t.append(y)
f = [[0] * (M + 1) for _ in range(T + 1)]
for i in range(n):
    for j in range(M, m[i] - 1, -1):
        for k in range(T, t[i] - 1, -1):
            f[j][k] = max(f[j][k], f[j - m[i]][k - t[i]] + 1)
print(f[M][T])
            
