#
# @lc app=leetcode.cn id=1497 lang=python3
# @lcpr version=21913
#
# [1497] 检查数组对是否可以被 k 整除
#
# https://leetcode.cn/problems/check-if-array-pairs-are-divisible-by-k/description/
#
# algorithms
# Medium (40.22%)
# Likes:    79
# Dislikes: 0
# Total Accepted:    13.4K
# Total Submissions: 33.3K
# Testcase Example:  '[1,2,3,4,5,10,6,7,8,9]\n5'
#
# 给你一个整数数组 arr 和一个整数 k ，其中数组长度是偶数，值为 n 。
# 
# 现在需要把数组恰好分成 n / 2 对，以使每对数字的和都能够被 k 整除。
# 
# 如果存在这样的分法，请返回 True ；否则，返回 False 。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# 输出：true
# 解释：划分后的数字对为 (1,9),(2,8),(3,7),(4,6) 以及 (5,10) 。
# 
# 
# 示例 2：
# 
# 输入：arr = [1,2,3,4,5,6], k = 7
# 输出：true
# 解释：划分后的数字对为 (1,6),(2,5) 以及 (3,4) 。
# 
# 
# 示例 3：
# 
# 输入：arr = [1,2,3,4,5,6], k = 10
# 输出：false
# 解释：无法在将数组中的数字分为三对的同时满足每对数字和能够被 10 整除的条件。
# 
# 
# 
# 
# 提示：
# 
# 
# arr.length == n
# 1 <= n <= 10^5
# n 为偶数
# -10^9 <= arr[i] <= 10^9
# 1 <= k <= 10^5
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
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = Counter()
        for x in arr:
            cnt[x % k] += 1 
        if cnt[0] & 1 or k & 1 == 0 and cnt[k // 2] & 1:
            return False
        for i in range(1, k // 2 + 1):
            if cnt[i] != cnt[k - i]:
                return False
        return True
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,10,6,7,8,9]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6]\n7\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6]\n10\n
# @lcpr case=end

#

