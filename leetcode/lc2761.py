#
# @lc app=leetcode.cn id=2761 lang=python3
# @lcpr version=21909
#
# [2761] 和等于目标值的质数对
#
# https://leetcode.cn/problems/prime-pairs-with-target-sum/description/
#
# algorithms
# Medium (34.13%)
# Likes:    4
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 14.5K
# Testcase Example:  '10'
#
# 给你一个整数 n 。如果两个整数 x 和 y 满足下述条件，则认为二者形成一个质数对：
# 
# 
# 1 <= x <= y <= n
# x + y == n
# x 和 y 都是质数
# 
# 
# 请你以二维有序列表的形式返回符合题目要求的所有 [xi, yi] ，列表需要按 xi 的 非递减顺序
# 排序。如果不存在符合要求的质数对，则返回一个空数组。
# 
# 注意：质数是大于 1 的自然数，并且只有两个因子，即它本身和 1 。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 10
# 输出：[[3,7],[5,5]]
# 解释：在这个例子中，存在满足条件的两个质数对。 
# 这两个质数对分别是 [3,7] 和 [5,5]，按照题面描述中的方式排序后返回。
# 
# 
# 示例 2：
# 
# 输入：n = 2
# 输出：[]
# 解释：可以证明不存在和为 2 的质数对，所以返回一个空数组。 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10^6
# 
# 
#
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
MX = 10 ** 6 + 5
primes = []
is_primes = [True] * MX 
for i in range(2, MX):
    if is_primes[i]:
        primes.append(i)
        for j in range(i * i, MX, i):
            is_primes[j] = False

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        res = []
        for x in primes:
            y = n - x
            if y < x:break
            if is_primes[y]:
                res.append([x, y])
        return res
# @lc code=end



#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#

