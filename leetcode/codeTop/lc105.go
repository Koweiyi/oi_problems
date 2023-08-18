/*
 * @lc app=leetcode.cn id=105 lang=golang
 * @lcpr version=21913
 *
 * [105] 从前序与中序遍历序列构造二叉树
 *
 * https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
 *
 * algorithms
 * Medium (71.26%)
 * Likes:    2041
 * Dislikes: 0
 * Total Accepted:    521.3K
 * Total Submissions: 731.5K
 * Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
 *
 * 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder
 * 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
 * 输出: [3,9,20,null,null,15,7]
 * 
 * 
 * 示例 2:
 * 
 * 输入: preorder = [-1], inorder = [-1]
 * 输出: [-1]
 * 
 * 
 * 
 * 
 * 提示:
 * 
 * 
 * 1 <= preorder.length <= 3000
 * inorder.length == preorder.length
 * -3000 <= preorder[i], inorder[i] <= 3000
 * preorder 和 inorder 均 无重复 元素
 * inorder 均出现在 preorder
 * preorder 保证 为二叉树的前序遍历序列
 * inorder 保证 为二叉树的中序遍历序列
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

func buildTree(preorder []int, inorder []int) *TreeNode {
	ids := map[int]int{}
	for i, x := range inorder{
		ids[x] = i
	}

	var	build func(preorder []int, lp int, rp int, inorder []int, li, ri int) *TreeNode 
	build = func(preorder []int, lp int, rp int, inorder []int, li, ri int) *TreeNode {
		if lp > rp{
			return nil
		}
		node := &TreeNode{Val: preorder[lp]}
		llen := ids[preorder[lp]] - li
		node.Left = build(preorder, lp + 1, lp + llen, inorder, li, ids[preorder[lp]] - 1)
		node.Right = build(preorder, lp + llen + 1, rp, inorder, ids[preorder[lp]] + 1, ri)
		return node
	}


	return build(preorder,0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
}
// @lc code=end



/*
// @lcpr case=start
// [3,9,20,15,7]\n[9,3,15,20,7]\n
// @lcpr case=end

// @lcpr case=start
// [-1]\n[-1]\n
// @lcpr case=end

 */

