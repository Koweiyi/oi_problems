#
# @lc app=leetcode.cn id=2059 lang=python3
# @lcpr version=21801
#
# [2059] 转化数字的最小运算数
#
# https://leetcode.cn/problems/minimum-operations-to-convert-number/description/
#
# algorithms
# Medium (48.26%)
# Likes:    48
# Dislikes: 0
# Total Accepted:    7.2K
# Total Submissions: 15K
# Testcase Example:  '[2,4,12]\n2\n12'
#
# 给你一个下标从 0 开始的整数数组 nums ，该数组由 互不相同 的数字组成。另给你两个整数 start 和 goal 。
# 
# 整数 x 的值最开始设为 start ，你打算执行一些运算使 x 转化为 goal 。你可以对数字 x 重复执行下述运算：
# 
# 如果 0 <= x <= 1000 ，那么，对于数组中的任一下标 i（0 <= i < nums.length），可以将 x 设为下述任一值：
# 
# 
# x + nums[i]
# x - nums[i]
# x ^ nums[i]（按位异或 XOR）
# 
# 
# 注意，你可以按任意顺序使用每个 nums[i] 任意次。使 x 越过 0 <= x <= 1000
# 范围的运算同样可以生效，但该该运算执行后将不能执行其他运算。
# 
# 返回将 x = start 转化为 goal 的最小操作数；如果无法完成转化，则返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [2,4,12], start = 2, goal = 12
# 输出：2
# 解释：
# 可以按 2 → 14 → 12 的转化路径进行，只需执行下述 2 次运算：
# - 2 + 12 = 14
# - 14 - 2 = 12
# 
# 
# 示例 2：
# 
# 输入：nums = [3,5,7], start = 0, goal = -4
# 输出：2
# 解释：
# 可以按 0 → 3 → -4 的转化路径进行，只需执行下述 2 次运算：
# - 0 + 3 = 3
# - 3 - 7 = -4
# 注意，最后一步运算使 x 超过范围 0 <= x <= 1000 ，但该运算仍然可以生效。
# 
# 
# 示例 3：
# 
# 输入：nums = [2,8,16], start = 0, goal = 1
# 输出：-1
# 解释：
# 无法将 0 转化为 1
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 1000
# -10^9 <= nums[i], goal <= 10^9
# 0 <= start <= 1000
# start != goal
# nums 中的所有整数互不相同
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
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        s = set()
        q = [start]
        res = 0 
        while q:
            tmp = q
            q = []
            for x in tmp:
                if x == goal:
                    return res 
                if 0 <= x <= 1000:
                    for y in nums:
                        if x + y not in s:
                            s.add(x + y)
                            q.append(x + y)
                        if x - y not in s:
                            s.add(x - y)
                            q.append(x - y) 
                        if x ^ y not in s:
                            s.add(x ^ y)
                            q.append(x ^ y)
            res += 1
        return -1

# @lc code=end

# @lcpr-div-debug-arg-start
# funName=
# paramTypes= []
# returnType=
# @lcpr-div-debug-arg-end


#
# @lcpr case=start
# [2,4,12]\n2\n12\n
# @lcpr case=end

# @lcpr case=start
# [3,5,7]\n0\n-4\n
# @lcpr case=end

# @lcpr case=start
# [2,8,16]\n0\n1\n
# @lcpr case=end

#


