#
# @lc app=leetcode.cn id=1073 lang=python3
# @lcpr version=21913
#
# [1073] 负二进制数相加
#
# https://leetcode.cn/problems/adding-two-negabinary-numbers/description/
#
# algorithms
# Medium (41.60%)
# Likes:    123
# Dislikes: 0
# Total Accepted:    16.5K
# Total Submissions: 39.8K
# Testcase Example:  '[1,1,1,1,1]\n[1,0,1]'
#
# 给出基数为 -2 的两个数 arr1 和 arr2，返回两数相加的结果。
# 
# 数字以 数组形式 给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如，arr = [1,1,0,1] 表示数字 (-2)^3 +
# (-2)^2 + (-2)^0 = -3。数组形式 中的数字 arr 也同样不含前导零：即 arr == [0] 或 arr[0] == 1。
# 
# 返回相同表示形式的 arr1 和 arr2 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组。
# 
# 
# 
# 示例 1：
# 
# 输入：arr1 = [1,1,1,1,1], arr2 = [1,0,1]
# 输出：[1,0,0,0,0]
# 解释：arr1 表示 11，arr2 表示 5，输出表示 16 。
# 
# 
# 
# 
# 示例 2：
# 
# 输入：arr1 = [0], arr2 = [0]
# 输出：[0]
# 
# 
# 示例 3：
# 
# 输入：arr1 = [0], arr2 = [1]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 
# 1 <= arr1.length, arr2.length <= 1000
# arr1[i] 和 arr2[i] 都是 0 或 1
# arr1 和 arr2 都没有前导0
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
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j =  len(arr1) - 1, len(arr2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry != 0:
            a = arr1[i] if i >= 0 else 0 
            b = arr2[j] if j >= 0 else 0
            s = a + b + carry
            carry = 0 
            if s >= 2:
                s -= 2 
                carry -= 1
            elif s == -1:
                s += 2 
                carry += 1 
            res.append(s)
            i -= 1
            j -= 1
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return res[::-1]
# @lc code=end



#
# @lcpr case=start
# [1,1,1,1,1]\n[1,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n[1,1]\n
# @lcpr case=end
#

