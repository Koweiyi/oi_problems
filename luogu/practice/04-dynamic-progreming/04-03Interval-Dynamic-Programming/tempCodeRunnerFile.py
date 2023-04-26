n = int(input())
a  = [int(input()) for _ in range(n)]

res = 0

# @lru_cache()
# def dfs(i, j):
#     global res 
#     if i == j:
#         return a[i]
#     dfs(i + 1, j)
#     dfs(i, j - 1)
#     x = 0
#     for m in range(i, j):
#         l, r = dfs(i, m), dfs(m + 1, j)
#         if  l == r and l != 0 and r != 0:
#             x = max(x, l + 1)
#             res = max(res, l + 1)
#     return x 

# print(res)
f = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    f[i][i] = a[i - 1]

for len in range(2, n + 1):
    # l + len - 1 < n ==> l < n + 1 - len
    for l in range(1, n + 1 - len + 1):
        j = l + len - 1
        for m in range(i, j):
            if f[i][m] == f[m + 1][j] and f[i][m] != 0 and f[m + 1][j] != 0:
                f[j][j] = max(f[i][j], f[i][m] + 1)
                res = max(res, f[i][m] + 1)

print(res)
