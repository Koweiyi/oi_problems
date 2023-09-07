#
# @lc app=leetcode.cn id=1626 lang=python3
# @lcpr version=21913
#
# [1626] 无矛盾的最佳球队
#
# https://leetcode.cn/problems/best-team-with-no-conflicts/description/
#
# algorithms
# Medium (53.65%)
# Likes:    190
# Dislikes: 0
# Total Accepted:    25.4K
# Total Submissions: 47.3K
# Testcase Example:  '[1,3,5,10,15]\n[1,2,3,4,5]'
#
# 假设你是球队的经理。对于即将到来的锦标赛，你想组合一支总体得分最高的球队。球队的得分是球队中所有球员的分数 总和 。
# 
# 然而，球队中的矛盾会限制球员的发挥，所以必须选出一支 没有矛盾 的球队。如果一名年龄较小球员的分数 严格大于
# 一名年龄较大的球员，则存在矛盾。同龄球员之间不会发生矛盾。
# 
# 给你两个列表 scores 和 ages，其中每组 scores[i] 和 ages[i] 表示第 i 名球员的分数和年龄。请你返回
# 所有可能的无矛盾球队中得分最高那支的分数 。
# 
# 
# 
# 示例 1：
# 
# 输入：scores = [1,3,5,10,15], ages = [1,2,3,4,5]
# 输出：34
# 解释：你可以选中所有球员。
# 
# 示例 2：
# 
# 输入：scores = [4,5,6,5], ages = [2,1,2,1]
# 输出：16
# 解释：最佳的选择是后 3 名球员。注意，你可以选中多个同龄球员。
# 
# 
# 示例 3：
# 
# 输入：scores = [1,2,3,5], ages = [8,9,10,1]
# 输出：6
# 解释：最佳的选择是前 3 名球员。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= scores.length, ages.length <= 1000
# scores.length == ages.length
# 1 <= scores[i] <= 10^6
# 1 <= ages[i] <= 1000
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
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        p = [(age, score) for age, score in zip(ages, scores)]
        p.sort()

        n = len(p)
        dp = [0] * n
        res = 0
        for i in range(n):
            dp[i] = p[i][1]
            for j in range(i):
                if p[j][1] <= p[i][1]:
                    dp[i] = max(dp[i], dp[j] + p[i][1])
            res = max(res, dp[i])
        return res  
        
# @lc code=end



#
# @lcpr case=start
# [1,3,5,10,15]\n[1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,5]\n[2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n[8,9,10,1]\n
# @lcpr case=end

#

