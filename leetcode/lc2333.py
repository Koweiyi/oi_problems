#
# @lc app=leetcode.cn id=2333 lang=python3
# @lcpr version=21917
#
# [2333] 最小差值平方和
#
# https://leetcode.cn/problems/minimum-sum-of-squared-difference/description/
#
# algorithms
# Medium (26.94%)
# Likes:    37
# Dislikes: 0
# Total Accepted:    5.2K
# Total Submissions: 19.2K
# Testcase Example:  '[1,2,3,4]\n[2,10,20,19]\n0\n0'
#
# 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，长度为 n 。
# 
# 数组 nums1 和 nums2 的 差值平方和 定义为所有满足 0 <= i < n 的 (nums1[i] - nums2[i])^2 之和。
# 
# 同时给你两个正整数 k1 和 k2 。你可以将 nums1 中的任意元素 +1 或者 -1 至多 k1 次。类似的，你可以将 nums2 中的任意元素
# +1 或者 -1 至多 k2 次。
# 
# 请你返回修改数组 nums1 至多 k1 次且修改数组 nums2 至多 k2 次后的最小 差值平方和 。
# 
# 注意：你可以将数组中的元素变成 负 整数。
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
# 输出：579
# 解释：nums1 和 nums2 中的元素不能修改，因为 k1 = 0 和 k2 = 0 。
# 差值平方和为：(1 - 2)^2 + (2 - 10)^2 + (3 - 20)^2 + (4 - 19)^2 = 579 。
# 
# 
# 示例 2：
# 
# 输入：nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
# 输出：43
# 解释：一种得到最小差值平方和的方式为：
# - 将 nums1[0] 增加一次。
# - 将 nums2[2] 增加一次。
# 最小差值平方和为：
# (2 - 5)^2 + (4 - 8)^2 + (10 - 7)^2 + (12 - 9)^2 = 43 。
# 注意，也有其他方式可以得到最小差值平方和，但没有得到比 43 更小答案的方案。
# 
# 
# 
# 提示：
# 
# 
# n == nums1.length == nums2.length
# 1 <= n <= 10^5
# 0 <= nums1[i], nums2[i] <= 10^5
# 0 <= k1, k2 <= 10^9
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
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1) 
        d = [abs(nums1[i] - nums2[i]) for i in range(n)]
        if sum(d) <= k1 + k2 :
            return 0
        d.append(0)
        d.sort(reverse=True) 
        l, r = 0, n 
        ss = list(accumulate(d, initial=0))
        def check(x): 
            return  k1 + k2 >= ss[x] - (x * d[x])
        while l + 1 < r:
            mid = (l + r) // 2 
            if check(mid):
                l = mid
            else:
                r = mid 
        left = (k1 + k2) - (ss[l] - (l * d[l]))
        # print(l, left, d)
        less = left // (l + 1)
        cnt = left % (l + 1)
        return cnt * pow(d[l] - less - 1, 2) + (l - cnt + 1) * pow(d[l] - less, 2) + sum(d[x] ** 2 for x in range(l + 1, n)) 




            

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n[2,10,20,19]\n0\n0\n
# @lcpr case=end

# @lcpr case=start
# [1,4,10,12]\n[5,8,6,9]\n1\n1\n
# @lcpr case=end

# @lcpr case=start
# [7,11,4,19,11,5,6,1,8]\n[4,7,6,16,12,9,10,2,10]\n3\n6\n
# @lcpr case=end

# @lcpr case=start
# [19,18,19,18,18,19,19]\n[1,0,1,0,0,1,1]\n10\n33\n
# @lcpr case=end
#

