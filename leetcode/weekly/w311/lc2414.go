/*
 * @lc app=leetcode.cn id=2414 lang=golang
 * @lcpr version=21913
 *
 * [2414] 最长的字母序连续子字符串的长度
 *
 * https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring/description/
 *
 * algorithms
 * Medium (60.32%)
 * Likes:    11
 * Dislikes: 0
 * Total Accepted:    12.2K
 * Total Submissions: 20.2K
 * Testcase Example:  '"abacaba"'
 *
 * 字母序连续字符串 是由字母表中连续字母组成的字符串。换句话说，字符串 "abcdefghijklmnopqrstuvwxyz" 的任意子字符串都是
 * 字母序连续字符串 。
 * 
 * 
 * 例如，"abc" 是一个字母序连续字符串，而 "acb" 和 "za" 不是。
 * 
 * 
 * 给你一个仅由小写英文字母组成的字符串 s ，返回其 最长 的 字母序连续子字符串 的长度。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：s = "abacaba"
 * 输出：2
 * 解释：共有 4 个不同的字母序连续子字符串 "a"、"b"、"c" 和 "ab" 。
 * "ab" 是最长的字母序连续子字符串。
 * 
 * 
 * 示例 2：
 * 
 * 输入：s = "abcde"
 * 输出：5
 * 解释："abcde" 是最长的字母序连续子字符串。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <= 10^5
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
// @lc code=start
func longestContinuousSubstring(s string) int {
	res := 0  
	for l := 0 ; l < len(s) ; l ++ {
		r := l
		for ; r + 1 < len(s) && s[r + 1] - s[r] == 1 ; r ++ {}
		res = max(res, r - l + 1)
		l = r 
	} 
	return res 
}
func max(a, b int) int {if a > b {return a}; return b}

// @lc code=end



/*
// @lcpr case=start
// "abacaba"\n
// @lcpr case=end

// @lcpr case=start
// "abcde"\n
// @lcpr case=end

 */

