'''
https://www.luogu.com.cn/problem/P1541
'''
from collections import Counter


n, m = map(int, input().split())

nums = [x for x in map(int, input().split())]
b = [x for x in map(int, input().split())]

cnt = Counter(b)
f = [[[0] * 45 for __ in range(45) ] for _ in range(45)] 
# f[0][0][0] = nums[0]
for a in range(cnt[1] + 1):
    for b in range(cnt[2] + 1):
        for c in range(cnt[3] + 1):
            for d in range(cnt[4] + 1):
                r =  a + 2 * b + 3 * c + 4 * d    
                if b: f[b][c][d] = max(f[b][c][d], f[b - 1][c][d])
                if c: f[b][c][d] = max(f[b][c][d], f[b][c - 1][d])
                if d: f[b][c][d] = max(f[b][c][d], f[b][c][d - 1])
                f[b][c][d] += nums[r]


print(f[cnt[2]][cnt[3]][cnt[4]])


