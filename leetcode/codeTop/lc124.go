/*
 * @lc app=leetcode.cn id=124 lang=golang
 * @lcpr version=21913
 *
 * [124] 二叉树中的最大路径和
 *
 * https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/
 *
 * algorithms
 * Hard (45.30%)
 * Likes:    2026
 * Dislikes: 0
 * Total Accepted:    337.5K
 * Total Submissions: 744.9K
 * Testcase Example:  '[1,2,3]'
 *
 * 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个
 * 节点，且不一定经过根节点。
 *
 * 路径和 是路径中各节点值的总和。
 *
 * 给你一个二叉树的根节点 root ，返回其 最大路径和 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：root = [1,2,3]
 * 输出：6
 * 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
 *
 * 示例 2：
 *
 * 输入：root = [-10,9,20,null,null,15,7]
 * 输出：42
 * 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点数目范围是 [1, 3 * 10^4]
 * -1000 <= Node.val <= 1000
 *
 *
 */
package leetcode

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}
type ListNode struct {
    Val int
    Next *ListNode
}
// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 // 简单树形dp问题
func maxPathSum(root *TreeNode) int {
	res := root.Val // 因为一定存在root节点，答案不可能小于root.Val
	
	// 定义一个dfs函数，函数返回从node出发向下的最大路径和值
	// 可以简单推导，
	// dfs(root) = max(0, dfs(root.Left) + root.Val, dfs(root.Right) + root.Val)

	var dfs func(node *TreeNode) (mx int)
	dfs = func(node *TreeNode) (mx int) {
		if node == nil{
			return 
		}
		mxl := dfs(node.Left)
		mxr := dfs(node.Right)
		mx = max(mx, max(mxl, mxr) + node.Val)
		res = max(res, mxl + node.Val + mxr)
		return mx 
	}
	dfs(root)
	return res 
}
func max(a, b int) int {if a > b {return a}; return b}

// @lc code=end



/*
// @lcpr case=start
// [1,2,3]\n
// @lcpr case=end

// @lcpr case=start
// [-10,9,20,null,null,15,7]\n
// @lcpr case=end

 */

