/*
 * @lc app=leetcode.cn id=958 lang=golang
 * @lcpr version=21913
 *
 * [958] 二叉树的完全性检验
 *
 * https://leetcode.cn/problems/check-completeness-of-a-binary-tree/description/
 *
 * algorithms
 * Medium (54.52%)
 * Likes:    264
 * Dislikes: 0
 * Total Accepted:    50.9K
 * Total Submissions: 93.3K
 * Testcase Example:  '[1,2,3,4,5,6]'
 *
 * 给定一个二叉树的 root ，确定它是否是一个 完全二叉树 。
 * 
 * 在一个 完全二叉树 中，除了最后一个关卡外，所有关卡都是完全被填满的，并且最后一个关卡中的所有节点都是尽可能靠左的。它可以包含 1 到 2^h
 * 节点之间的最后一级 h 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 输入：root = [1,2,3,4,5,6]
 * 输出：true
 * 解释：最后一层前的每一层都是满的（即，结点值为 {1} 和 {2,3} 的两层），且最后一层中的所有结点（{4,5,6}）都尽可能地向左。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 
 * 输入：root = [1,2,3,4,5,null,7]
 * 输出：false
 * 解释：值为 7 的结点没有尽可能靠向左侧。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 树的结点数在范围  [1, 100] 内。
 * 1 <= Node.val <= 1000
 * 
 * 
 */
package leetcode
type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
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


func isCompleteTree(root *TreeNode) bool {
	var dfs func(*TreeNode, int) bool 
	n, p := 0, 0
	dfs = func(root *TreeNode, k int) bool {
		if root == nil{
			return true
		}
		if (k > 100){
			return false
		}
		n ++
		p = max(p, k)
		return 	dfs(root.Left, k * 2) && dfs(root.Right, k * 2 + 1)
	}
	if !dfs(root, 1){
		return false
	}
	return n == p
}
func max(a, b int) int {if a > b {return a}; return b}

// @lc code=end



/*
// @lcpr case=start
// [1,2,3,4,5,6]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,null,7]\n
// @lcpr case=end

 */

