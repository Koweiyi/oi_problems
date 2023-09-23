#
# @lc app=leetcode.cn id=LCP 67 lang=python3
# @lcpr version=21913
#
# [LCP 67] 装饰树
#
# https://leetcode.cn/problems/KnLfVT/description/
#
# algorithms
# Medium (87.76%)
# Likes:    10
# Dislikes: 0
# Total Accepted:    5.8K
# Total Submissions: 6.6K
# Testcase Example:  '[7,5,6]'
#
# 力扣嘉年华上的 DIY 手工展位准备了一棵缩小版的 **二叉** 装饰树 `root` 和灯饰，你需要将灯饰逐一插入装饰树中，要求如下：
# 
# - 完成装饰的二叉树根结点与 `root` 的根结点值相同
# - 若一个节点拥有父节点，则在该节点和他的父节点之间插入一个灯饰（即插入一个值为 `-1` 的节点）。具体地：
# ⁠   - 在一个 父节点 x 与其左子节点 y 之间添加 -1 节点， 节点 -1、节点 y 为各自父节点的左子节点，
# ⁠   - 在一个 父节点 x 与其右子节点 y 之间添加 -1 节点， 节点 -1、节点 y 为各自父节点的右子节点，
# ⁠   
# 现给定二叉树的根节点 `root` ，请返回完成装饰后的树的根节点。
# **示例 1：**
# >输入：
# >`root = [7,5,6]`
# >
# >输出：`[7,-1,-1,5,null,null,6]`
# >
# >解释：如下图所示，
# 
# >![image.png](https://pic.leetcode-cn.com/1663575757-yRLGaq-image.png){:width=400px}
# 
# **示例 2：**
# >输入：
# >`root = [3,1,7,3,8,null,4]`
# >
# >输出：`[3,-1,-1,1,null,null,7,-1,-1,null,-1,3,null,null,8,null,4]`
# >
# >解释：如下图所示
# 
# ![image.png](https://pic.leetcode-cn.com/1663577920-sjrAYH-image.png){:width=500px}
# 
# **提示：**
# >`0 <= root.Val <= 1000`
# >`root` 节点数量范围为 `[1, 10^5]`
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
# @lc code=end



#
# @lcpr case=start
# [7,5,6]`>\n
# @lcpr case=end

# @lcpr case=start
# [3,1,7,3,8,null,4]`>\n
# @lcpr case=end

#

