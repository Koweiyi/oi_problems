#
# @lc app=leetcode.cn id=1658 lang=python3
# @lcpr version=21913
#
# [1658] 将 x 减到 0 的最小操作数
#
# https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/description/
#
# algorithms
# Medium (39.27%)
# Likes:    301
# Dislikes: 0
# Total Accepted:    40.2K
# Total Submissions: 102.5K
# Testcase Example:  '[1,1,4,2,3]\n5'
#
# 给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要
# 修改 数组以供接下来的操作使用。
# 
# 如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,1,4,2,3], x = 5
# 输出：2
# 解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
# 
# 
# 示例 2：
# 
# 输入：nums = [5,6,7,8,9], x = 4
# 输出：-1
# 
# 
# 示例 3：
# 
# 输入：nums = [3,2,20,1,1,3], x = 10
# 输出：5
# 解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 1 <= x <= 10^9
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
    def minOperations(self, nums: List[int], x: int) -> int:
        # 有点类似于后缀的前缀匹配
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        j = bisect_left(s, x)
        if j >= len(s) :
            return -1
        res = j if s[j] == x else inf 
        suf = 0 
        for i in range(n - 1, -1, -1):
            suf += nums[i]
            j = bisect_left(s, x - suf)
            if s[j] == x - suf:
                res = min(res, j + len(nums) - i)
        return res if res != inf else -1 
            



# @lc code=end



#
# @lcpr case=start
# [1,1,4,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [5,6,7,8,9]\n4\n
# @lcpr case=end

# @lcpr case=start
# [3,2,20,1,1,3]\n10\n
# @lcpr case=end

#

