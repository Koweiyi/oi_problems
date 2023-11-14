/*
 * @lc app=leetcode.cn id=1382 lang=golang
 * @lcpr version=30109
 *
 * [1382] 将二叉搜索树变平衡
 *
 * https://leetcode.cn/problems/balance-a-binary-search-tree/description/
 *
 * algorithms
 * Medium (73.83%)
 * Likes:    191
 * Dislikes: 0
 * Total Accepted:    26.3K
 * Total Submissions: 35.6K
 * Testcase Example:  '[1,null,2,null,3,null,4]'
 *
 * 给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。如果有多种构造方法，请你返回任意一种。
 *
 * 如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：root = [1,null,2,null,3,null,4,null,null]
 * 输出：[2,1,3,null,null,null,4]
 * 解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。
 *
 *
 * 示例 2：
 *
 *
 *
 * 输入: root = [2,1,3]
 * 输出: [2,1,3]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树节点的数目在 [1, 10^4] 范围内。
 * 1 <= Node.val <= 10^5
 *
 *
 */

// @lcpr-template-start
package leetcode


type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
type ListNode struct {
	Val  int
	Next *ListNode
}

// @lcpr-template-end
// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func balanceBST(root *TreeNode) *TreeNode {
	// AVL 
	// 中序遍历生成有序数组 ，然后进行构造 
	var inorder func(root *TreeNode) []int 
	inorder = func (root *TreeNode) []int {
		if root == nil {
			return []int{}
		}
		res := []int{}
		left := inorder(root.Left)
		res = append(res, left...)
		res = append(res, root.Val)
		right := inorder(root.Right)
		res = append(res, right...)
		return res 
	}
	arr := inorder(root) 
	// fmt.Println(arr)
	var build func(nums []int) *TreeNode 
	build = func(nums []int) *TreeNode{
		if len(nums) == 0 {
			return nil 
		}
		mid := len(nums) / 2 
		root := &TreeNode{Val: nums[mid], Left: build(nums[:mid]), Right: build(nums[mid + 1:])}
		return root
	} 
	return build(arr)
}


// @lc code=end

/*
// @lcpr case=start
// [1,null,2,null,3,null,4,null,null]\n
// @lcpr case=end

// @lcpr case=start
// [2,1,3]\n
// @lcpr case=end

*/
