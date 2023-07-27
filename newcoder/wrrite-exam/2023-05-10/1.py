a = list(map(int, input().split()))

stk = []
for i in range(len(a)):
    flag = True
    stk.append(a[i])
    while flag:
        s = 0
        x = stk[-1]
        stk.pop()
        tmp = []
        while stk and s < a[i]:
            s += stk[-1]
            tmp.append(stk[-1])
            stk.pop()
        if s == x:
            stk.append(2 * x)
        else:
            stk.extend(tmp[::-1])
            stk.append(x)
            flag = False

while stk:
    print(stk[-1], end=" ")
    stk.pop()
