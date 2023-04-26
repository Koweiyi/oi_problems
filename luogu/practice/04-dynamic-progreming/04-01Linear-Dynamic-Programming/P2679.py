'''
https://www.luogu.com.cn/problem/P2679
'''

n, m, k = map(int, input().split())
a = input()
b = input()
MOD = 10 ** 9 + 7

'''
f[i][j][k][0] = f[i - 1][j][k][0] + f[i - 1][j][k][1]
f[i][j][k][1] = f[i - 1][j - 1][k][1] 
              + f[i - 1][j - 1][k - 1][0] 
              + f[i - 1][j - 1][k - 1][1]

              
'''
f = [[[[0] * 2 for _ in range(m + 10)] for __ in range(m + 10)] for ___ in range(2)]
f[0][0][0][0] = 1
for i in range(1, n + 1):
    cur = i & 1
    f[cur][0][0][0] = 1
    for j in range(1, min(i, m) + 1):
        for x in range(1, min(j, k) + 1):
            f[cur][j][x][0] = f[cur][j][x][1] = 0
            f[cur][j][x][0] = (f[cur^1][j][x][0] + f[cur^1][j][x][1])% MOD
            if a[i - 1] == b[j - 1]:
                f[cur][j][x][1] = (f[cur ^ 1][j - 1][x][1] + f[cur ^ 1][j - 1][x - 1][0] + f[cur ^ 1][j - 1][x - 1][1]) % MOD

print((f[n&1][m][k][0] + f[n&1][m][k][1]) % MOD)

