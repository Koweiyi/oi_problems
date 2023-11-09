#
# @lc app=leetcode.cn id=813 lang=python3
# @lcpr version=21914
#
# [813] 最大平均值和的分组
#
# https://leetcode.cn/problems/largest-sum-of-averages/description/
#
# algorithms
# Medium (61.75%)
# Likes:    403
# Dislikes: 0
# Total Accepted:    28.5K
# Total Submissions: 46.2K
# Testcase Example:  '[9,1,2,3,9]\n3'
#
# 给定数组 nums 和一个整数 k 。我们将给定的数组 nums 分成 最多 k 个非空子数组，且数组内部是连续的 。 分数
# 由每个子数组内的平均值的总和构成。
# 
# 注意我们必须使用 nums 数组中的每一个数进行分组，并且分数不一定需要是整数。
# 
# 返回我们所能得到的最大 分数 是多少。答案误差在 10^-6 内被视为是正确的。
# 
# 
# 
# 示例 1:
# 
# 输入: nums = [9,1,2,3,9], k = 3
# 输出: 20.00000
# 解释: 
# nums 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20. 
# 我们也可以把 nums 分成[9, 1], [2], [3, 9]. 
# 这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.
# 
# 
# 示例 2:
# 
# 输入: nums = [1,2,3,4,5,6,7], k = 4
# 输出: 20.50000
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 10^4
# 1 <= k <= nums.length
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
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        if k >= len(nums):
            return sum(nums)
        # 区间dp 
        s = list(accumulate(nums, initial=0))
        @cache
        def dfs(i: int, j: int, cnt: int) -> float:
            if cnt >= (j - i + 1):
                return s[j + 1] - s[i] 
            if cnt == 1:
                return (s[j + 1] - s[i]) / (j - i + 1) 
            res = -1 
            for z in range(i, j + 1):
                res = max(res, (s[z + 1] - s[i]) / (z - i + 1) + dfs(z + 1, j, cnt - 1))
            return res 
        return dfs(0, len(nums) - 1, k)

        
# @lc code=end



# @lcpr case=start
# [2561,9087,398,8137,7838,7669,8731,2460,1166,619]\n3\n
# @lcpr case=end
    

#
# @lcpr case=start
# [9,1,2,3,9]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6,7]\n4\n
# @lcpr case=end

# @lcpr case=start
# [4,1,7,5,6,2,3]\n4\n
# @lcpr case=end
# @lcpr case=start
# [3324,8299,5545,6172,5817]\n2\n
# @lcpr case=end

#


