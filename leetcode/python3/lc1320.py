#
# @lc app=leetcode.cn id=1320 lang=python3
# @lcpr version=30109
#
# [1320] 二指输入的的最小距离
#
# https://leetcode.cn/problems/minimum-distance-to-type-a-word-using-two-fingers/description/
#
# algorithms
# Hard (60.95%)
# Likes:    84
# Dislikes: 0
# Total Accepted:    4K
# Total Submissions: 6.6K
# Testcase Example:  '"CAKE"'
#
# 
# 
# 二指输入法定制键盘在 X-Y 平面上的布局如上图所示，其中每个大写英文字母都位于某个坐标处。
# 
# 
# 例如字母 A 位于坐标 (0,0)，字母 B 位于坐标 (0,1)，字母 P 位于坐标 (2,3) 且字母 Z 位于坐标 (4,1)。
# 
# 
# 给你一个待输入字符串 word，请你计算并返回在仅使用两根手指的情况下，键入该字符串需要的最小移动总距离。
# 
# 坐标 (x1,y1) 和 (x2,y2) 之间的 距离 是 |x1 - x2| + |y1 - y2|。 
# 
# 注意，两根手指的起始位置是零代价的，不计入移动总距离。你的两根手指的起始位置也不必从首字母或者前两个字母开始。
# 
# 
# 
# 示例 1：
# 
# 输入：word = "CAKE"
# 输出：3
# 解释： 
# 使用两根手指输入 "CAKE" 的最佳方案之一是： 
# 手指 1 在字母 'C' 上 -> 移动距离 = 0 
# 手指 1 在字母 'A' 上 -> 移动距离 = 从字母 'C' 到字母 'A' 的距离 = 2 
# 手指 2 在字母 'K' 上 -> 移动距离 = 0 
# 手指 2 在字母 'E' 上 -> 移动距离 = 从字母 'K' 到字母 'E' 的距离  = 1 
# 总距离 = 3
# 
# 
# 示例 2：
# 
# 输入：word = "HAPPY"
# 输出：6
# 解释： 
# 使用两根手指输入 "HAPPY" 的最佳方案之一是：
# 手指 1 在字母 'H' 上 -> 移动距离 = 0
# 手指 1 在字母 'A' 上 -> 移动距离 = 从字母 'H' 到字母 'A' 的距离 = 2
# 手指 2 在字母 'P' 上 -> 移动距离 = 0
# 手指 2 在字母 'P' 上 -> 移动距离 = 从字母 'P' 到字母 'P' 的距离 = 0
# 手指 1 在字母 'Y' 上 -> 移动距离 = 从字母 'A' 到字母 'Y' 的距离 = 4
# 总距离 = 6
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= word.length <= 300
# 每个 word[i] 都是一个大写英文字母。
# 
# 
#


# @lcpr-template-start
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from itertools import accumulate
from functools import cache
from typing import Optional
from typing import List
from cmath import inf
from string import ascii_uppercase
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumDistance(self, word: str) -> int:

        mp = {}
        for i, c in enumerate(ascii_uppercase):
            mp[c] = [i // 6, i % 6]

        def calc(i: int, j: int) -> int:
            if i == -1:
                return 0 
            x1, y1 = mp[word[i]]
            x2, y2 = mp[word[j]] 
            return abs(x2 - x1) + abs(y2 - y1)
    
        @cache 
        def dfs(i, l, r):
            if i == len(word):
                return 0 
            return min(dfs(i + 1, i, r) + calc(l, i), dfs(i + 1, l, i) + calc(r, i))
        return dfs(0, -1, -1)

# @lc code=end



#
# @lcpr case=start
# "CAKE"\n
# @lcpr case=end

# @lcpr case=start
# "HAPPY"\n
# @lcpr case=end

#

