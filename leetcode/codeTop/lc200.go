/*
 * @lc app=leetcode.cn id=200 lang=golang
 * @lcpr version=21913
 *
 * [200] 岛屿数量
 *
 * https://leetcode.cn/problems/number-of-islands/description/
 *
 * algorithms
 * Medium (59.41%)
 * Likes:    2255
 * Dislikes: 0
 * Total Accepted:    682.7K
 * Total Submissions: 1.1M
 * Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
 *
 * 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
 * 
 * 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
 * 
 * 此外，你可以假设该网格的四条边均被水包围。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：grid = [
 * ⁠ ["1","1","1","1","0"],
 * ⁠ ["1","1","0","1","0"],
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["0","0","0","0","0"]
 * ]
 * 输出：1
 * 
 * 
 * 示例 2：
 * 
 * 输入：grid = [
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["0","0","1","0","0"],
 * ⁠ ["0","0","0","1","1"]
 * ]
 * 输出：3
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
 * grid[i][j] 的值为 '0' 或 '1'
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
func numIslands(grid [][]byte) (res int) {
	m, n := len(grid), len(grid[0])
	d := [4][2]int{{0,1},{1,0},{0,-1},{-1,0}}
	var dfs func(i, j int)
	dfs = func(i, j int) {
		grid[i][j] = '0'
		for k := 0 ; k < 4 ; k ++ {
			nx, ny := i + d[k][0], j + d[k][1]
			if 0 <= nx && nx < m && 0 <= ny && ny < n && grid[nx][ny] == '1'{
				dfs(nx, ny)
			} 
		}		
	}

	for i := 0 ; i < len(grid) ; i ++ {
		for j := 0 ; j < len(grid[0]) ; j ++ {
			if grid[i][j] == '1'{
				res ++
				dfs(i, j)
			}
		}
	}
	return res 
}
// @lc code=end



/*
// @lcpr case=start
// [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
// @lcpr case=end

// @lcpr case=start
// [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
// @lcpr case=end

 */

