/*
 * @lc app=leetcode.cn id=32 lang=golang
 * @lcpr version=21913
 *
 * [32] 最长有效括号
 *
 * https://leetcode.cn/problems/longest-valid-parentheses/description/
 *
 * algorithms
 * Hard (37.29%)
 * Likes:    2335
 * Dislikes: 0
 * Total Accepted:    389.1K
 * Total Submissions: 1M
 * Testcase Example:  '"(()"'
 *
 * 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：s = "(()"
 * 输出：2
 * 解释：最长有效括号子串是 "()"
 *
 *
 * 示例 2：
 *
 * 输入：s = ")()())"
 * 输出：4
 * 解释：最长有效括号子串是 "()()"
 *
 *
 * 示例 3：
 *
 * 输入：s = ""
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= s.length <= 3 * 10^4
 * s[i] 为 '(' 或 ')'
 *
 *
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
func longestValidParentheses(s string) int {

	// dp[i] 表示以s[i] 结尾的最长有效括号长度
	// s[i] == '(' dp[i] = 0
	// s[i] == ')' if s[i - 1] == '(' dp[i] = dp[i - 2] + 2
	// 				  s[i - 1] != '(' 那么继续向前寻找s[i - dp[i - 1] - 1]是否为'('
	n := len(s)
	dp := make([]int, n + 1)
	// dp[0] = 0
	for i := 2 ; i <= n ; i ++ {
		if s[i - 1] == ')'{
			if s[i - 2] == '('{
				dp[i] = dp[i - 2] + 2	
			}else{
				if i > dp[i - 1] + 1 && s[i - dp[i - 1] - 2] == '('{
					dp[i] = dp[i - dp[i - 1] -2] + dp[i - 1] + 2 	
				}
			}
		}
	}
	res := 0
	for i := 0 ; i <= n ; i ++ {
		res = max(res, dp[i])
	}
	return res 
}
func max(a, b int) int {if a > b {return a}; return b}

// @lc code=end



/*
// @lcpr case=start
// "(()"\n
// @lcpr case=end

// @lcpr case=start
// ")()())"\n
// @lcpr case=end

// @lcpr case=start
// ""\n
// @lcpr case=end

 */

