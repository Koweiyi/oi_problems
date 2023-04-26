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
        
        # 24 - 26是修改后的逻辑，相比模板只改了这三行,search 原定义是搜索字符串是否在字典树中
        if cur.isEnd:
            if self.search(str,pos, self.root):
                return True
        
        idx = ord(str[pos]) - ord('a')
        if cur.next[idx] is None:
            return False

        return self.search(str, pos+1, cur.next[idx])

class Solution:
    def can_construct(self, str_arr, str):
        trie = Trie()
        for s in str_arr:
            trie.insert(s)
        return trie.search(str, 0, trie.root)
sl = ["hello","world","hel"] 
s = "helloworld"
print(Solution().can_construct(sl, s))