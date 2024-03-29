/*
 * @lc app=leetcode.cn id=2400 lang=golang
 * @lcpr version=21913
 *
 * [2400] 恰好移动 k 步到达某一位置的方法数目
 *
 * https://leetcode.cn/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/description/
 *
 * algorithms
 * Medium (32.76%)
 * Likes:    45
 * Dislikes: 0
 * Total Accepted:    11.3K
 * Total Submissions: 34.5K
 * Testcase Example:  '1\n2\n3'
 *
 * 给你两个 正 整数 startPos 和 endPos 。最初，你站在 无限 数轴上位置 startPos
 * 处。在一步移动中，你可以向左或者向右移动一个位置。
 * 
 * 给你一个正整数 k ，返回从 startPos 出发、恰好 移动 k 步并到达 endPos 的 不同 方法数目。由于答案可能会很大，返回对 10^9
 * + 7 取余 的结果。
 * 
 * 如果所执行移动的顺序不完全相同，则认为两种方法不同。
 * 
 * 注意：数轴包含负整数。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：startPos = 1, endPos = 2, k = 3
 * 输出：3
 * 解释：存在 3 种从 1 到 2 且恰好移动 3 步的方法：
 * - 1 -> 2 -> 3 -> 2.
 * - 1 -> 2 -> 1 -> 2.
 * - 1 -> 0 -> 1 -> 2.
 * 可以证明不存在其他方法，所以返回 3 。
 * 
 * 示例 2：
 * 
 * 输入：startPos = 2, endPos = 5, k = 10
 * 输出：0
 * 解释：不存在从 2 到 5 且恰好移动 10 步的方法。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= startPos, endPos, k <= 1000
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
func numberOfWays(startPos int, endPos int, k int) int {
	// 题目信息在右侧, 主播刷题用的go python c++ 三种语言
	// 目前用Go
	type pair struct{x, y int}
	dp := map[pair]int{}
	const mod int = 1e9 + 7
	var dfs func(x, left int) int 
	dfs = func(x int, left int) int{
		p := pair{x, left}
		if v, ok := dp[p] ; ok{
			return v
		}

		if abs(x - endPos) > left{ return 0 }
		if left == 0 {return 1}
		res := (dfs(x + 1, left - 1) + dfs(x - 1, left - 1)) % mod 
		dp[p] = res 
		return res 

	}
	return dfs(startPos, k)
}
func abs(a int) int {if a < 0 {return -a}; return a}

// @lc code=end



/*
// @lcpr case=start
// 1\n2\n3\n
// @lcpr case=end

// @lcpr case=start
// 2\n5\n10\n
// @lcpr case=end

 */

