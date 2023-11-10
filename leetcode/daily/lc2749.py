#
# @lc app=leetcode.cn id=2749 lang=python3
# @lcpr version=21917
#
# [2749] 得到整数零需要执行的最少操作数
#
# https://leetcode.cn/problems/minimum-operations-to-make-the-integer-zero/description/
#
# algorithms
# Medium (32.81%)
# Likes:    17
# Dislikes: 0
# Total Accepted:    3.4K
# Total Submissions: 10.3K
# Testcase Example:  '3\n-2'
#
# 给你两个整数：num1 和 num2 。
# 
# 在一步操作中，你需要从范围 [0, 60] 中选出一个整数 i ，并从 num1 减去 2^i + num2 。
# 
# 请你计算，要想使 num1 等于 0 需要执行的最少操作数，并以整数形式返回。
# 
# 如果无法使 num1 等于 0 ，返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 输入：num1 = 3, num2 = -2
# 输出：3
# 解释：可以执行下述步骤使 3 等于 0 ：
# - 选择 i = 2 ，并从 3 减去 2^2 + (-2) ，num1 = 3 - (4 + (-2)) = 1 。
# - 选择 i = 2 ，并从 1 减去 2^2 + (-2) ，num1 = 1 - (4 + (-2)) = -1 。
# - 选择 i = 0 ，并从 -1 减去 2^0 + (-2) ，num1 = (-1) - (1 + (-2)) = 0 。
# 可以证明 3 是需要执行的最少操作数。
# 
# 
# 示例 2：
# 
# 输入：num1 = 5, num2 = 7
# 输出：-1
# 解释：可以证明，执行操作无法使 5 等于 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= num1 <= 10^9
# -10^9 <= num2 <= 10^9
# 
# 
#
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter
from functools import cache
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if num1 == 0:
            return 0 
        for i in range(35):
            num = num1 - num2 * i 
            if num > 0 and num.bit_count() <= i <= num:
                return i
        return -1
# @lc code=end



#
# @lcpr case=start
# 85\n42\n
# @lcpr case=end

# @lcpr case=start
# 5\n7\n
# @lcpr case=end

#

