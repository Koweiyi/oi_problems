n, m = map(int, input().split())
r1 = [_ for _ in range(n + 1)]
def find(x):
    if x != r1[x]:
        r1[x] = find(r1[x])
    return r1[x]

def union(x, y):
    rx, ry = find(x), find(y)
    if rx != ry:
        r1[rx] = ry

for i in range(m):
    u, v = map(int, input().split())
    union(u, v) 

r2 = [_ for _ in range(n + 1)]
s = [1] * (n + 1)
k = int(input())

def find2(x):
    if x != r2[x]:
        r2[x] = find2(r2[x])
    return r2[x]

def union2(x, y):
    rx, ry = find2(x), find2(y)
    if rx != ry:
        r2[rx] = ry
        tot = s[rx] + s[ry]
        s[rx] = s[ry] = tot 


g = [set() for _ in range(n + 1)]    

for i in range(k):
    u, v = map(int, input().split())
    if find(u) == find(v):
        union2(u, v)
    else:
        for w in g[u]:
            if find(v) == find(w):
                union2(v, w)
        for w in g[v]:
            if find(u) == find(w):
                union2(u, w)
        g[u].add(v)
        g[v].add(u)

mx = -1
mn = 999999999
for i in range(1, n + 1):
    sz = s[find2(i)]
    mx = max(mx, sz)
    mn = min(mn, sz)
print(mx, mn)

