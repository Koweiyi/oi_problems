#
# @lc app=leetcode.cn id=2096 lang=python3
# @lcpr version=21913
#
# [2096] 从二叉树一个节点到另一个节点每一步的方向
#
# https://leetcode.cn/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/
#
# algorithms
# Medium (44.66%)
# Likes:    67
# Dislikes: 0
# Total Accepted:    8.1K
# Total Submissions: 18.1K
# Testcase Example:  '[5,1,2,3,null,6,4]\n3\n6'
#
# 给你一棵 二叉树 的根节点 root ，这棵二叉树总共有 n 个节点。每个节点的值为 1 到 n 中的一个整数，且互不相同。给你一个整数
# startValue ，表示起点节点 s 的值，和另一个不同的整数 destValue ，表示终点节点 t 的值。
#
# 请找到从节点 s 到节点 t 的 最短路径 ，并以字符串的形式返回每一步的方向。每一步用 大写 字母 'L' ，'R' 和 'U'
# 分别表示一种方向：
#
#
# 'L' 表示从一个节点前往它的 左孩子 节点。
# 'R' 表示从一个节点前往它的 右孩子 节点。
# 'U' 表示从一个节点前往它的 父 节点。
#
#
# 请你返回从 s 到 t 最短路径 每一步的方向。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
# 输出："UURL"
# 解释：最短路径为：3 → 1 → 5 → 2 → 6 。
#
#
# 示例 2：
#
#
#
# 输入：root = [2,1], startValue = 2, destValue = 1
# 输出："L"
# 解释：最短路径为：2 → 1 。
#
#
#
#
# 提示：
#
#
# 树中节点数目为 n 。
# 2 <= n <= 10^5
# 1 <= Node.val <= n
# 树中所有节点的值 互不相同 。
# 1 <= startValue, destValue <= n
# startValue != destValue
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
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        pa = {root: None}
        st = None

        def dfs(root: Optional[TreeNode]):
            nonlocal st
            if not root:
                return
            if root.val == startValue:
                st = root
            if root.left:
                pa[root.left] = root
            if root.right:
                pa[root.right] = root
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        s = set([None])
        res = ""
        path = []

        def dfs2(node: Optional[TreeNode]):
            nonlocal res
            if not node:
                return
            if node.val == destValue:
                res = "".join(path)
                return
            for d, x in zip("ULR", [pa[node], node.left, node.right]):
                if x not in s:
                    s.add(x)
                    path.append(d)
                    dfs2(x)
                    path.pop()
                    s.remove(x)

        s.add(st)
        dfs2(st)
        return res


# @lc code=end


#
# @lcpr case=start
# [5,1,2,3,null,6,4]\n3\n6\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n1\n
# @lcpr case=end

#
