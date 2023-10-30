n = int(input())
res = 0
while n:
    if n % 2 == 0:
        res += 1
    n //= 2
print(res)

