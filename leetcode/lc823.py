#
# @lc app=leetcode.cn id=823 lang=python3
# @lcpr version=21913
#
# [823] 带因子的二叉树
#
# https://leetcode.cn/problems/binary-trees-with-factors/description/
#
# algorithms
# Medium (43.55%)
# Likes:    107
# Dislikes: 0
# Total Accepted:    7K
# Total Submissions: 15.5K
# Testcase Example:  '[2,4]'
#
# 给出一个含有不重复整数元素的数组 arr ，每个整数 arr[i] 均大于 1。
# 
# 用这些整数来构建二叉树，每个整数可以使用任意次数。其中：每个非叶结点的值应等于它的两个子结点的值的乘积。
# 
# 满足条件的二叉树一共有多少个？答案可能很大，返回 对 10^9 + 7 取余 的结果。
# 
# 
# 
# 示例 1:
# 
# 输入: arr = [2, 4]
# 输出: 3
# 解释: 可以得到这些二叉树: [2], [4], [4, 2, 2]
# 
# 示例 2:
# 
# 输入: arr = [2, 4, 5, 10]
# 输出: 7
# 解释: 可以得到这些二叉树: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 1000
# 2 <= arr[i] <= 10^9
# arr 中的所有值 互不相同
# 
# 
#
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter
from functools import cache
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
mod = 10 ** 9 + 7
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = [1] * len(arr)
        for i in range(1,len(arr)):
            l, r = 0, i - 1
            while l < r:
                if arr[l] * arr[r] == arr[i]:
                    dp[i] = (dp[i] + 2 * dp[l] * dp[r]) % mod
                    l += 1
                    r -= 1
                elif arr[l] * arr[r] > arr[i]:
                    r -= 1
                else :
                    l += 1
            if arr[l] * arr[l] == arr[i]:
                dp[i] = (dp[i] + dp[l] * dp[l]) % mod
        return sum(dp) % mod



# @lc code=end



#
# @lcpr case=start
# [2, 4]\n
# @lcpr case=end

# @lcpr case=start
# [2, 4, 5, 10]\n
# @lcpr case=end

#

