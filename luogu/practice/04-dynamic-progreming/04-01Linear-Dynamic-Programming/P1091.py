from bisect import bisect_left
from typing import List
n = int(input())
t = [x for x in map(int, input().split())]

def solve(nums: List[int], val: int) -> int:
    f = []
    for x in nums:
        if not f or x > f[-1]:
            f.append(x)
        else:
            idx = bisect_left(f, x)
            f[idx] = x
    return bisect_left(f, val)

res = 0
for i in range(n):
    l = r = 0
    if i > 0:
        l = solve(t[:i], t[i])
    if i < n - 1:
        r = solve(t[i + 1:][::-1], t[i])
    res = max(res, l + r + 1)
print(n - res)
