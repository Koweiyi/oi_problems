/*
 * @lc app=leetcode.cn id=2415 lang=golang
 * @lcpr version=21913
 *
 * [2415] 反转二叉树的奇数层
 *
 * https://leetcode.cn/problems/reverse-odd-levels-of-binary-tree/description/
 *
 * algorithms
 * Medium (70.07%)
 * Likes:    25
 * Dislikes: 0
 * Total Accepted:    10.6K
 * Total Submissions: 15.2K
 * Testcase Example:  '[2,3,5,8,13,21,34]'
 *
 * 给你一棵 完美 二叉树的根节点 root ，请你反转这棵树中每个 奇数 层的节点值。
 * 
 * 
 * 例如，假设第 3 层的节点值是 [2,1,3,4,7,11,29,18] ，那么反转后它应该变成 [18,29,11,7,4,3,1,2] 。
 * 
 * 
 * 反转后，返回树的根节点。
 * 
 * 完美 二叉树需满足：二叉树的所有父节点都有两个子节点，且所有叶子节点都在同一层。
 * 
 * 节点的 层数 等于该节点到根节点之间的边数。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：root = [2,3,5,8,13,21,34]
 * 输出：[2,5,3,8,13,21,34]
 * 解释：
 * 这棵树只有一个奇数层。
 * 在第 1 层的节点分别是 3、5 ，反转后为 5、3 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：root = [7,13,11]
 * 输出：[7,11,13]
 * 解释： 
 * 在第 1 层的节点分别是 13、11 ，反转后为 11、13 。 
 * 
 * 
 * 示例 3：
 * 
 * 输入：root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
 * 输出：[0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
 * 解释：奇数层由非零值组成。
 * 在第 1 层的节点分别是 1、2 ，反转后为 2、1 。
 * 在第 3 层的节点分别是 1、1、1、1、2、2、2、2 ，反转后为 2、2、2、2、1、1、1、1 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 树中的节点数目在范围 [1, 2^14] 内
 * 0 <= Node.val <= 10^5
 * root 是一棵 完美 二叉树
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
func reverseOddLevels(root *TreeNode) *TreeNode {
	cur := 1
	q := []*TreeNode{root}
	for q[0].Left != nil {
		tmp := []*TreeNode{}
		for _, node := range q{
			tmp = append(tmp, node.Left)
			tmp = append(tmp, node.Right)
		}
		q = tmp
		if cur == 1{
			for i := 0 ; i < len(q) / 2 ; i ++ {
				q[i].Val, q[len(q) - i - 1].Val = q[len(q) - i - 1].Val, q[i].Val
			}
		}
		cur ^= 1
	}
	return root
}
// @lc code=end



/*
// @lcpr case=start
// [2,3,5,8,13,21,34]\n
// @lcpr case=end

// @lcpr case=start
// [7,13,11]\n
// @lcpr case=end

// @lcpr case=start
// [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]\n
// @lcpr case=end

 */

