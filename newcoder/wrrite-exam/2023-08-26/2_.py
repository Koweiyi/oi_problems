n = int(input())
s = set()
res = [""] * n 

def check(x: str) -> bool:
    j = 0 
    t = "red"
    for ch in x:
        if ch == t[j]:
            j += 1
            if j == 3:
                break
    return j == 3
def dfs(i:int):
    if i == n:
        if check("".join(res)):
            s.add("".join(res))
        return 
    for ch in "red":
        res[i] = ch
        dfs(i + 1)
dfs(0)
print(len(s))
