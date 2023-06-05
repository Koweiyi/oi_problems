n = input()
res = 0
def solve(pre, i, s):
    global res
    if i == len(n):
        res += s + int(n[pre:i])
        return 
    solve(pre, i + 1, s)
    solve(i + 1, i + 1, s + int(n[pre: i]))
solve(0,0,0)
print(res)

