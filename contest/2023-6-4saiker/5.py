def get_next(s):
    n = len(s) 
    next = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = next[j - 1]
        if s[i] == s[j]:
            j += 1
        next[i] = j
    return next

def count_repeated_substring(s):
    n = len(s)
    next = get_next(s)
    count = 0
    for i in range(1, n):
        next_P = next[i - 1]
        if next_P > 0 or next_P >= i // 2:
            count += 1
    return count

s = input()
print(count_repeated_substring(s) + len(s))
