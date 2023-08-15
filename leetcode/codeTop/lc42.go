/*
 * @lc app=leetcode.cn id=42 lang=golang
 * @lcpr version=21913
 *
 * [42] 接雨水
 *
 * https://leetcode.cn/problems/trapping-rain-water/description/
 *
 * algorithms
 * Hard (63.03%)
 * Likes:    4613
 * Dislikes: 0
 * Total Accepted:    743.1K
 * Total Submissions: 1.2M
 * Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
 *
 * 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
 * 输出：6
 * 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
 * 
 * 
 * 示例 2：
 * 
 * 输入：height = [4,2,0,3,2,5]
 * 输出：9
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * n == height.length
 * 1 <= n <= 2 * 10^4
 * 0 <= height[i] <= 10^5
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
func trap(height []int) int {
	n := len(height)
	left := make([]int, n)
	for i := 1 ; i < n ; i ++ {
		left[i] = max(left[i - 1], height[i - 1])
	} 
	rmax := 0
	res := 0 
	for i := n - 1 ; i >= 0 ; i -- {
		mx := min(left[i], rmax)
		res += max(0, mx - height[i])
		rmax = max(rmax, height[i])
	}
	return res 
}
func min(a, b int) int {if a < b {return a}; return b}
func max(a, b int) int {if a > b {return a}; return b}

// @lc code=end



/*
// @lcpr case=start
// [0,1,0,2,1,0,1,3,2,1,2,1]\n
// @lcpr case=end

// @lcpr case=start
// [4,2,0,3,2,5]\n
// @lcpr case=end

 */

