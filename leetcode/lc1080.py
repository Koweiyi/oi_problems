#
# @lc app=leetcode.cn id=1080 lang=python3
# @lcpr version=21913
#
# [1080] 根到叶路径上的不足节点
#
# https://leetcode.cn/problems/insufficient-nodes-in-root-to-leaf-paths/description/
#
# algorithms
# Medium (61.49%)
# Likes:    164
# Dislikes: 0
# Total Accepted:    22.7K
# Total Submissions: 37K
# Testcase Example:  '[1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]\n1'
#
# 给你二叉树的根节点 root 和一个整数 limit ，请你同时删除树中所有 不足节点 ，并返回最终二叉树的根节点。
# 
# 假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为 不足节点 ，需要被删除。
# 
# 叶子节点，就是没有子节点的节点。
# 
# 
# 
# 示例 1：
# 
# 输入：root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
# 输出：[1,2,3,4,null,null,7,8,9,null,14]
# 
# 
# 示例 2：
# 
# 输入：root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
# 输出：[5,4,8,11,null,17,4,7,null,null,null,5]
# 
# 
# 示例 3：
# 
# 输入：root = [1,2,-3,-5,null,4,null], limit = -1
# 输出：[1,null,-3,4]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [1, 5000] 内
# -10^5 <= Node.val <= 10^5
# -10^9 <= limit <= 10^9
# 
# 
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
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(root: Optional[TreeNode], pre_s: int) -> (int, bool):   
            if not root.left and not root.right:
                # print(pre_s, root.val)
                if pre_s + root.val < limit:
                    return root.val, True
                else:
                    return root.val, False 
            sl = sr = -inf
            if root.left:
                sl, dl = dfs(root.left, pre_s + root.val)
                if dl: root.left = None
            if root.right:
                sr, dr = dfs(root.right, pre_s + root.val)
                if dr: root.right = None
            s = max(sl, sr) + root.val
            if s + pre_s < limit:
                return s, True
            return s, False
        s, d = dfs(root, 0)
        # print(s, d)
        return None if d else root 


# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]\n1\n
# @lcpr case=end

# @lcpr case=start
# [2,7,2,null,8,null,null,null,4]\n15\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,17,4,7,1,null,null,5,3]\n22\n
# @lcpr case=end

# @lcpr case=start
# [1,2,-3,-5,null,4,null]\n-1\n
# @lcpr case=end

#

