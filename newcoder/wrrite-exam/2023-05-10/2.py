x = input()
y = int(input())

def check(num):
    return len(set(str(num))) == 1 and 3 <= len(str(num)) <= 12

def cul(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2 
    return n1 * n2

res = -1
op = input()
if op == '*':
    for st in range(len(x)):
        for j in range (1, 5):
            if st + j <= len(x):
                n1 = int(x[st:st + j])
                if check(cul(n1, y, op)):
                    res = max(res, n1)
else:
    for st in range(len(x)):
        for ed in range(st, len(x)):
            n1 = int(x[st: ed + 1])
            if check(cul(n1, y, op)):
                res = max(res, n1)
print(res)
