#
# @lc app=leetcode.cn id=1043 lang=python3
# @lcpr version=21913
#
# [1043] 分隔数组以得到最大和
#
# https://leetcode.cn/problems/partition-array-for-maximum-sum/description/
#
# algorithms
# Medium (75.49%)
# Likes:    272
# Dislikes: 0
# Total Accepted:    31.5K
# Total Submissions: 41.8K
# Testcase Example:  '[1,15,7,9,2,5,10]\n3'
#
# 给你一个整数数组 arr，请你将该数组分隔为长度 最多 为 k 的一些（连续）子数组。分隔完成后，每个子数组的中的所有值都会变为该子数组中的最大值。
# 
# 返回将数组分隔变换后能够得到的元素最大和。本题所用到的测试用例会确保答案是一个 32 位整数。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [1,15,7,9,2,5,10], k = 3
# 输出：84
# 解释：数组变为 [15,15,15,9,10,10,10]
# 
# 示例 2：
# 
# 输入：arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
# 输出：83
# 
# 
# 示例 3：
# 
# 输入：arr = [1], k = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 500
# 0 <= arr[i] <= 10^9
# 1 <= k <= arr.length
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
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @cache 
        def dfs(i: int)-> int:
            res = mx = 0
            for j in range(i, max(i - k, -1), -1):
                mx = max(mx, arr[j])
                res = max(res, dfs(j - 1) + mx * (i - j + 1)) 
            return res 
        return dfs(len(arr) - 1)
# @lc code=end



#
# @lcpr case=start
# [1,15,7,9,2,5,10]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,4,1,5,7,3,6,1,9,9,3]\n4\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

