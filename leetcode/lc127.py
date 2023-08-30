#
# @lc app=leetcode.cn id=127 lang=python3
# @lcpr version=21913
#
# [127] 单词接龙
#
# https://leetcode.cn/problems/word-ladder/description/
#
# algorithms
# Hard (48.25%)
# Likes:    1281
# Dislikes: 0
# Total Accepted:    190.9K
# Total Submissions: 395.6K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 ->
# s2 -> ... -> sk：
# 
# 
# 每一对相邻的单词只差一个字母。
# 对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
# sk == endWord
# 
# 
# 给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列
# 中的 单词数目 。如果不存在这样的转换序列，返回 0 。
# 
# 
# 示例 1：
# 
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# 输出：5
# 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
# 
# 
# 示例 2：
# 
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# 输出：0
# 解释：endWord "cog" 不在字典中，所以无法进行转换。
# 
# 
# 
# 提示：
# 
# 
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord、endWord 和 wordList[i] 由小写英文字母组成
# beginWord != endWord
# wordList 中的所有字符串 互不相同
# 
# 
#
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter, defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        g = []
        mp = defaultdict()
        cur = 0 
        wordList.append(beginWord)
        for w in wordList:
            mp[w] = cur
            g.append([]) 
            cur += 1
            lw = list(w)
            for j in range(len(lw)):
                t = lw[j]
                lw[j] = "."
                if "".join(lw) not in mp:
                    mp["".join(lw)] = cur
                    cur += 1
                    g.append([])
                g[mp[w]].append(mp["".join(lw)])
                g[mp["".join(lw)]].append(mp[w])
                lw[j] = t 
        if beginWord not in mp or endWord not in mp:
            return 0 
        res = 0 
        vis = set()
        q = [mp[beginWord]] 

        while q:
            print(q)
            tmp = q 
            q = [] 
            for x in tmp:
                if x == mp[endWord]:
                    return res // 2 + 1
                for y in g[x]:
                    if y not in vis:
                        vis.add(y)
                        q.append(y)
            res += 1
        return 0 





# @lc code=end



#
# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]\n
# @lcpr case=end

# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log"]\n
# @lcpr case=end

#

