/*
 * @lc app=leetcode.cn id=2370 lang=golang
 * @lcpr version=21913
 *
 * [2370] 最长理想子序列
 *
 * https://leetcode.cn/problems/longest-ideal-subsequence/description/
 *
 * algorithms
 * Medium (43.10%)
 * Likes:    36
 * Dislikes: 0
 * Total Accepted:    8.6K
 * Total Submissions: 20K
 * Testcase Example:  '"acfgbd"\n2'
 *
 * 给你一个由小写字母组成的字符串 s ，和一个整数 k 。如果满足下述条件，则可以将字符串 t 视作是 理想字符串 ：
 *
 *
 * t 是字符串 s 的一个子序列。
 * t 中每两个 相邻 字母在字母表中位次的绝对差值小于或等于 k 。
 *
 *
 * 返回 最长 理想字符串的长度。
 *
 * 字符串的子序列同样是一个字符串，并且子序列还满足：可以经由其他字符串删除某些字符（也可以不删除）但不改变剩余字符的顺序得到。
 *
 * 注意：字母表顺序不会循环。例如，'a' 和 'z' 在字母表中位次的绝对差值是 25 ，而不是 1 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：s = "acfgbd", k = 2
 * 输出：4
 * 解释：最长理想字符串是 "acbd" 。该字符串长度为 4 ，所以返回 4 。
 * 注意 "acfgbd" 不是理想字符串，因为 'c' 和 'f' 的字母表位次差值为 3 。
 *
 * 示例 2：
 *
 * 输入：s = "abcd", k = 3
 * 输出：4
 * 解释：最长理想字符串是 "abcd" ，该字符串长度为 4 ，所以返回 4 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 10^5
 * 0 <= k <= 25
 * s 由小写英文字母组成
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
func longestIdealString(s string, k int) int {
	dp := make([]int, 26)
	for i := 0 ; i < len(s) ; i ++ {
		id := int(s[i] - 'a')
		dp[id] ++ 
		// fmt.Println( max(-int(s[i] - 'a'), -k) ,min(int('z' - s[i]), k))
		for j := max(-int(s[i] - 'a'), -k) ; j <= min(int('z' - s[i]), k) ; j ++ {
			if j != 0 {dp[id] = max(dp[id], dp[id + j] + 1)}
		}
	}
	
	mx := 0
	for i := 0 ; i < 26 ; i ++ {
		mx = max(mx, dp[i])
	}
	return mx 
}
func max(a, b int) int {if a > b {return a}; return b}
func min(a, b int) int {if a < b {return a}; return b}

// @lc code=end



/*
// @lcpr case=start
// "acfgbd"\n2\n
// @lcpr case=end

// @lcpr case=start
// "abcd"\n3\n
// @lcpr case=end

 */

