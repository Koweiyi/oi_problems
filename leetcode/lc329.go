/*
 * @lc app=leetcode.cn id=329 lang=golang
 * @lcpr version=21913
 *
 * [329] 矩阵中的最长递增路径
 *
 * https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/description/
 *
 * algorithms
 * Hard (51.82%)
 * Likes:    785
 * Dislikes: 0
 * Total Accepted:    99.5K
 * Total Submissions: 192.1K
 * Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
 *
 * 给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。
 * 
 * 对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
 * 输出：4 
 * 解释：最长递增路径为 [1, 2, 6, 9]。
 * 
 * 示例 2：
 * 
 * 输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
 * 输出：4 
 * 解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
 * 
 * 
 * 示例 3：
 * 
 * 输入：matrix = [[1]]
 * 输出：1
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 200
 * 0 <= matrix[i][j] <= 2^31 - 1
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
func longestIncreasingPath(matrix [][]int) int {
	m,n := len(matrix), len(matrix[0])
	memo := make([][]int, m)
	for i := range memo{
		memo[i] = make([]int, n)
		for j := range memo[i]{
			memo[i][j] = -1
		}
	}
	dir := [][]int{{0,1},{1,0},{0,-1},{-1,0}}
	var dfs func(x, y int) int
	dfs = func(x int, y int) int {
		if memo[x][y] != -1{
			return memo[x][y]
		}
		res := 1
		defer func ()  {
			memo[x][y] = res 
		}()
		for _, d := range dir{
			nx, ny := x + d[0], y + d[1]
			if 0 <= nx && nx < m && 0 <= ny && ny < n && matrix[nx][ny] > matrix[x][y]{
				res = max(res, dfs(nx, ny) + 1)
			}
		}
		return res 
	}
	res := 0
	for i := 0 ; i < m ; i ++ {
		for j := 0 ; j < n ; j ++ {
			res = max(res, dfs(i, j))
		}
	}
	return res 

}
func max(a, b int) int {if a > b {return a} ; return b}
// @lc code=end



/*
// @lcpr case=start
// [[9,9,4],[6,6,8],[2,1,1]]\n
// @lcpr case=end

// @lcpr case=start
// [[3,4,5],[3,2,6],[2,2,1]]\n
// @lcpr case=end

// @lcpr case=start
// [[1]]\n
// @lcpr case=end

 */

