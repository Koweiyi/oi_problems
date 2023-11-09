from math import isqrt  
primes = []
mx = 10 ** 5 + 5 
vis = [False] * mx
vis[0] = vis[1] = True
for i in range(2, isqrt(mx)):
    if not vis[i]:
        for j in range(i * i, mx, i):
            vis[j] = True 
for i in range(2, mx):
    if not vis[i]:
        primes.append(i)
print(len(primes))