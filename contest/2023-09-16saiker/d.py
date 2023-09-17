from itertools import count

i = 0
for j in count(1):
    print(j)
    if i > 100:
        break
    i += 1
    
    