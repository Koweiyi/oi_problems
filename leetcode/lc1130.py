#
# @lc app=leetcode.cn id=1130 lang=python3
# @lcpr version=21914
#
# [1130] 叶值的最小代价生成树
#
# https://leetcode.cn/problems/minimum-cost-tree-from-leaf-values/description/
#
# algorithms
# Medium (70.72%)
# Likes:    382
# Dislikes: 0
# Total Accepted:    21.2K
# Total Submissions: 29.9K
# Testcase Example:  '[6,2,4]'
#
# 给你一个正整数数组 arr，考虑所有满足以下条件的二叉树：
# 
# 
# 每个节点都有 0 个或是 2 个子节点。
# 数组 arr 中的值与树的中序遍历中每个叶节点的值一一对应。
# 每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。
# 
# 
# 在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。
# 
# 如果一个节点有 0 个子节点，那么该节点为叶节点。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [6,2,4]
# 输出：32
# 解释：有两种可能的树，第一种的非叶节点的总和为 36 ，第二种非叶节点的总和为 32 。 
# 
# 
# 示例 2：
# 
# 输入：arr = [4,11]
# 输出：44
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= arr.length <= 40
# 1 <= arr[i] <= 15
# 答案保证是一个 32 位带符号整数，即小于 2^31 。
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
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # 区间dp 
        @ cache 
        def dfs(i: int, j: int) -> (int, int):
            if i == j:
                return  0, arr[i] 
            # 枚举划分中点 
            s = inf 
            for k in range(i, j):
                ls, lmx = dfs(i, k)
                rs, rmx = dfs(k + 1, j)
                s = min(s, ls + rs + lmx * rmx)
            return s, max(lmx, rmx)
        return dfs(0, len(arr) - 1)[0]
# @lc code=end



#
# @lcpr case=start
# [6,2,4]\n
# @lcpr case=end

# @lcpr case=start
# [4,11]\n
# @lcpr case=end

#

