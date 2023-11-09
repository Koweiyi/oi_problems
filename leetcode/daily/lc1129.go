/*
 * @lc app=leetcode.cn id=1129 lang=golang
 * @lcpr version=21913
 *
 * [1129] 颜色交替的最短路径
 *
 * https://leetcode.cn/problems/shortest-path-with-alternating-colors/description/
 *
 * algorithms
 * Medium (48.56%)
 * Likes:    284
 * Dislikes: 0
 * Total Accepted:    29.2K
 * Total Submissions: 60.2K
 * Testcase Example:  '3\n[[0,1],[1,2]]\n[]'
 *
 * 给定一个整数 n，即有向图中的节点数，其中节点标记为 0 到 n - 1。图中的每条边为红色或者蓝色，并且可能存在自环或平行边。
 * 
 * 给定两个数组 redEdges 和 blueEdges，其中：
 * 
 * 
 * redEdges[i] = [ai, bi] 表示图中存在一条从节点 ai 到节点 bi 的红色有向边，
 * blueEdges[j] = [uj, vj] 表示图中存在一条从节点 uj 到节点 vj 的蓝色有向边。
 * 
 * 
 * 返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X
 * 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 answer[x] = -1。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
 * 输出：[0,1,-1]
 * 
 * 
 * 示例 2：
 * 
 * 输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
 * 输出：[0,1,-1]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n <= 100
 * 0 <= redEdges.length, blueEdges.length <= 400
 * redEdges[i].length == blueEdges[j].length == 2
 * 0 <= ai, bi, uj, vj < n
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
func shortestAlternatingPaths(n int, redEdges [][]int, blueEdges [][]int) []int {
	g := make([][][]int, 2)
	g[0] = make([][]int, n)
	g[1] = make([][]int, n)
	for _, x := range redEdges{
		g[0][x[0]] = append(g[0][x[0]], x[1])
	}
	for _, x := range blueEdges{
		g[1][x[0]] = append(g[1][x[0]], x[1])
	}

	res := make([]int, n)
	for i := range res {
		res[i] = -1
	}
	vis := make([]int, n)
	cur := 0
	q := []int{0}
	vis[0] = 1
	for len(q) > 0{
		tmp := []int{}
		for _, u := range q{
			if res[u] == -1{
				res[u] = cur
			}else{
				res[u] = min(res[u], cur)
			}
			for _, v := range g[cur % 2][u]{
				if vis[v] < 2{
					vis[v] ++
					tmp = append(tmp, v)
				}
			}
		}
		cur ++
		q = tmp 
	}
	vis = make([]int, n)
	cur = 0
	q = []int{0}
	vis[0] = 1
	for len(q) > 0{
		tmp := []int{}
		for _, u := range q{
			if res[u] == -1{
				res[u] = cur
			}else{
				res[u] = min(res[u], cur)
			}
			for _, v := range g[(cur + 1) % 2][u]{
				if vis[v] < 2{
					vis[v] ++
					tmp = append(tmp, v)
				}
			}
		}
		cur ++
		q = tmp 
	}
	return res 

}
func min(a, b int) int {if a < b {return a}; return b}

// @lc code=end



/*
// @lcpr case=start
// 3\n[[0,1],[1,2]]\n[]\n
// @lcpr case=end

// @lcpr case=start
// 3\n[[0,1]]\n[[2,1]]\n
// @lcpr case=end

// @lcpr case=start
// 5\n[[0,1],[1,2],[2,3],[3,4]]\n[[1,2],[2,3],[3,1]]\n
// @lcpr case=end
 */

