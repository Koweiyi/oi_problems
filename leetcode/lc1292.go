/*
 * @lc app=leetcode.cn id=1292 lang=golang
 * @lcpr version=21913
 *
 * [1292] 元素和小于等于阈值的正方形的最大边长
 *
 * https://leetcode.cn/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/description/
 *
 * algorithms
 * Medium (50.78%)
 * Likes:    114
 * Dislikes: 0
 * Total Accepted:    11.6K
 * Total Submissions: 22.8K
 * Testcase Example:  '[[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]\n4'
 *
 * 给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。
 * 
 * 请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0 。
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 输入：mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
 * 输出：2
 * 解释：总和小于或等于 4 的正方形的最大边长为 2，如图所示。
 * 
 * 
 * 示例 2：
 * 
 * 输入：mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]],
 * threshold = 1
 * 输出：0
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * m == mat.length
 * n == mat[i].length
 * 1 <= m, n <= 300
 * 0 <= mat[i][j] <= 10^4
 * 0 <= threshold <= 10^5^ 
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
func maxSideLength(mat [][]int, threshold int) int {

	m, n := len(mat), len(mat[0])
	pre_sum := make([][]int, len(mat) + 1)
	for i := range pre_sum{
		pre_sum[i] = make([]int, len(mat[0]) + 1)
	}
	for i := 0 ; i < m ; i ++ {
		for j := 0 ; j < n ; j ++ {
			pre_sum[i + 1][j + 1] = pre_sum[i + 1][j] + pre_sum[i][j + 1] - pre_sum[i][j] + mat[i][j]
		}
	}
	res := 0
	for i := 0 ; i < m ; i ++ {
		for j := 0 ; j < n ; j ++{
			// 枚举可以改二分会快一点
			for l := 1 ; i + l - 1 < m && j + l - 1 < n ; l ++ {
				rx, ry := i + l, j + l 
				if pre_sum[rx][ry] - pre_sum[rx][j] - pre_sum[i][ry] + pre_sum[i][j] <= threshold{
					res = max(res, l)
				}
			}
		}
	}
	return res 
}
func max(a, b int) int {if a > b {return a} ; return b}
// @lc code=end



/*
// @lcpr case=start
// [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]\n4\n
// @lcpr case=end

// @lcpr case=start
// [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]\n1\n
// @lcpr case=end

 */

