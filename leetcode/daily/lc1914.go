/*
 * @lc app=leetcode.cn id=1914 lang=golang
 * @lcpr version=21913
 *
 * [1914] 循环轮转矩阵
 *
 * https://leetcode.cn/problems/cyclically-rotating-a-grid/description/
 *
 * algorithms
 * Medium (46.77%)
 * Likes:    23
 * Dislikes: 0
 * Total Accepted:    4.4K
 * Total Submissions: 9.4K
 * Testcase Example:  '[[40,10],[30,20]]\n1'
 *
 * 给你一个大小为 m x n 的整数矩阵 grid​​​ ，其中 m 和 n 都是 偶数 ；另给你一个整数 k 。
 *
 * 矩阵由若干层组成，如下图所示，每种颜色代表一层：
 *
 *
 *
 * 矩阵的循环轮转是通过分别循环轮转矩阵中的每一层完成的。在对某一层进行一次循环旋转操作时，层中的每一个元素将会取代其 逆时针
 * 方向的相邻元素。轮转示例如下：
 *
 * 返回执行 k 次循环轮转操作后的矩阵。
 *
 *
 *
 * 示例 1：
 *
 * 输入：grid = [[40,10],[30,20]], k = 1
 * 输出：[[10,20],[40,30]]
 * 解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。
 *
 * 示例 2：
 * ⁠
 *
 * 输入：grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
 * 输出：[[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
 * 解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == grid.length
 * n == grid[i].length
 * 2 <= m, n <= 50
 * m 和 n 都是 偶数
 * 1 <= grid[i][j] <=^ 5000
 * 1 <= k <= 10^9
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
func rotateGrid(grid [][]int, k int) [][]int {
	dir := [4][2]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}}
	m, n := len(grid), len(grid[0])

	vis := make([][]bool, m)
	for i := range vis{
		vis[i] = make([]bool, n)
	}

	for cx, cy := 0, 0 ; cx < m / 2 && cy < n / 2 ; cx, cy = cx + 1, cy + 1{
		px, py := cx, cy 
		cd := 0 // 当前方向
		nums := []int{}
		tot := (m / 2 - cx) * 4 + (n / 2 - cy) * 4 - 4 
		for i := 0 ; i < tot ; i ++ {
			nums = append(nums, grid[px][py])
			nx, ny := px + dir[cd][0], py + dir[cd][1]
			if nx < 0 || nx >= m || ny < 0 || ny >= n || vis[nx][ny] {
				cd = (cd + 1) % 4 
				nx, ny = px + dir[cd][0], py + dir[cd][1]
			}
			px, py = nx, ny 
		} 

		for i := 0 ; i < k % tot ; i ++ {
			nx, ny := px + dir[cd][0], py + dir[cd][1]
			if nx < 0 || nx >= m || ny < 0 || ny >= n || vis[nx][ny] {
				cd = (cd + 1) % 4 
				nx, ny = px + dir[cd][0], py + dir[cd][1]
			}
			px, py = nx, ny 
		}

		for i := 0 ; i < tot ; i ++ {
			grid[px][py] = nums[i]
			vis[px][py] = true
			nx, ny := px + dir[cd][0], py + dir[cd][1]
			if nx < 0 || nx >= m || ny < 0 || ny >= n || vis[nx][ny] {
				cd = (cd + 1) % 4 
				nx, ny = px + dir[cd][0], py + dir[cd][1]
			}
			px, py = nx, ny 
		}
	}
	return grid
}
// @lc code=end



/*
// @lcpr case=start
// [[40,10],[30,20]]\n1\n
// @lcpr case=end

// @lcpr case=start
// [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]\n2\n
// @lcpr case=end

 */

