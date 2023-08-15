/*
 * @lc app=leetcode.cn id=103 lang=golang
 * @lcpr version=21913
 *
 * [103] 二叉树的锯齿形层序遍历
 *
 * https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/description/
 *
 * algorithms
 * Medium (57.59%)
 * Likes:    794
 * Dislikes: 0
 * Total Accepted:    314.9K
 * Total Submissions: 546.9K
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：root = [3,9,20,null,null,15,7]
 * 输出：[[3],[20,9],[15,7]]
 * 
 * 
 * 示例 2：
 * 
 * 输入：root = [1]
 * 输出：[[1]]
 * 
 * 
 * 示例 3：
 * 
 * 输入：root = []
 * 输出：[]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 树中节点数目在范围 [0, 2000] 内
 * -100 <= Node.val <= 100
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
func zigzagLevelOrder(root *TreeNode) (res [][]int) {
	if root == nil{
		return
	}
	level := 0
	q := []*TreeNode{root}
	for len(q) > 0{
		tmp := []*TreeNode{}
		arr := []int{}
		for _, node := range q{
			arr = append(arr, node.Val)
			if node.Left != nil {tmp = append(tmp, node.Left)}
			if node.Right != nil {tmp = append(tmp, node.Right)}
		}
		if level == 1{
			for i := 0 ; i < len(arr) / 2 ; i ++ {
				arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
			}
		}
		level ^= 1
		q = tmp
		res = append(res, arr)
	}
	return 
}
// @lc code=end



/*
// @lcpr case=start
// [3,9,20,null,null,15,7]\n
// @lcpr case=end

// @lcpr case=start
// [1]\n
// @lcpr case=end

// @lcpr case=start
// []\n
// @lcpr case=end

 */

