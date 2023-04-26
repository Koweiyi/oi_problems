class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.next = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.next[idx] is None:
                cur.next[idx] = TrieNode()
            cur = cur.next[idx]
        cur.isEnd = True

    def search(self, str, pos, cur):
        if pos == len(str):
            return cur.isEnd
        
        idx = ord(str[pos]) - ord('a')
        if cur.next[idx] is None:
            return False

        return self.search(str, pos+1, cur.next[idx])


n = int(input())
tries = [Trie() for _ in range(n)]

for i in range(n):
    strs = input().split()[1:]
    for s in strs:
        tries[i].insert(s)

m = int(input())
for i in range(m):
    x = input()
    for j in range(n):
        if tries[j].search(x, 0, tries[j].root):
            print(j + 1, end=" ")
    print("")

