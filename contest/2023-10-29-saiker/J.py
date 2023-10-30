s = input()

def calc(x):
    if x == ' ':
        return 1 
    if x in "adgjmptw":
        return 1
    if x in "behknqux":
        return 2 
    if x in "cfilorvy":
        return 3
    return 4
res = 0
for x in s:
    res += calc(x)
print(res)
