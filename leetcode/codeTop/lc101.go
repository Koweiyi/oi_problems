/*
 * @lc app=leetcode.cn id=101 lang=golang
 * @lcpr version=21913
 *
 * [101] 对称二叉树
 *
 * https://leetcode.cn/problems/symmetric-tree/description/
 *
 * algorithms
 * Easy (58.99%)
 * Likes:    2505
 * Dislikes: 0
 * Total Accepted:    877.6K
 * Total Submissions: 1.5M
 * Testcase Example:  '[1,2,2,3,4,4,3]'
 *
 * 给你一个二叉树的根节点 root ， 检查它是否轴对称。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：root = [1,2,2,3,4,4,3]
 * 输出：true
 * 
 * 
 * 示例 2：
 * 
 * 输入：root = [1,2,2,null,3,null,3]
 * 输出：false
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 树中节点数目在范围 [1, 1000] 内
 * -100 <= Node.val <= 100
 * 
 * 
 * 
 * 
 * 进阶：你可以运用递归和迭代两种方法解决这个问题吗？
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
func isSymmetric(root *TreeNode) bool {
	if root == nil{
		return true
	}

	var check func(l, r *TreeNode) bool
	check = func(l, r *TreeNode) bool {
		// 如果都到达空节点， 返回true
		if l == nil && r == nil{
			return true
		}
		// 如果其中一个节点为空， 或者对比的两个节点值不相同 返回false
		if l == nil || r == nil{
			return false
		} 
		if l.Val != r.Val{
			return false
		}

		// 镜像check 对比左节点的左节点和右节点的右节点， 左节点的右节点和右节点的左节点
		return check(l.Left, r.Right) && check(l.Right, r.Left)
	}
	return check(root.Left, root.Right)
}
// @lc code=end



/*
// @lcpr case=start
// [1,2,2,3,4,4,3]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,2,null,3,null,3]\n
// @lcpr case=end

 */

