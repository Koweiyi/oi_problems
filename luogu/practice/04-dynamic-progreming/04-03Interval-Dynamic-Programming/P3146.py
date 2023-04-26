

# @lru_cache()
# def dfs(i, j):
#     global res 
#     if i == j:
#         return a[i]
   
#     x = 0
#     for m in range(i, j):
#         l, r = dfs(i, m), dfs(m + 1, j)
#         if  l == r and l != 0 and r != 0:
#             x = max(x, l + 1)
#             res = max(res, l + 1)
#     dfs(i + 1, j)
#     dfs(i, j - 1)
#     return x 

# print(res)

n = int(input())
a  = [int(input()) for _ in range(n)]
res = 0
f = [[-1] * (n + 10) for _ in range(60)]
for i in range(n):
    f[a[i]][i] = i + 1
res = 0
for i in range(2, 59):
    for j in range(n):
        if f[i][j] == -1:
            f[i][j] = f[i - 1][f[i - 1][j]]
        if f[i][j] != -1:
            res = i  
print(res)

