from collections import defaultdict


n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
record = defaultdict(int)
record[0] = - 1

s = res = 0
for i in range(n):
    s += a[i]
    if s % 7 in record:
        res = max(res, i - record[s % 7])
    else:
        record[s % 7] = i 
print(res) 