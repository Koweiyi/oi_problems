/*
 * @lc app=leetcode.cn id=1391 lang=golang
 * @lcpr version=21913
 *
 * [1391] 检查网格中是否存在有效路径
 *
 * https://leetcode.cn/problems/check-if-there-is-a-valid-path-in-a-grid/description/
 *
 * algorithms
 * Medium (42.08%)
 * Likes:    67
 * Dislikes: 0
 * Total Accepted:    9K
 * Total Submissions: 21.3K
 * Testcase Example:  '[[2,4,3],[6,5,2]]'
 *
 * 给你一个 m x n 的网格 grid。网格里的每个单元都代表一条街道。grid[i][j] 的街道可以是：
 *
 *
 * 1 表示连接左单元格和右单元格的街道。
 * 2 表示连接上单元格和下单元格的街道。
 * 3 表示连接左单元格和下单元格的街道。
 * 4 表示连接右单元格和下单元格的街道。
 * 5 表示连接左单元格和上单元格的街道。
 * 6 表示连接右单元格和上单元格的街道。
 *
 *
 *
 *
 * 你最开始从左上角的单元格 (0,0) 开始出发，网格中的「有效路径」是指从左上方的单元格 (0,0) 开始、一直到右下方的 (m-1,n-1)
 * 结束的路径。该路径必须只沿着街道走。
 *
 * 注意：你 不能 变更街道。
 *
 * 如果网格中存在有效的路径，则返回 true，否则返回 false 。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：grid = [[2,4,3],[6,5,2]]
 * 输出：true
 * 解释：如图所示，你可以从 (0, 0) 开始，访问网格中的所有单元格并到达 (m - 1, n - 1) 。
 *
 *
 * 示例 2：
 *
 *
 *
 * 输入：grid = [[1,2,1],[1,2,1]]
 * 输出：false
 * 解释：如图所示，单元格 (0, 0) 上的街道没有与任何其他单元格上的街道相连，你只会停在 (0, 0) 处。
 *
 *
 * 示例 3：
 *
 * 输入：grid = [[1,1,2]]
 * 输出：false
 * 解释：你会停在 (0, 1)，而且无法到达 (0, 2) 。
 *
 *
 * 示例 4：
 *
 * 输入：grid = [[1,1,1,1,1,1,3]]
 * 输出：true
 *
 *
 * 示例 5：
 *
 * 输入：grid = [[2],[2],[2],[2],[2],[2],[6]]
 * 输出：true
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 300
 * 1 <= grid[i][j] <= 6
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
func hasValidPath(grid [][]int) bool {
	m, n := len(grid), len(grid[0]) 
	visited := make([][]bool, m) 
	for i := range visited{
		visited[i] = make([]bool, n)
	}
	mp := []int{0, 6, 9, 10, 12, 3, 5}
	d := [][]int{{-1,0},{0,-1},{0,1},{1,0}} // 上左右下
	var dfs func(x, y int) bool
	dfs = func(x, y int) bool {
		if x + y == 0 {
			return true
		} 
		res := false
		for i := 0 ; i < 4 ; i ++ {
			if mp[grid[x][y]] & (1 << i) == 0{continue}
			nx, ny := x + d[i][0], y + d[i][1]
			if 0 <= nx && nx < m && 0 <= ny && ny < n && !visited[nx][ny] && mp[grid[nx][ny]] & (1 << (3 - i)) != 0{
				visited[nx][ny] = true
				res = res || dfs(nx, ny)
			}
		}
		return res 
	}
	visited[m - 1][n - 1] = true
	return dfs(m - 1, n - 1)
}
// @lc code=end



/*
// @lcpr case=start
// [[2,4,3],[6,5,2]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,2,1],[1,2,1]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,1,2]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,1,1,1,1,1,3]]\n
// @lcpr case=end

// @lcpr case=start
// [[2],[2],[2],[2],[2],[2],[6]]\n
// @lcpr case=end

// @lcpr case=start
// [[4,1,3], [6,1,2]]\n
// @lcpr case=end
 */

