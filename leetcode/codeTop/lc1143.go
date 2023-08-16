/*
 * @lc app=leetcode.cn id=1143 lang=golang
 * @lcpr version=21913
 *
 * [1143] 最长公共子序列
 *
 * https://leetcode.cn/problems/longest-common-subsequence/description/
 *
 * algorithms
 * Medium (64.93%)
 * Likes:    1388
 * Dislikes: 0
 * Total Accepted:    360.4K
 * Total Submissions: 555K
 * Testcase Example:  '"abcde"\n"ace"'
 *
 * 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
 *
 * 一个字符串的 子序列
 * 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
 *
 *
 * 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
 *
 *
 * 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
 *
 *
 *
 * 示例 1：
 *
 * 输入：text1 = "abcde", text2 = "ace"
 * 输出：3
 * 解释：最长公共子序列是 "ace" ，它的长度为 3 。
 *
 *
 * 示例 2：
 *
 * 输入：text1 = "abc", text2 = "abc"
 * 输出：3
 * 解释：最长公共子序列是 "abc" ，它的长度为 3 。
 *
 *
 * 示例 3：
 *
 * 输入：text1 = "abc", text2 = "def"
 * 输出：0
 * 解释：两个字符串没有公共子序列，返回 0 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= text1.length, text2.length <= 1000
 * text1 和 text2 仅由小写英文字符组成。
 *
 *
 */
package leetcode

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
type ListNode struct {
	Val  int
	Next *ListNode
}

// @lc code=start
func longestCommonSubsequence(text1 string, text2 string) int {
	_, n := len(text1), len(text2)
	// 二维数组 空间O(mn)
	// dp := make([][]int, m + 1)
	// for i := range dp{
	// 	dp[i] = make([]int, n + 1)
	// }
	// // dp[i + 1][j + 1] = dp[i][j]  if text1[i] == text2[j]
	// //					= max(dp[i + 1][j], dp[i][j + 1]) if text1[i] != text2[j]
	// //					(0 < i <= m && 0 <= j < n)
	// // dp[0][i] = 0 0 <= i <= n
	// // dp[j][0] = 0 0 <= j <= m
	// // dp[i + 1][j + 1]
	// for i, x := range text1{
	// 	for j, y := range text2{
	// 		if x == y{
	// 			dp[i + 1][j + 1] = dp[i][j] + 1
	// 		}else{
	// 			dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
	// 		}
	// 	}
	// }
	// return dp[m][n]

	// 使用滚动数组进行优化 空间O(n)
	// dp := [2][]int{make([]int, n + 1), make([]int, n + 1)}
	// for i, x := range text1{
	// 	for j, y := range text2{
	// 		if x == y{
	// 			dp[(i + 1) % 2][j + 1] = dp[i % 2][j] + 1
	// 		}else{
	// 			dp[(i + 1) % 2][j + 1] = max(dp[(i + 1) % 2][j], dp[i % 2][j + 1])
	// 		}
	// 	}
	// }
	// return dp[m % 2][n]

	// 只使用一维数组解决 O(n) 空间

	/**
	pre dp[j + 1]
	*/
	dp := make([]int, n+1)
	for _, x := range text1 {
		pre := dp[0]
		for j, y := range text2 {
			if x == y {
				dp[j+1], pre = pre+1, dp[j+1]
			} else {
				dp[j+1], pre = max(dp[j+1], dp[j]), dp[j+1]
			}
		}
	}
	return dp[n]
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end

/*
// @lcpr case=start
// "abcde"\n"ace"\n
// @lcpr case=end

// @lcpr case=start
// "abc"\n"abc"\n
// @lcpr case=end

// @lcpr case=start
// "abc"\n"def"\n
// @lcpr case=end

*/
