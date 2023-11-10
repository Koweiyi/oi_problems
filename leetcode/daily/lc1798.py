#
# @lc app=leetcode.cn id=1798 lang=python3
# @lcpr version=21914
#
# [1798] 你能构造出连续值的最大数目
#
# https://leetcode.cn/problems/maximum-number-of-consecutive-values-you-can-make/description/
#
# algorithms
# Medium (70.94%)
# Likes:    210
# Dislikes: 0
# Total Accepted:    23.2K
# Total Submissions: 32.7K
# Testcase Example:  '[1,3]'
#
# 给你一个长度为 n 的整数数组 coins ，它代表你拥有的 n 个硬币。第 i 个硬币的值为 coins[i]
# 。如果你从这些硬币中选出一部分硬币，它们的和为 x ，那么称，你可以 构造 出 x 。
# 
# 请返回从 0 开始（包括 0 ），你最多能 构造 出多少个连续整数。
# 
# 你可能有多个相同值的硬币。
# 
# 
# 
# 示例 1：
# 
# 输入：coins = [1,3]
# 输出：2
# 解释：你可以得到以下这些值：
# - 0：什么都不取 []
# - 1：取 [1]
# 从 0 开始，你可以构造出 2 个连续整数。
# 
# 示例 2：
# 
# 输入：coins = [1,1,1,4]
# 输出：8
# 解释：你可以得到以下这些值：
# - 0：什么都不取 []
# - 1：取 [1]
# - 2：取 [1,1]
# - 3：取 [1,1,1]
# - 4：取 [4]
# - 5：取 [4,1]
# - 6：取 [4,1,1]
# - 7：取 [4,1,1,1]
# 从 0 开始，你可以构造出 8 个连续整数。
# 
# 示例 3：
# 
# 输入：nums = [1,4,10,3,1]
# 输出：20
# 
# 
# 
# 提示：
# 
# 
# coins.length == n
# 1 <= n <= 4 * 10^4
# 1 <= coins[i] <= 4 * 10^4
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
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        cur = 0 
        for x in coins:
            if x > cur + 1:
                break
            cur = cur + x 
        return cur + 1

# @lc code=end



#
# @lcpr case=start
# [1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,10,3,1]\n
# @lcpr case=end

#

