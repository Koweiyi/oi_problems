#
# @lc app=leetcode.cn id=1696 lang=python3
# @lcpr version=21914
#
# [1696] 跳跃游戏 VI
#
# https://leetcode.cn/problems/jump-game-vi/description/
#
# algorithms
# Medium (40.32%)
# Likes:    133
# Dislikes: 0
# Total Accepted:    13.3K
# Total Submissions: 33.1K
# Testcase Example:  '[1,-1,-2,4,-7,3]\n2'
#
# 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
# 
# 一开始你在下标 0 处。每一步，你最多可以往前跳 k 步，但你不能跳出数组的边界。也就是说，你可以从下标 i 跳到 [i + 1， min(n - 1,
# i + k)] 包含 两个端点的任意位置。
# 
# 你的目标是到达数组最后一个位置（下标为 n - 1 ），你的 得分 为经过的所有数字之和。
# 
# 请你返回你能得到的 最大得分 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,-1,-2,4,-7,3], k = 2
# 输出：7
# 解释：你可以选择子序列 [1,-1,4,3] （上面加粗的数字），和为 7 。
# 
# 
# 示例 2：
# 
# 输入：nums = [10,-5,-2,4,0,3], k = 3
# 输出：17
# 解释：你可以选择子序列 [10,4,3] （上面加粗数字），和为 17 。
# 
# 
# 示例 3：
# 
# 输入：nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length, k <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#
from collections import Counter, defaultdict, deque
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
    def maxResult(self, nums: List[int], k:int) -> int:
        # 维护一个单调队列(递减)

        # 单调队列优化dp 
        # FIXED 好像有问题 吃完改
        n = len(nums)
        dq = deque([0])
        for i in range(1, n):
            while dq and i - dq[0] > k:
                dq.popleft()
            nums[i] += nums[dq[0]] 
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        return nums[n - 1]
                 

        
# @lc code=end



#
# @lcpr case=start
# [1,-1,-2,4,-7,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [10,-5,-2,4,0,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,-5,-20,4,-1,3,-6,-3]\n2\n
# @lcpr case=end


# @lcpr case=start
# [100,-1,-100,-1,100]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,-1,-2,-3,1]\n2\n

# @lcpr case=end
#

