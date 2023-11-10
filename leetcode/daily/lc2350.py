#
# @lc app=leetcode.cn id=2350 lang=python3
# @lcpr version=21914
#
# [2350] 不可能得到的最短骰子序列
#
# https://leetcode.cn/problems/shortest-impossible-sequence-of-rolls/description/
#
# algorithms
# Hard (65.16%)
# Likes:    43
# Dislikes: 0
# Total Accepted:    4.2K
# Total Submissions: 6.5K
# Testcase Example:  '[4,2,1,2,3,3,2,4,1]\n4'
#
# 给你一个长度为 n 的整数数组 rolls 和一个整数 k 。你扔一个 k 面的骰子 n 次，骰子的每个面分别是 1 到 k ，其中第 i
# 次扔得到的数字是 rolls[i] 。
# 
# 请你返回 无法 从 rolls 中得到的 最短 骰子子序列的长度。
# 
# 扔一个 k 面的骰子 len 次得到的是一个长度为 len 的 骰子子序列 。
# 
# 注意 ，子序列只需要保持在原数组中的顺序，不需要连续。
# 
# 
# 
# 示例 1：
# 
# 输入：rolls = [4,2,1,2,3,3,2,4,1], k = 4
# 输出：3
# 解释：所有长度为 1 的骰子子序列 [1] ，[2] ，[3] ，[4] 都可以从原数组中得到。
# 所有长度为 2 的骰子子序列 [1, 1] ，[1, 2] ，... ，[4, 4] 都可以从原数组中得到。
# 子序列 [1, 4, 2] 无法从原数组中得到，所以我们返回 3 。
# 还有别的子序列也无法从原数组中得到。
# 
# 示例 2：
# 
# 输入：rolls = [1,1,2,2], k = 2
# 输出：2
# 解释：所有长度为 1 的子序列 [1] ，[2] 都可以从原数组中得到。
# 子序列 [2, 1] 无法从原数组中得到，所以我们返回 2 。
# 还有别的子序列也无法从原数组中得到，但 [2, 1] 是最短的子序列。
# 
# 
# 示例 3：
# 
# 输入：rolls = [1,1,3,2,2,2,3,3], k = 4
# 输出：1
# 解释：子序列 [4] 无法从原数组中得到，所以我们返回 1 。
# 还有别的子序列也无法从原数组中得到，但 [4] 是最短的子序列。
# 
# 
# 
# 
# 提示：
# 
# 
# n == rolls.length
# 1 <= n <= 10^5
# 1 <= rolls[i] <= k <= 10^5
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
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        s = set()
        res = 1 
        for x in rolls:
            s.add(x)
            if len(s) == k:
                res += 1
                s.clear()
        return res 
# @lc code=end



#
# @lcpr case=start
# [4,2,1,2,3,3,2,4,1]\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,1,3,2,2,2,3,3]\n4\n
# @lcpr case=end

#

