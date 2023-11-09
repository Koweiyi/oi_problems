#
# @lc app=leetcode.cn id=971 lang=python3
# @lcpr version=21913
#
# [971] 翻转二叉树以匹配先序遍历
#
# https://leetcode.cn/problems/flip-binary-tree-to-match-preorder-traversal/description/
#
# algorithms
# Medium (45.79%)
# Likes:    112
# Dislikes: 0
# Total Accepted:    10.9K
# Total Submissions: 23.9K
# Testcase Example:  '[1,2]\n[2,1]'
#
# 给你一棵二叉树的根节点 root ，树中有 n 个节点，每个节点都有一个不同于其他节点且处于 1 到 n 之间的值。
# 
# 另给你一个由 n 个值组成的行程序列 voyage ，表示 预期 的二叉树 先序遍历 结果。
# 
# 通过交换节点的左右子树，可以 翻转 该二叉树中的任意节点。例，翻转节点 1 的效果如下：
# 
# 请翻转 最少 的树中节点，使二叉树的 先序遍历 与预期的遍历行程 voyage 相匹配 。 
# 
# 如果可以，则返回 翻转的 所有节点的值的列表。你可以按任何顺序返回答案。如果不能，则返回列表 [-1]。
# 
# 
# 
# 示例 1：
# 
# 输入：root = [1,2], voyage = [2,1]
# 输出：[-1]
# 解释：翻转节点无法令先序遍历匹配预期行程。
# 
# 
# 示例 2：
# 
# 输入：root = [1,2,3], voyage = [1,3,2]
# 输出：[1]
# 解释：交换节点 2 和 3 来翻转节点 1 ，先序遍历可以匹配预期行程。
# 
# 示例 3：
# 
# 输入：root = [1,2,3], voyage = [1,2,3]
# 输出：[]
# 解释：先序遍历已经匹配预期行程，所以不需要翻转节点。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数目为 n
# n == voyage.length
# 1 <= n <= 100
# 1 <= Node.val, voyage[i] <= n
# 树中的所有值 互不相同
# voyage 中的所有值 互不相同
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        mp = {v:i for i, v in enumerate(voyage)}

        res = []
        def dfs(root: Optional[TreeNode], l: int, r: int) -> bool:
            if not root:
                return l > r 
            if l > r:
                return not root 
            if root.val != voyage[l]:
                return False 
            if not root.left or not root.right:
                if not root.left:
                    return dfs(root.right, l + 1, r)
                return dfs(root.left, l + 1, r) 
            if l >= r :
                return False
            if root.left.val == voyage[l + 1]:
                idr = mp[root.right.val]
                return dfs(root.left, l + 1, idr - 1) and dfs(root.right, idr, r)
            res.append(root.val)
            idl = mp[root.left.val]
            return dfs(root.left, idl, r) and dfs(root.right, l + 1, idl - 1)
        return res if dfs(root, 0, len(voyage) - 1) else [-1]
# @lc code=end



#
# @lcpr case=start
# [1,2]\n[2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n[1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n[1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,3,2,1,null,null,null,null,null,null]\n[5,4,1,2,3]\n
# @lcpr case=end
#

