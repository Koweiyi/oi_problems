/*
 * @lc app=leetcode.cn id=5 lang=golang
 * @lcpr version=21913
 *
 * [5] 最长回文子串
 *
 * https://leetcode.cn/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (37.68%)
 * Likes:    6708
 * Dislikes: 0
 * Total Accepted:    1.5M
 * Total Submissions: 3.9M
 * Testcase Example:  '"babad"'
 *
 * 给你一个字符串 s，找到 s 中最长的回文子串。
 *
 * 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
 *
 *
 *
 * 示例 1：
 *
 * 输入：s = "babad"
 * 输出："bab"
 * 解释："aba" 同样是符合题意的答案。
 *
 *
 * 示例 2：
 *
 * 输入：s = "cbbd"
 * 输出："bb"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 1000
 * s 仅由数字和英文字母组成
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
func longestPalindrome(s string) string {

	n := len(s)
	dp := make([][]int, n)
	for i := range dp{
		dp[i] = make([]int, n)
	}
	maxlen, start := 1, 0
	for i := 0 ; i < n ; i ++ {
		dp[i][i] = 1
	}

	for len := 2 ; len <= n ; len ++ {
		for i := 0 ; i + len - 1 < n ; i ++ {
			j := i + len - 1 
			if s[i] == s[j]{
				if len == 2 {
					dp[i][j] = 2
				}else{
					if dp[i + 1][j - 1] > 0{
						dp[i][j] = 2 + dp[i + 1][j - 1]
					}
				}
			}
			if dp[i][j] > 0{
				maxlen = len 
				start = i  
			}
		}
	}
	return s[start:start + maxlen]
}
func max(a, b int) int {if a > b {return a}; return b}

// @lc code=end



/*
// @lcpr case=start
// "babad"\n
// @lcpr case=end

// @lcpr case=start
// "cbbd"\n
// @lcpr case=end

 */

