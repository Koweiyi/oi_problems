from bisect import bisect_left


n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for i in range(1, n + 1):
    print(a[bisect_left(a, i)] - i)
