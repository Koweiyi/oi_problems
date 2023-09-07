from functools import lru_cache
n = int(input())

mx = n + 5
ables = []
able = [False] * mx
able[1] = True
for i in range(1, mx):
    if able[i]:
        if i * 2 + 1 < mx:
            able[i * 2 + 1] = True  
        for j in ables:
            if i + j + 1 < mx:
                able[i + j + 1] = True 
            else:break
        ables.append(i)

if not able[n]:
    print(0)

mod = 10 ** 9 + 7

@lru_cache
def dfs(i: int) -> int:
    if i == 1 or i == 3:
        return 1
    res = 0
    for j in range(1, i // 2 + 2):
        x = j
        y = i - x - 1
        if x < y and able[x] and able[y]:
            res = (res + dfs(x) * dfs(y) * 2) % mod 
        elif x == y and able[x] and able[y]:
            res = (res + dfs(x) * dfs(y)) % mod 
    return res 
print(dfs(n))

    



