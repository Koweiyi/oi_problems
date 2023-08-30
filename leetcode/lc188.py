#
# @lc app=leetcode.cn id=188 lang=python3
# @lcpr version=21913
#
# [188] 买卖股票的最佳时机 IV
#
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (46.27%)
# Likes:    1009
# Dislikes: 0
# Total Accepted:    202.1K
# Total Submissions: 436.6K
# Testcase Example:  '2\n[2,4,1]'
#
# 给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。
# 
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 
# 
# 示例 1：
# 
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 
# 示例 2：
# 
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
# ⁠    随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3
# 。
# 
# 
# 
# 提示：
# 
# 
# 1 <= k <= 100
# 1 <= prices.length <= 1000
# 0 <= prices[i] <= 1000
# 
# 
#
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter, defaultdict
from functools import cache
from sortedcontainers import SortedList
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dfs(i: int, k: int, have: bool) -> int :
            if i == 0:
                if k == 0 and not have:
                    return 0 
                return -inf
            res = dfs(i - 1, k, have)
            if have:
                res = max(res, dfs(i - 1, k, not have) - prices[i - 1])
            else:
                if k > 0:
                    res = max(res, dfs(i - 1, k - 1, not have) + prices[i - 1]) 
            return res 
        return max(dfs(len(prices), j, False) for j in range(k + 1))

# @lc code=end



#
# @lcpr case=start
# 2\n[2,4,1]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[3,2,6,5,0,3]\n
# @lcpr case=end

#

