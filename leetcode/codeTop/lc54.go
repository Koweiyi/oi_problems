/*
 * @lc app=leetcode.cn id=54 lang=golang
 * @lcpr version=21913
 *
 * [54] 螺旋矩阵
 *
 * https://leetcode.cn/problems/spiral-matrix/description/
 *
 * algorithms
 * Medium (49.47%)
 * Likes:    1453
 * Dislikes: 0
 * Total Accepted:    392.4K
 * Total Submissions: 793.1K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
 *
 *
 *
 * 示例 1：
 *
 * 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
 * 输出：[1,2,3,6,9,8,7,4,5]
 *
 *
 * 示例 2：
 *
 * 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
 * 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 10
 * -100 <= matrix[i][j] <= 100
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
func spiralOrder(matrix [][]int) (res []int) {
	m, n := len(matrix), len(matrix[0])
	// fmt.Printf("m: %d, n: %d\n", m, n)
	used := make([][]bool, m)
	for i := 0 ; i < m ; i ++ {
		used[i] = make([]bool, n)
	}

	curx, cury := 0, 0
	curd := 0 
	d := [4][2]int{{0, 1}, {1, 0}, {0, -1}, {-1,0}}
	for len(res) < m * n {
		res = append(res, matrix[curx][cury])
		used[curx][cury] = true
		nx, ny := curx + d[curd][0], cury + d[curd][1]
		
		// fmt.Printf("nx: %d, ny: %d\n", nx, ny)
		if nx < 0 || nx >= m || ny < 0 || ny >= n || used[nx][ny]{
			curd = (curd + 1) % 4
			nx, ny = curx + d[curd][0], cury + d[curd][1]
		}
		curx, cury = nx, ny 
	}
	return

}
// @lc code=end



/*
// @lcpr case=start
// [[1,2,3],[4,5,6],[7,8,9]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
// @lcpr case=end

 */

