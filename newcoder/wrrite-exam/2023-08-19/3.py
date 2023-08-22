n, m, k = map(int, input().split())
a = list(map(int, input().split()))
h = list(map(int, input().split()))

# 构建交通时间矩阵
W = [[float('inf')] * n for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    W[u-1][v-1] = w
    W[v-1][u-1] = w

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        dp[i][j] = dp[i-1][j]
        if j >= h[i-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-h[i-1]] + a[i-1])
            if i >= 2:
                dp[i][j] = max(dp[i][j], dp[i-2][j-h[i-1]-h[i-2]] + a[i-1] + a[i-2])
                if i >= 3:
                    dp[i][j] = max(dp[i][j], dp[i-3][j-h[i-1]-h[i-2]-h[i-3]] + a[i-1] + a[i-2] + a[i-3])
        dp[i][j] += a[i-1]

print(dp[n][k])