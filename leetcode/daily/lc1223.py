#
# @lc app=leetcode.cn id=1223 lang=python3
# @lcpr version=21917
#
# [1223] 掷骰子模拟
#
# https://leetcode.cn/problems/dice-roll-simulation/description/
#
# algorithms
# Hard (61.93%)
# Likes:    217
# Dislikes: 0
# Total Accepted:    18K
# Total Submissions: 29K
# Testcase Example:  '2\n[1,1,2,2,2,3]'
#
# 有一个骰子模拟器会每次投掷的时候生成一个 1 到 6 的随机数。
#
# 不过我们在使用它时有个约束，就是使得投掷骰子时，连续 掷出数字 i 的次数不能超过 rollMax[i]（i 从 1 开始编号）。
#
# 现在，给你一个整数数组 rollMax 和一个整数 n，请你来计算掷 n 次骰子可得到的不同点数序列的数量。
#
# 假如两个序列中至少存在一个元素不同，就认为这两个序列是不同的。由于答案可能很大，所以请返回 模 10^9 + 7 之后的结果。
#
#
#
# 示例 1：
#
# 输入：n = 2, rollMax = [1,1,2,2,2,3]
# 输出：34
# 解释：我们掷 2 次骰子，如果没有约束的话，共有 6 * 6 = 36 种可能的组合。但是根据 rollMax 数组，数字 1 和 2
# 最多连续出现一次，所以不会出现序列 (1,1) 和 (2,2)。因此，最终答案是 36-2 = 34。
#
#
# 示例 2：
#
# 输入：n = 2, rollMax = [1,1,1,1,1,1]
# 输出：30
#
#
# 示例 3：
#
# 输入：n = 3, rollMax = [1,1,1,2,2,3]
# 输出：181
#
#
#
#
# 提示：
#
#
# 1 <= n <= 5000
# rollMax.length == 6
# 1 <= rollMax[i] <= 15
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
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10 ** 9 + 7
        dp = [[[0] * rollMax[i] for i in range(6)] for _ in range(n)]
        for i in range(6):
            dp[0][i][0] = 1
        tot = 6
        for i in range(1, n):
            cur = 0
            for j in range(6):
                for k in range(rollMax[j]):
                    if k == 0:
                        dp[i][j][k] = tot - sum(dp[i - 1][j])
                    else:
                        dp[i][j][k] = dp[i - 1][j][k - 1]
                    cur += dp[i][j][k]
            tot = cur
        return tot % mod

# @lc code=end


#
# @lcpr case=start
# 2\n[1,1,2,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[1,1,1,1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[1,1,1,2,2,3]\n
# @lcpr case=end

#
