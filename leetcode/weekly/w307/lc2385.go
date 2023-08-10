/*
 * @lc app=leetcode.cn id=2385 lang=golang
 * @lcpr version=21913
 *
 * [2385] 感染二叉树需要的总时间
 *
 * https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected/description/
 *
 * algorithms
 * Medium (46.16%)
 * Likes:    42
 * Dislikes: 0
 * Total Accepted:    8.5K
 * Total Submissions: 18.5K
 * Testcase Example:  '[1,5,3,null,4,10,6,9,2]\n3'
 *
 * 给你一棵二叉树的根节点 root ，二叉树中节点的值 互不相同 。另给你一个整数 start 。在第 0 分钟，感染 将会从值为 start
 * 的节点开始爆发。
 * 
 * 每分钟，如果节点满足以下全部条件，就会被感染：
 * 
 * 
 * 节点此前还没有感染。
 * 节点与一个已感染节点相邻。
 * 
 * 
 * 返回感染整棵树需要的分钟数。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：root = [1,5,3,null,4,10,6,9,2], start = 3
 * 输出：4
 * 解释：节点按以下过程被感染：
 * - 第 0 分钟：节点 3
 * - 第 1 分钟：节点 1、10、6
 * - 第 2 分钟：节点5
 * - 第 3 分钟：节点 4
 * - 第 4 分钟：节点 9 和 2
 * 感染整棵树需要 4 分钟，所以返回 4 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：root = [1], start = 1
 * 输出：0
 * 解释：第 0 分钟，树中唯一一个节点处于感染状态，返回 0 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 树中节点的数目在范围 [1, 10^5] 内
 * 1 <= Node.val <= 10^5
 * 每个节点的值 互不相同
 * 树中必定存在值为 start 的节点
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
func amountOfTime(root *TreeNode, start int) int {
	var st *TreeNode
    parents := map[*TreeNode]*TreeNode{}
	var dfs func(*TreeNode, *TreeNode)

    dfs = func(node, pa *TreeNode) {
        if node == nil{
            return
        }
        if node.Val == start{
            st = node
        }
        parents[node] = pa 
        dfs(node.Left, node)
        dfs(node.Right, node)
    }
    dfs(root, nil)

    vis := map[*TreeNode]bool{st:true, nil:true}

    q := []*TreeNode{st}
    res := - 1
    for len(q) > 0 {
        res ++
        tmp := q
        q = nil
        for _, x := range tmp {
            if x != nil{
                if !vis[x.Left]{
                    vis[x.Left] = true
                    q = append(q, x.Left)
                }
                if !vis[x.Right]{
                    vis[x.Right] = true
                    q = append(q, x.Right)
                }
                if !vis[parents[x]]{
                    vis[parents[x]] = true
                    q = append(q, parents[x])
                }
            }
        }
    }
    return res 
}
// @lc code=end



/*
// @lcpr case=start
// [1,5,3,null,4,10,6,9,2]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1]\n1\n
// @lcpr case=end

 */

