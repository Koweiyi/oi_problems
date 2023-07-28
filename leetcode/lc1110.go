/*
 * @lc app=leetcode.cn id=1110 lang=golang
 * @lcpr version=21912
 *
 * [1110] 删点成林
 *
 * https://leetcode.cn/problems/delete-nodes-and-return-forest/description/
 *
 * algorithms
 * Medium (69.33%)
 * Likes:    298
 * Dislikes: 0
 * Total Accepted:    36.1K
 * Total Submissions: 52.1K
 * Testcase Example:  '[1,2,3,4,5,6,7]\n[3,5]'
 *
 * 给出二叉树的根节点 root，树上每个节点都有一个不同的值。
 *
 * 如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。
 *
 * 返回森林中的每棵树。你可以按任意顺序组织答案。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
 * 输出：[[1,2,null,4],[6],[7]]
 *
 *
 * 示例 2：
 *
 * 输入：root = [1,2,4,null,3], to_delete = [3]
 * 输出：[[1,2,4]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中的节点数最大为 1000。
 * 每个节点都有一个介于 1 到 1000 之间的值，且各不相同。
 * to_delete.length <= 1000
 * to_delete 包含一些从 1 到 1000、各不相同的值。
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
func delNodes(root *TreeNode, to_delete []int) []*TreeNode {
	delete := [1005]bool{}
	for _, x := range to_delete{
		delete[x] = true
	}
    var dfs func(root *TreeNode) []*TreeNode
	dfs = func(root *TreeNode) []*TreeNode {
		res := []*TreeNode{} 
		if root == nil{
			return nil
		}
		if delete[root.Val]{
			res = append(res, dfs(root.Left)...)
			res = append(res, dfs(root.Right)...)
		}else {
			res = append(res, root)
			for _, x := range dfs(root.Left){
				if x != root.Left{
					res = append(res, x)
				}
			}
			for _, x := range dfs(root.Right){
				if x != root.Right{
					res = append(res, x)
				}
			}
			if root.Left != nil && delete[root.Left.Val]{
				root.Left = nil	
			}
			if root.Right != nil && delete[root.Right.Val]{
				root.Right = nil
			}
		}
		return res 
	}
	return dfs(root)
}
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,4,5,6,7]\n[3,5]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,4,null,3]\n[3]\n
// @lcpr case=end

 */

