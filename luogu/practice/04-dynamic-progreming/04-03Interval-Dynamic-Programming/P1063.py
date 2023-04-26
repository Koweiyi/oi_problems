from cmath import inf
from functools import lru_cache
import sys
sys.setrecursionlimit(1000000)


n = int(input())
head = [x for x in map(int, input().split())]
head += head
mars = list(zip(head, head[1:] + head[:1]))


@lru_cache()
def dfs(i, j):
    if i == j:
        return 0
    res = 0
    for m in range(i, j):
        res = max(res, dfs(i, m) + dfs(m + 1, j) + mars[i][0] * mars[m][1] * mars[j][1])
    return res 

res = -inf 
for i in range(n):
    res = max(res, dfs(i, i + n - 1))
print(res)
