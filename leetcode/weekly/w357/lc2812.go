/*
 * @lc app=leetcode.cn id=2812 lang=golang
 * @lcpr version=21913
 *
 * [2812] 找出最安全路径
 *
 * https://leetcode.cn/problems/find-the-safest-path-in-a-grid/description/
 *
 * algorithms
 * Medium (23.61%)
 * Likes:    16
 * Dislikes: 0
 * Total Accepted:    2.4K
 * Total Submissions: 10K
 * Testcase Example:  '[[1,0,0],[0,0,0],[0,0,1]]'
 *
 * 给你一个下标从 0 开始、大小为 n x n 的二维矩阵 grid ，其中 (r, c) 表示：
 * 
 * 
 * 如果 grid[r][c] = 1 ，则表示一个存在小偷的单元格
 * 如果 grid[r][c] = 0 ，则表示一个空单元格
 * 
 * 
 * 你最开始位于单元格 (0, 0) 。在一步移动中，你可以移动到矩阵中的任一相邻单元格，包括存在小偷的单元格。
 * 
 * 矩阵中路径的 安全系数 定义为：从路径中任一单元格到矩阵中任一小偷所在单元格的 最小 曼哈顿距离。
 * 
 * 返回所有通向单元格 (n - 1, n - 1) 的路径中的 最大安全系数 。
 * 
 * 单元格 (r, c) 的某个 相邻 单元格，是指在矩阵中存在的 (r, c + 1)、(r, c - 1)、(r + 1, c) 和 (r - 1,
 * c) 之一。
 * 
 * 两个单元格 (a, b) 和 (x, y) 之间的 曼哈顿距离 等于 | a - x | + | b - y | ，其中 |val| 表示 val
 * 的绝对值。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：grid = [[1,0,0],[0,0,0],[0,0,1]]
 * 输出：0
 * 解释：从 (0, 0) 到 (n - 1, n - 1) 的每条路径都经过存在小偷的单元格 (0, 0) 和 (n - 1, n - 1) 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：grid = [[0,0,1],[0,0,0],[0,0,0]]
 * 输出：2
 * 解释：
 * 上图所示路径的安全系数为 2：
 * - 该路径上距离小偷所在单元格（0，2）最近的单元格是（0，0）。它们之间的曼哈顿距离为 | 0 - 0 | + | 0 - 2 | = 2 。
 * 可以证明，不存在安全系数更高的其他路径。
 * 
 * 
 * 示例 3：
 * 
 * 输入：grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
 * 输出：2
 * 解释：
 * 上图所示路径的安全系数为 2：
 * - 该路径上距离小偷所在单元格（0，3）最近的单元格是（1，2）。它们之间的曼哈顿距离为 | 0 - 1 | + | 3 - 2 | = 2 。
 * - 该路径上距离小偷所在单元格（3，0）最近的单元格是（3，2）。它们之间的曼哈顿距离为 | 3 - 3 | + | 0 - 2 | = 2 。
 * 可以证明，不存在安全系数更高的其他路径。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= grid.length == n <= 400
 * grid[i].length == n
 * grid[i][j] 为 0 或 1
 * grid 至少存在一个小偷
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

type point struct{x, y int}
func maximumSafenessFactor(grid [][]int) int {
	n := len(grid)
	dis := make([][]int, n)
	for i := 0 ; i < n ; i ++ {
		dis[i] = make([]int, n)
	}
	for i := 0; i < n ; i ++{
		for j := 0 ; j < n ; j ++ {
			dis[i][j] = -1
		}
	}
	q := make([]point, 0)
	for i := 0 ; i < n ; i ++ {
		for j := 0 ; j < n ; j ++ {
			if grid[i][j] == 1{
				q = append(q, point{i, j})
				dis[i][j] = 0
			}
		}
	}
	group := [][]point{q}
	d := [4][2]int{{0, 1}, {0,-1}, {1, 0}, {-1, 0}}

	for len(q) > 0{
		tmp := q
		q = nil
		for _, p := range tmp{
			x, y := p.x, p.y
			for i := 0 ; i < 4 ; i ++ {
				nx, ny := x + d[i][0], y + d[i][1]
				if 0 <= nx && nx < n && 0 <= ny && ny < n && dis[nx][ny] < 0{
					q = append(q, point{nx, ny})
					dis[nx][ny] = len(group)
				}
			}			
		}
		group = append(group, q)
	}

	fa := make([]int, n * n)
	for i := range fa {
		fa[i] = i
	}
	var find func (x int) int
	find = func(x int) int {
		if fa[x] != x{
			fa[x] = find(fa[x])
		}
		return fa[x]
	}
	var union func (x, y int) 
	union = func(x, y int) {
		fa[find(x)] = find(y)
	}

	for res := len(group) - 2 ; res > 0 ; res -- {
		for _, p := range group[res]{
			i, j := p.x, p.y
			for k := range d{
				nx, ny := i + d[k][0], j + d[k][1]
				if 0 <= nx && nx < n && 0 <= ny && ny < n && dis[nx][ny] >= dis[i][j]{
					union(i * n + j, nx * n + ny)
				}
			} 
		}
		if find(0) == find(n * n - 1){
			return res 
		}
	}
	return 0
	
}
// @lc code=end



/*
// @lcpr case=start
// [[1,0,0],[0,0,0],[0,0,1]]\n
// @lcpr case=end

// @lcpr case=start
// [[0,0,1],[0,0,0],[0,0,0]]\n
// @lcpr case=end

// @lcpr case=start
// [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]\n
// @lcpr case=end

 */

