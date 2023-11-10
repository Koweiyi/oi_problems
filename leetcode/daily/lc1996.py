#
# @lc app=leetcode.cn id=1996 lang=python3
# @lcpr version=21913
#
# [1996] 游戏中弱角色的数量
#
# https://leetcode.cn/problems/the-number-of-weak-characters-in-the-game/description/
#
# algorithms
# Medium (41.55%)
# Likes:    182
# Dislikes: 0
# Total Accepted:    29.9K
# Total Submissions: 71.9K
# Testcase Example:  '[[5,5],[6,3],[3,6]]'
#
# 你正在参加一个多角色游戏，每个角色都有两个主要属性：攻击 和 防御 。给你一个二维整数数组 properties ，其中 properties[i] =
# [attacki, defensei] 表示游戏中第 i 个角色的属性。
# 
# 如果存在一个其他角色的攻击和防御等级 都严格高于 该角色的攻击和防御等级，则认为该角色为 弱角色 。更正式地，如果认为角色 i 弱于 存在的另一个角色 j
# ，那么 attackj > attacki 且 defensej > defensei 。
# 
# 返回 弱角色 的数量。
# 
# 
# 
# 示例 1：
# 
# 输入：properties = [[5,5],[6,3],[3,6]]
# 输出：0
# 解释：不存在攻击和防御都严格高于其他角色的角色。
# 
# 
# 示例 2：
# 
# 输入：properties = [[2,2],[3,3]]
# 输出：1
# 解释：第一个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。
# 
# 
# 示例 3：
# 
# 输入：properties = [[1,5],[10,4],[4,3]]
# 输出：1
# 解释：第三个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= properties.length <= 10^5
# properties[i].length == 2
# 1 <= attacki, defensei <= 10^5
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
from sortedcontainers import SortedList
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # 有序集合过了，但是好慢,等等看下题解区，休息下

        # 算法瓶颈在排序上
        properties.sort(key=lambda x:[x[0], -x[1]])
        res = 0 
        mx = properties[-1][1]
        for i in range(len(properties) - 2, -1, -1):
            if properties[i][1] < mx:
                res += 1
            else:
                mx = properties[i][1] 
        return res 
# @lc code=end



#
# @lcpr case=start
# [[5,5],[6,3],[3,6]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,2],[3,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,5],[10,4],[4,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]]\n
# @lcpr case=end
#

