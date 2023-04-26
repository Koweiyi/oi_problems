n = int(input())
rec = []
for i in range(n):
    x, y, lenx, leny = map(int, input().split())
    rec.append((x, y, lenx, leny))
px, py = map(int, input().split())
for i in range(n - 1, -1, -1):
    x, y, lenx, leny = rec[i]
    if px >= x and px <= x + lenx and py >= y and py <= y + leny:
        print(i + 1)
        break
else:
    print(-1)