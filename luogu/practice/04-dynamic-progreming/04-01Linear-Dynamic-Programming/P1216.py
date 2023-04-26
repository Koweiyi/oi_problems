r = int(input())
g = [[x for x in map(int, input().split())] for _ in range(r)]

for i in range(1, r):
    for j in range(len(g[i])):
        if j == 0:
            g[i][j] = max(g[i][j], g[i - 1][j] + g[i][j])
        elif j == len(g[i]) - 1:
            g[i][j] = max(g[i][j], g[i - 1][j - 1] + g[i][j])
        else:
            g[i][j] = max(g[i][j], g[i - 1][j] + g[i][j], g[i -1][j - 1] + g[i][j])

print(max(g[-1]))


