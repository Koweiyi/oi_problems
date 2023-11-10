/*
 * @lc app=leetcode.cn id=1530 lang=golang
 * @lcpr version=21913
 *
 * [1530] 好叶子节点对的数量
 *
 * https://leetcode.cn/problems/number-of-good-leaf-nodes-pairs/description/
 *
 * algorithms
 * Medium (58.56%)
 * Likes:    142
 * Dislikes: 0
 * Total Accepted:    11.6K
 * Total Submissions: 19.8K
 * Testcase Example:  '[1,2,3,null,4]\n3'
 *
 * 给你二叉树的根节点 root 和一个整数 distance 。
 * 
 * 如果二叉树中两个 叶 节点之间的 最短路径长度 小于或者等于 distance ，那它们就可以构成一组 好叶子节点对 。
 * 
 * 返回树中 好叶子节点对的数量 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 
 * 
 * 输入：root = [1,2,3,null,4], distance = 3
 * 输出：1
 * 解释：树的叶节点是 3 和 4 ，它们之间的最短路径的长度是 3 。这是唯一的好叶子节点对。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 
 * 输入：root = [1,2,3,4,5,6,7], distance = 3
 * 输出：2
 * 解释：好叶子节点对为 [4,5] 和 [6,7] ，最短路径长度都是 2 。但是叶子节点对 [4,6] 不满足要求，因为它们之间的最短路径长度为 4
 * 。
 * 
 * 
 * 示例 3：
 * 
 * 输入：root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
 * 输出：1
 * 解释：唯一的好叶子节点对是 [2,5] 。
 * 
 * 
 * 示例 4：
 * 
 * 输入：root = [100], distance = 1
 * 输出：0
 * 
 * 
 * 示例 5：
 * 
 * 输入：root = [1,1,1], distance = 2
 * 输出：1
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * tree 的节点数在 [1, 2^10] 范围内。
 * 每个节点的值都在 [1, 100] 之间。
 * 1 <= distance <= 10
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

// 枚举从每个叶子节点进行深搜，因为disdance不超过10
// 在distance步之内搜到的其他叶子就都满足条件， 一共1000节点，每个节点递归深度10以内//不太可行好像

// lc啊· 求一下最近公共祖先 
func countPairs(root *TreeNode, distance int) int {

	// 力扣的treeNode真的是很傻

	pa := map[*TreeNode]*TreeNode{}
	leafs := []*TreeNode{} // 存叶子节点

	visited := map[*TreeNode]bool{nil:true}

	var dfs1 func(root *TreeNode, p *TreeNode)
	dfs1 = func(root *TreeNode, p *TreeNode){
		if root == nil{
			return
		}
		if root.Left == nil && root.Right == nil{
			leafs = append(leafs, root)
		}
		pa[root] = p
		dfs1(root.Left, root)
		dfs1(root.Right, root)
	}
	res := 0
	dfs1(root, nil)
	var dfs func(root *TreeNode, dis int)
	dfs = func(root *TreeNode, dis int){
		if dis > distance{
			return
		}
		if root.Left == nil && root.Right == nil && dis != 0{
			res ++
		}
		if !visited[root.Left]{
			visited[root.Left] = true
			dfs(root.Left, dis + 1)
			visited[root.Left] = false
		} 
		if !visited[root.Right]{
			visited[root.Right] = true
			dfs(root.Right, dis + 1)
			visited[root.Right] = false
		}
		if !visited[pa[root]]{
			visited[pa[root]] = true
			dfs(pa[root], dis + 1)
			visited[pa[root]] = false
		}
	}
	for _, leaf := range leafs{
		visited[leaf] = true
		dfs(leaf, 0)
	} 
	return res
}
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,null,4]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5,6,7]\n3\n
// @lcpr case=end

// @lcpr case=start
// [7,1,4,6,null,5,3,null,null,null,null,null,2]\n3\n
// @lcpr case=end

// @lcpr case=start
// [100]\n1\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1]\n2\n
// @lcpr case=end

 */

