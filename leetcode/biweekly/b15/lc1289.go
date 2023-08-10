/*
 * @lc app=leetcode.cn id=1289 lang=golang
 * @lcpr version=21913
 *
 * [1289] 下降路径最小和  II
 *
 * https://leetcode.cn/problems/minimum-falling-path-sum-ii/description/
 *
 * algorithms
 * Hard (58.34%)
 * Likes:    108
 * Dislikes: 0
 * Total Accepted:    17.9K
 * Total Submissions: 29.9K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * 给你一个 n x n 整数矩阵 grid ，请你返回 非零偏移下降路径 数字和的最小值。
 *
 * 非零偏移下降路径 定义为：从 grid 数组中的每一行选择一个数字，且按顺序选出来的数字中，相邻数字不在原数组的同一列。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：grid = [[1,2,3],[4,5,6],[7,8,9]]
 * 输出：13
 * 解释：
 * 所有非零偏移下降路径包括：
 * [1,5,9], [1,5,7], [1,6,7], [1,6,8],
 * [2,4,8], [2,4,9], [2,6,7], [2,6,8],
 * [3,4,8], [3,4,9], [3,5,7], [3,5,9]
 * 下降路径中数字和最小的是 [1,5,7] ，所以答案是 13 。
 *
 *
 * 示例 2：
 *
 * 输入：grid = [[7]]
 * 输出：7
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == grid.length == grid[i].length
 * 1 <= n <= 200
 * -99 <= grid[i][j] <= 99
 *
 *
 */
package leetcode

import "math"
type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}
// @lc code=start
func minFallingPathSum(grid [][]int) int {
	n := len(grid)
	first_min_sum, first_min_index, second_min_sum := 0, -1, 0

	for i := 0 ; i < n ; i ++{
		cur_first_min_sum, cur_second_min_sum, cur_first_min_index  := math.MaxInt, math.MaxInt, -1
		for j := 0 ; j < n ; j ++{
			cur_sum := grid[i][j]
			if j != first_min_index{
				cur_sum += first_min_sum
			}else{
				cur_sum += second_min_sum
			}
			if cur_sum < cur_first_min_sum{
				cur_second_min_sum = cur_first_min_sum
				cur_first_min_index = j 
				cur_first_min_sum = cur_sum
			}else if cur_sum < cur_second_min_sum{
				cur_second_min_sum = cur_sum
			}
		}
		first_min_index = cur_first_min_index
		first_min_sum = cur_first_min_sum
		second_min_sum = cur_second_min_sum
	}
	return first_min_sum
}
func min(a, b int) int {if a < b {return a}; return b}

// @lc code=end



/*
// @lcpr case=start
// [[1,2,3],[4,5,6],[7,8,9]]\n
// @lcpr case=end

// @lcpr case=start
// [[7]]\n
// @lcpr case=end

 */

