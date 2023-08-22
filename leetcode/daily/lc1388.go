/*
 * @lc app=leetcode.cn id=1388 lang=golang
 * @lcpr version=21913
 *
 * [1388] 3n 块披萨
 *
 * https://leetcode.cn/problems/pizza-with-3n-slices/description/
 *
 * algorithms
 * Hard (62.93%)
 * Likes:    216
 * Dislikes: 0
 * Total Accepted:    17.2K
 * Total Submissions: 26.5K
 * Testcase Example:  '[1,2,3,4,5,6]'
 *
 * 给你一个披萨，它由 3n 块不同大小的部分组成，现在你和你的朋友们需要按照如下规则来分披萨：
 * 
 * 
 * 你挑选 任意 一块披萨。
 * Alice 将会挑选你所选择的披萨逆时针方向的下一块披萨。
 * Bob 将会挑选你所选择的披萨顺时针方向的下一块披萨。
 * 重复上述过程直到没有披萨剩下。
 * 
 * 
 * 每一块披萨的大小按顺时针方向由循环数组 slices 表示。
 * 
 * 请你返回你可以获得的披萨大小总和的最大值。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 输入：slices = [1,2,3,4,5,6]
 * 输出：10
 * 解释：选择大小为 4 的披萨，Alice 和 Bob 分别挑选大小为 3 和 5 的披萨。然后你选择大小为 6 的披萨，Alice 和 Bob
 * 分别挑选大小为 2 和 1 的披萨。你获得的披萨总大小为 4 + 6 = 10 。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 
 * 输入：slices = [8,9,8,6,1,1]
 * 输出：16
 * 解释：两轮都选大小为 8 的披萨。如果你选择大小为 9 的披萨，你的朋友们就会选择大小为 8 的披萨，这种情况下你的总和不是最大的。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= slices.length <= 500
 * slices.length % 3 == 0
 * 1 <= slices[i] <= 1000
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
func maxSizeSlices(slices []int) int {
	n := len(slices) / 3 
	solve := func (slices []int) int {
		m := len(slices)
		dp := make([][]int, m)
		for i := range dp{
			dp[i] = make([]int, n + 1)
			for j := range dp[i]{
				dp[i][j] = -0x3f3f3f3f
			}
		}

		dp[0][0], dp[1][0], dp[0][1], dp[1][1] = 0, 0, slices[0], max(slices[0], slices[1])
		for i := 2 ; i < m ; i ++ {
			dp[i][0] = 0 
			for j := 1 ; j <= n ; j ++ {
				dp[i][j] = max(dp[i - 1][j], dp[i - 2][ j - 1] + slices[i])
			}
		}
		return dp[m - 1][n]
	}
	return max(solve(slices[1:]), solve(slices[:len(slices) - 1]))
}
func max(a, b int) int {if a > b {return a}; return b}

// @lc code=end



/*
// @lcpr case=start
// [1,2,3,4,5,6]\n
// @lcpr case=end

// @lcpr case=start
// [8,9,8,6,1,1]\n
// @lcpr case=end

 */

