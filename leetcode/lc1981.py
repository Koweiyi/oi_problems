#
# @lc app=leetcode.cn id=1981 lang=python3
# @lcpr version=21917
#
# [1981] 最小化目标值与所选元素的差
#
# https://leetcode.cn/problems/minimize-the-difference-between-target-and-chosen-elements/description/
#
# algorithms
# Medium (33.43%)
# Likes:    63
# Dislikes: 0
# Total Accepted:    7.6K
# Total Submissions: 22.7K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]\n13'
#
# 给你一个大小为 m x n 的整数矩阵 mat 和一个整数 target 。
# 
# 从矩阵的 每一行 中选择一个整数，你的目标是 最小化 所有选中元素之 和 与目标值 target 的 绝对差 。
# 
# 返回 最小的绝对差 。
# 
# a 和 b 两数字的 绝对差 是 a - b 的绝对值。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13
# 输出：0
# 解释：一种可能的最优选择方案是：
# - 第一行选出 1
# - 第二行选出 5
# - 第三行选出 7
# 所选元素的和是 13 ，等于目标值，所以绝对差是 0 。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：mat = [[1],[2],[3]], target = 100
# 输出：94
# 解释：唯一一种选择方案是：
# - 第一行选出 1
# - 第二行选出 2
# - 第三行选出 3
# 所选元素的和是 6 ，绝对差是 94 。
# 
# 
# 示例 3：
# 
# 
# 
# 输入：mat = [[1,2,9,8,7]], target = 6
# 输出：1
# 解释：最优的选择方案是选出第一行的 7 。
# 绝对差是 1 。
# 
# 
# 
# 
# 提示：
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 70
# 1 <= mat[i][j] <= 70
# 1 <= target <= 800
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
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # 取出的和值范围在 [m, m * 70] 
        # 枚举值 判断是否能取到 
        n = len(mat) 
        for m in mat:
            m.sort() 
        mn = sum(x[0] for x in mat)
        mx = sum(x[-1] for x in mat) 
        if mn >= target:
            return mn - target
        if mx <= target:
            return target - mx  
        mx = 2 * target + 5 
        dp = [[False] * (mx + 1) for _ in range(n + 1)] 
        dp[0][0] = True  
        for i in range(n):
            for j in range(mx + 1):
                for x in mat[i]:
                    if x <= j:
                        dp[i + 1][j] |= dp[i][j - x]
                    else:
                        break 
                    if dp[i + 1][j]:
                        break
        res = inf 
        for j in range(mx + 1):
            if dp[n][j]:
                res = min(res, abs(target - j))
                if j >= target:
                    break 
        return res 
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n13\n
# @lcpr case=end

# @lcpr case=start
# [[1],[2],[3]]\n100\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,9,8,7]]\n6\n
# @lcpr case=end

#

