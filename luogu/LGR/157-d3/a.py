n, m = map(int, input().split())

if n <= m // 2:
    print(0)
else:
    res = 0
    n -= m // 2
    if m & 1:
        res += 2
        n -= 1
    while n > 0 :
        res += 4
        n -= 1
    print(res)

    