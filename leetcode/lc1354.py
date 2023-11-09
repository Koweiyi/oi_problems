#
# @lc app=leetcode.cn id=1354 lang=python3
# @lcpr version=21917
#
# [1354] 多次求和构造目标数组
#
# https://leetcode.cn/problems/construct-target-array-with-multiple-sums/description/
#
# algorithms
# Hard (29.01%)
# Likes:    88
# Dislikes: 0
# Total Accepted:    4.4K
# Total Submissions: 15.2K
# Testcase Example:  '[9,3,5]'
#
# 给你一个整数数组 target 。一开始，你有一个数组 A ，它的所有元素均为 1 ，你可以执行以下操作：
#
#
# 令 x 为你数组里所有元素的和
# 选择满足 0 <= i < target.size 的任意下标 i ，并让 A 数组里下标为 i 处的值为 x 。
# 你可以重复该过程任意次
#
#
# 如果能从 A 开始构造出目标数组 target ，请你返回 True ，否则返回 False 。
#
#
#
# 示例 1：
#
# 输入：target = [9,3,5]
# 输出：true
# 解释：从 [1, 1, 1] 开始
# [1, 1, 1], 和为 3 ，选择下标 1
# [1, 3, 1], 和为 5， 选择下标 2
# [1, 3, 5], 和为 9， 选择下标 0
# [9, 3, 5] 完成
#
#
# 示例 2：
#
# 输入：target = [1,1,1,2]
# 输出：false
# 解释：不可能从 [1,1,1,1] 出发构造目标数组。
#
#
# 示例 3：
#
# 输入：target = [8,5]
# 输出：true
#
#
#
#
# 提示：
#
#
# N == target.length
# 1 <= target.length <= 5 * 10^4
# 1 <= target[i] <= 10^9
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
from heapq import heapify, heappop, heappush


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        tot = sum(target)
        target = [-x for x in target]
        heapify(target)
        n = len(target)
        while tot > n:
            p = -heappop(target)
            left = tot - p
            if left >= p:
                return False
            tot -= left * (p // left - int(p % left == 0))
            heappush(target, -left if p % left == 0 else -(p % left))
        return True

        "{\"version\"" + data + "..."


# @lc code=end


#
# @lcpr case=start
# [9,3,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [8,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1000000000]\n
# @lcpr case=end

#
