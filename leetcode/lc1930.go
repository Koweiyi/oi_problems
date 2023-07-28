/*
 * @lc app=leetcode.cn id=1930 lang=golang
 * @lcpr version=21912
 *
 * [1930] 长度为 3 的不同回文子序列
 *
 * https://leetcode.cn/problems/unique-length-3-palindromic-subsequences/description/
 *
 * algorithms
 * Medium (51.75%)
 * Likes:    31
 * Dislikes: 0
 * Total Accepted:    8.9K
 * Total Submissions: 17.1K
 * Testcase Example:  '"aabca"'
 *
 * 给你一个字符串 s ，返回 s 中 长度为 3 的不同回文子序列 的个数。
 * 
 * 即便存在多种方法来构建相同的子序列，但相同的子序列只计数一次。
 * 
 * 回文 是正着读和反着读一样的字符串。
 * 
 * 子序列 是由原字符串删除其中部分字符（也可以不删除）且不改变剩余字符之间相对顺序形成的一个新字符串。
 * 
 * 
 * 例如，"ace" 是 "abcde" 的一个子序列。
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：s = "aabca"
 * 输出：3
 * 解释：长度为 3 的 3 个回文子序列分别是：
 * - "aba" ("aabca" 的子序列)
 * - "aaa" ("aabca" 的子序列)
 * - "aca" ("aabca" 的子序列)
 * 
 * 
 * 示例 2：
 * 
 * 输入：s = "adc"
 * 输出：0
 * 解释："adc" 不存在长度为 3 的回文子序列。
 * 
 * 
 * 示例 3：
 * 
 * 输入：s = "bbcbaba"
 * 输出：4
 * 解释：长度为 3 的 4 个回文子序列分别是：
 * - "bbb" ("bbcbaba" 的子序列)
 * - "bcb" ("bbcbaba" 的子序列)
 * - "bab" ("bbcbaba" 的子序列)
 * - "aba" ("bbcbaba" 的子序列)
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 3 <= s.length <= 10^5
 * s 仅由小写英文字母组成
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
func countPalindromicSubsequence(s string) int {
	mp := make([][]int, 26)
	for i, x := range s {
		mp[x - 'a'] = append(mp[x-'a'], i)
	}
	res := 0 
	for _, x := range mp{
		if len(x) >= 3{
			res += (len(x) * (len(x) - 1) * (len(x) - 2)) / 6 
		}
		for i := 0 ; i < len(x) - 1 ; i ++ {
			res += (x[i + 1] - x[i] - 1) * (i + 1) * (len(x) - i - 1)
		}
	}
	return res 
}
// @lc code=end



/*
// @lcpr case=start
// "aabca"\n
// @lcpr case=end

// @lcpr case=start
// "adc"\n
// @lcpr case=end

// @lcpr case=start
// "bbcbaba"\n
// @lcpr case=end

 */

