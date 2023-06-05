from collections import defaultdict
from bisect import bisect_left
s = input()
t = input()

record = defaultdict(list)

for i, x in enumerate(s):
    record[x].append(i)
res = 0
for i in range(len(s)):
    cur = i
    flag = True
    for x in t:
        nx = bisect_left(record[x], cur)
        if nx < len(record[x]):
            cur = record[x][nx] + 1
        else:
            flag = False
            break
    if flag: 
        res += len(s) - cur + 1
print(res)

