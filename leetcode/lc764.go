/*
 * @lc app=leetcode.cn id=764 lang=golang
 * @lcpr version=21913
 *
 * [764] 最大加号标志
 *
 * https://leetcode.cn/problems/largest-plus-sign/description/
 *
 * algorithms
 * Medium (54.18%)
 * Likes:    212
 * Dislikes: 0
 * Total Accepted:    29.5K
 * Total Submissions: 54.4K
 * Testcase Example:  '5\n[[4,2]]'
 *
 * 在一个 n x n 的矩阵 grid 中，除了在数组 mines 中给出的元素为 0，其他每个元素都为 1。mines[i] = [xi, yi]表示
 * grid[xi][yi] == 0
 * 
 * 返回  grid 中包含 1 的最大的 轴对齐 加号标志的阶数 。如果未找到加号标志，则返回 0 。
 * 
 * 一个 k 阶由 1 组成的 “轴对称”加号标志 具有中心网格 grid[r][c] == 1 ，以及4个从中心向上、向下、向左、向右延伸，长度为
 * k-1，由 1 组成的臂。注意，只有加号标志的所有网格要求为 1 ，别的网格可能为 0 也可能为 1 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 输入: n = 5, mines = [[4, 2]]
 * 输出: 2
 * 解释: 在上面的网格中，最大加号标志的阶只能是2。一个标志已在图中标出。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 
 * 输入: n = 1, mines = [[0, 0]]
 * 输出: 0
 * 解释: 没有加号标志，返回 0 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n <= 500
 * 1 <= mines.length <= 5000
 * 0 <= xi, yi < n
 * 每一对 (xi, yi) 都 不重复​​​​​​​
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
func orderOfLargestPlusSign(n int, mines [][]int) int {


	dp := make([][]int, n)
	for i := range dp{
		dp[i] = make([]int, n)
		for j := range dp[i]{
			dp[i][j] = 5005
		}
	}
	for _, m := range mines{
		dp[m[0]][m[1]] = 0
	}
	res := 0
	for i := 0 ; i < n  ; i ++ {
		cnt := 0
		for j := 0 ; j < n ; j ++ {
			if dp[i][j] == 0{
				cnt = 0
			}else{
				cnt ++ 
			}
			dp[i][j] = min(dp[i][j], cnt)
		}
		cnt = 0 
		for j := n - 1 ; j >= 0 ; j -- {
			if dp[i][j] == 0{
				cnt = 0 
			}else{
				cnt ++ 
			}
			dp[i][j] = min(dp[i][j], cnt)
		}
	}

	for j := 0 ; j < n  ; j ++ {
		cnt := 0
		for i := 0 ; i < n ; i ++ {
			if dp[i][j] == 0{
				cnt = 0
			}else{
				cnt ++ 
			}
			dp[i][j] = min(dp[i][j], cnt)
		}
		cnt = 0 
		for i := n - 1 ; i >= 0 ; i -- {
			if dp[i][j] == 0{
				cnt = 0 
			}else{
				cnt ++ 
			}
			dp[i][j] = min(dp[i][j], cnt)
			res = max(res, dp[i][j])
		}
	}
	return res 
}
func min(a, b int) int {if a < b {return a}; return b}
func max(a, b int) int {if a > b {return a}; return b}

// @lc code=end



/*
// @lcpr case=start
// 5\n[[4, 2]]\n
// @lcpr case=end

// @lcpr case=start
// 1\n[[0, 0]]\n
// @lcpr case=end

 */

