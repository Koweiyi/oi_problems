'''
https://www.luogu.com.cn/problem/P1868
'''

from collections import defaultdict


n = int(input())
g = defaultdict(list)

mx = 0
for i in range(n):
    x, y = map(int, input().split())
    g[y].append(x)
    mx = max(mx, y)
f = [0] * (mx + 1)
for i in range(1, mx + 1):
    f[i] = f[i - 1]
    if i in g:
        for x in g[i]:
            f[i] = max(f[i], f[x - 1] + i - x + 1)

print(f[mx])


