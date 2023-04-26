from cmath import inf

n,c,m = map(int, input().split())
g = [x for x in map(int, input().split())]
t = [x for x in map(int, input().split())]
w = [[] for _ in range(c)]
for i in range(n):
    w[t[i] - 1].append(g[i])

dp = [0] * (m + 1)
for i in range(c):
    for j in range(m, 0, -1):
        res = -inf
        for k in w[i]:
            if j >= k:
                res = max(res, dp[j - k] + k)
        dp[j] = res
print(dp[m])





'''
5 3 50
10 3 23 13 21
1 2 2 1 3
'''

