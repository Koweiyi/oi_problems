/*
 * @lc app=leetcode.cn id=322 lang=golang
 * @lcpr version=21913
 *
 * [322] 零钱兑换
 *
 * https://leetcode.cn/problems/coin-change/description/
 *
 * algorithms
 * Medium (46.59%)
 * Likes:    2518
 * Dislikes: 0
 * Total Accepted:    663.3K
 * Total Submissions: 1.4M
 * Testcase Example:  '[1,2,5]\n11'
 *
 * 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
 *
 * 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
 *
 * 你可以认为每种硬币的数量是无限的。
 *
 *
 *
 * 示例 1：
 *
 * 输入：coins = [1, 2, 5], amount = 11
 * 输出：3
 * 解释：11 = 5 + 5 + 1
 *
 * 示例 2：
 *
 * 输入：coins = [2], amount = 3
 * 输出：-1
 *
 * 示例 3：
 *
 * 输入：coins = [1], amount = 0
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= coins.length <= 12
 * 1 <= coins[i] <= 2^31 - 1
 * 0 <= amount <= 10^4
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
func coinChange(coins []int, amount int) int {


	// 记忆化写法
	// dfs(i) 表示金额i 需要的最少硬币数
	// memo := make([]int, amount + 10)
	// for i := range memo{
	// 	memo[i] = -1
	// }

	// var dfs func(left int) int
	// dfs = func(left int) int {
	// 	if left == 0{
	// 		return 0
	// 	}
	// 	if memo[left] != -1{
	// 		return memo[left]
	// 	}
	// 	res := amount + 1
	// 	for _, x := range coins{
	// 		if left >= x{
	// 			res = min(res, dfs(left - x) + 1)
	// 		}
	// 	}
	// 	memo[left] = res 
	// 	return res 
	// } 
	// res := dfs(amount)
	// if res == amount + 1{
	// 	return -1
	// }
	// return res 

	// 递推
	dp := make([]int, amount + 1)
	for i := 1 ; i <= amount ; i ++ {
		dp[i] = amount + 1
		for _,x := range coins{
			if i >= x {
				dp[i] = min(dp[i], 1 + dp[i - x])
			}
		}
	}
	if dp[amount] == amount + 1{
		return -1
	}
	return dp[amount]
}
func min(a, b int) int {if a < b {return a}; return b}

// @lc code=end



/*
// @lcpr case=start
// [1, 2, 5]\n11\n
// @lcpr case=end

// @lcpr case=start
// [2]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1]\n0\n
// @lcpr case=end

 */

