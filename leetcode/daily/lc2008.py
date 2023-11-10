#
# @lc app=leetcode.cn id=2008 lang=python3
# @lcpr version=21913
#
# [2008] 出租车的最大盈利
#
# https://leetcode.cn/problems/maximum-earnings-from-taxi/description/
#
# algorithms
# Medium (47.39%)
# Likes:    75
# Dislikes: 0
# Total Accepted:    6.8K
# Total Submissions: 14.4K
# Testcase Example:  '5\n[[2,5,4],[1,5,1]]'
#
# 你驾驶出租车行驶在一条有 n 个地点的路上。这 n 个地点从近到远编号为 1 到 n ，你想要从 1 开到 n
# ，通过接乘客订单盈利。你只能沿着编号递增的方向前进，不能改变方向。
# 
# 乘客信息用一个下标从 0 开始的二维数组 rides 表示，其中 rides[i] = [starti, endi, tipi] 表示第 i
# 位乘客需要从地点 starti 前往 endi ，愿意支付 tipi 元的小费。
# 
# 每一位 你选择接单的乘客 i ，你可以 盈利 endi - starti + tipi 元。你同时 最多 只能接一个订单。
# 
# 给你 n 和 rides ，请你返回在最优接单方案下，你能盈利 最多 多少元。
# 
# 注意：你可以在一个地点放下一位乘客，并在同一个地点接上另一位乘客。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 5, rides = [[2,5,4],[1,5,1]]
# 输出：7
# 解释：我们可以接乘客 0 的订单，获得 5 - 2 + 4 = 7 元。
# 
# 
# 示例 2：
# 
# 输入：n = 20, rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]
# 输出：20
# 解释：我们可以接以下乘客的订单：
# - 将乘客 1 从地点 3 送往地点 10 ，获得 10 - 3 + 2 = 9 元。
# - 将乘客 2 从地点 10 送往地点 12 ，获得 12 - 10 + 3 = 5 元。
# - 将乘客 5 从地点 13 送往地点 18 ，获得 18 - 13 + 1 = 6 元。
# 我们总共获得 9 + 5 + 6 = 20 元。
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10^5
# 1 <= rides.length <= 3 * 10^4
# rides[i].length == 3
# 1 <= starti < endi <= n
# 1 <= tipi <= 10^5
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
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # dp就好了 

        # 按照时间结尾进行分类
        g = defaultdict(list)
        for st, ed, tip in rides:
            g[ed].append((st, tip))

        # dp[i] 表示再路程i之内能获得最大收益 
        dp = [0] * (n + 1) 
        for i in range(n):
            # 当前不载人 
            dp[i + 1] = dp[i]
            for st, tip in g[i + 1]:
                dp[i + 1] = max(dp[i + 1], dp[st] + (i + 1 - st) + tip) 
        return dp[n]
    
    
# @lc code=end



#
# @lcpr case=start
# 5\n[[2,5,4],[1,5,1]]\n
# @lcpr case=end

# @lcpr case=start
# 20\n[[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]\n
# @lcpr case=end

#

