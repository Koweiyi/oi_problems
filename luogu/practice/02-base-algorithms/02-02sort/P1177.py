import sys
sys.setrecursionlimit(1000000)

n = int(input())
a = [x for x in map(int, input().split())]

def partition(a, l, r):
    i = j = l
    for j in range(l, r):
        if a[j] < a[r]:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[i], a[r] = a[r], a[i]
    return i

def quick_sort(a, l, r):
    if l >= r:
        return
    p = partition(a, l, r)
    quick_sort(a, l, p - 1)
    quick_sort(a, p + 1, r)

quick_sort(a, 0, n - 1)
for x in a:
    print(x, end=" ")
