n = int(input())

mod = 10 ** 9 + 7
dp = [[0] * 3 for _ in range(n + 1)] 
for i in range(n):
    # dp[i + 1][0] = pow(3, i, mod) + 2 * (pow(3, i, mod) - pow(2, i, mod))
    # dp[i + 1][0] = pow(3, i + 1, mod) - pow(2, i + 1, mod)
    dp[i + 1][1] = (dp[i][1] * 2 + pow(3,i,mod) - pow(2,i,mod)) % mod
    dp[i + 1][2] = (dp[i][2] * 2 + dp[i][1]) % mod

print(dp[n][2])

""""
redr
rede
redd
rerd
reed

rded
rred
ered
dred
"""