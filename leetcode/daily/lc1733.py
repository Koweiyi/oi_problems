#
# @lc app=leetcode.cn id=1733 lang=python3
# @lcpr version=21917
#
# [1733] 需要教语言的最少人数
#
# https://leetcode.cn/problems/minimum-number-of-people-to-teach/description/
#
# algorithms
# Medium (48.82%)
# Likes:    25
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 7.7K
# Testcase Example:  '2\n[[1],[2],[1,2]]\n[[1,2],[1,3],[2,3]]'
#
# 在一个由 m 个用户组成的社交网络里，我们获取到一些用户之间的好友关系。两个用户之间可以相互沟通的条件是他们都掌握同一门语言。
# 
# 给你一个整数 n ，数组 languages 和数组 friendships ，它们的含义如下：
# 
# 
# 总共有 n 种语言，编号从 1 到 n 。
# languages[i] 是第 i 位用户掌握的语言集合。
# friendships[i] = [u​​​​​​i​​​, v​​​​​​i] 表示 u^​​​​​​​​​​​i​​​​​ 和 vi 为好友关系。
# 
# 
# 你可以选择 一门 语言并教会一些用户，使得所有好友之间都可以相互沟通。请返回你 最少 需要教会多少名用户。
# 请注意，好友关系没有传递性，也就是说如果 x 和 y 是好友，且 y 和 z 是好友， x 和 z 不一定是好友。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
# 输出：1
# 解释：你可以选择教用户 1 第二门语言，也可以选择教用户 2 第一门语言。
# 
# 
# 示例 2：
# 
# 输入：n = 3, languages = [[2],[1,3],[1,2],[3]], friendships =
# [[1,4],[1,2],[3,4],[2,3]]
# 输出：2
# 解释：教用户 1 和用户 3 第三门语言，需要教 2 名用户。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= n <= 500
# languages.length == m
# 1 <= m <= 500
# 1 <= languages[i].length <= n
# 1 <= languages[i][j] <= n
# 1 <= u​​​​​​i < v​​​​​​i <= languages.length
# 1 <= friendships.length <= 500
# 所有的好友关系 (u​​​​​i, v​​​​​​i) 都是唯一的。
# languages[i] 中包含的值互不相同。
# 
# 
#
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from itertools import accumulate
from functools import cache
from typing import Optional
from typing import List
from cmath import inf
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        mp = set()
        record = defaultdict(set)
        for i, ls in enumerate(languages, 1):
            for l in ls:
                record[l].add(i)
        for x, y in friendships:
            f = False 
            for lx in languages[x - 1]:
                for ly in languages[y - 1]:
                    if lx == ly:
                        f = True 
            if not f:
                mp.add(x) 
                mp.add(y)
        res = inf 
        for l in range(1, n + 1):
            tot = 0
            for x in mp:
                if x not in record[l]:
                    tot += 1
            res = min(res, tot) 
        return res 





     

# @lc code=end



#
# @lcpr case=start
# 2\n[[1],[2],[1,2]]\n[[1,2],[1,3],[2,3]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[2],[1,3],[1,2],[3]]\n[[1,4],[1,2],[3,4],[2,3]]\n
# @lcpr case=end

# @lcpr case=start
# 17\n[[4,7,2,14,6],[15,13,6,3,2,7,10,8,12,4,9],[16],[10],[10,3],[4,12,8,1,16,5,15,17,13],[4,13,15,8,17,3,6,14,5,10],[11,4,13,8,3,14,5,7,15,6,9,17,2,16,12],[4,14,6],[16,17,9,3,11,14,10,12,1,8,13,4,5,6],[14],[7,14],[17,15,10,3,2,12,16,14,1,7,9,6,4]]\n[[4,11],[3,5],[7,10],[10,12],[5,7],[4,5],[3,8],[1,5],[1,6],[7,8],[4,12],[2,4],[8,9],[3,10],[4,7],[5,12],[4,9],[1,4],[2,8],[1,2],[3,4],[5,10],[2,7],[1,7],[1,8],[8,10],[1,9],[1,10],[6,7],[3,7],[8,12],[7,9],[9,11],[2,5],[2,3]]\n
# @lcpr case=end

#

