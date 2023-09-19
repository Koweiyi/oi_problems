#
# @lc app=leetcode.cn id=2654 lang=python3
# @lcpr version=21914
#
# [2654] 使数组所有元素变成 1 的最少操作次数
#
# https://leetcode.cn/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/description/
#
# algorithms
# Medium (40.36%)
# Likes:    25
# Dislikes: 0
# Total Accepted:    3.6K
# Total Submissions: 9K
# Testcase Example:  '[2,6,3,4]'
#
# 给你一个下标从 0 开始的 正 整数数组 nums 。你可以对数组执行以下操作 任意 次：
# 
# 
# 选择一个满足 0 <= i < n - 1 的下标 i ，将 nums[i] 或者 nums[i+1] 两者之一替换成它们的最大公约数。
# 
# 
# 请你返回使数组 nums 中所有元素都等于 1 的 最少 操作次数。如果无法让数组全部变成 1 ，请你返回 -1 。
# 
# 两个正整数的最大公约数指的是能整除这两个数的最大正整数。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [2,6,3,4]
# 输出：4
# 解释：我们可以执行以下操作：
# - 选择下标 i = 2 ，将 nums[2] 替换为 gcd(3,4) = 1 ，得到 nums = [2,6,1,4] 。
# - 选择下标 i = 1 ，将 nums[1] 替换为 gcd(6,1) = 1 ，得到 nums = [2,1,1,4] 。
# - 选择下标 i = 0 ，将 nums[0] 替换为 gcd(2,1) = 1 ，得到 nums = [1,1,1,4] 。
# - 选择下标 i = 2 ，将 nums[3] 替换为 gcd(1,4) = 1 ，得到 nums = [1,1,1,1] 。
# 
# 
# 示例 2：
# 
# 输入：nums = [2,10,6,14]
# 输出：-1
# 解释：无法将所有元素都变成 1 。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= nums.length <= 50
# 1 <= nums[i] <= 10^6
# 
# 
#
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from itertools import accumulate
from functools import cache
from math import gcd, isqrt
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
    def minOperations(self, nums: List[int]) -> int:
        # 质因数分解 
        # 如果 所有数字都有相同质因数那么返回 -1 
        # 否则返回最快变1操作数 + (len(num1) - 1)

        # 我以为随便选两个数，，，，绷不住了 
        # 
        n = len(nums)
        # def divx(x: int) -> List[int]:
        #     dx = []
        #     for i in range(2, isqrt(x) + 1):
        #         if x % i == 0:
        #             dx.append(i)
        #             while x % i == 0:
        #                 x //= i 
        #     if x > 1:
        #         dx.append(x)
        #     return dx
                
        # res = inf 
        # for x in nums:
        #     d = divx(x)
        #     dp = [[inf] * (1 << len(d)) for _ in range(n + 1)]
        #     for i in range(n + 1):
        #         dp[i][0] = 0
        #     for i in range(n):
        #         m = 0
        #         for k, y in enumerate(d):
        #             if nums[i] % y == 0:
        #                 m |= (1 << k) 
        #         for j in range(1 << (len(d))):
        #             dp[i + 1][j] = min(dp[i][j], dp[i][j&m] + 1)
        #     if dp[-1][- 1] == inf:
        #         return -1 
        #     res = min(res, dp[-1][-1] + (n - 1)) 
        #     print(dp)
        # return res if res != inf else -1 
        cnt = sum(x == 1 for x in nums)
        if cnt:
            return n - cnt 
        
        res = inf
        for i in range(n):
            g = nums[i]
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    res = min((j - i) + (n - 1), res)
        return res if res != inf else -1 
    



# @lc code=end



#
# @lcpr case=start
# [4, 2, 6, 3]\n
# @lcpr case=end

# @lcpr case=start
# [2,10,6,14]\n
# @lcpr case=end

# @lcpr case=start
# [410193,229980,600441]
# @lcpr case=end

#

