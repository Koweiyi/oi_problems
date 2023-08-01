/*
 * @lc app=leetcode.cn id=2730 lang=golang
 * @lcpr version=21912
 *
 * [2730] 找到最长的半重复子字符串
 *
 * https://leetcode.cn/problems/find-the-longest-semi-repetitive-substring/description/
 *
 * algorithms
 * Medium (46.13%)
 * Likes:    14
 * Dislikes: 0
 * Total Accepted:    3.5K
 * Total Submissions: 7.6K
 * Testcase Example:  '"52233"'
 *
 * 给你一个下标从 0 开始的字符串 s ，这个字符串只包含 0 到 9 的数字字符。
 * 
 * 如果一个字符串 t 中至多有一对相邻字符是相等的，那么称这个字符串 t 是 半重复的 。例如，0010 、002020 、0123 、2002 和
 * 54944 是半重复字符串，而 00101022 和 1101234883 不是。
 * 
 * 请你返回 s 中最长 半重复 子字符串的长度。
 * 
 * 一个 子字符串 是一个字符串中一段连续 非空 的字符。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：s = "52233"
 * 输出：4
 * 解释：最长半重复子字符串是 "5223" ，子字符串从 i = 0 开始，在 j = 3 处结束。
 * 
 * 
 * 示例 2：
 * 
 * 输入：s = "5494"
 * 输出：4
 * 解释：s 就是一个半重复字符串，所以答案为 4 。
 * 
 * 
 * 示例 3：
 * 
 * 输入：s = "1111111"
 * 输出：2
 * 解释：最长半重复子字符串是 "11" ，子字符串从 i = 0 开始，在 j = 1 处结束。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <= 50
 * '0' <= s[i] <= '9'
 * 
 * 
 */
package leetcode
// @lc code=start
func longestSemiRepetitiveSubstring(s string) int {
	idx := []int{}
	for i := 0 ; i < len(s) - 1 ; i ++ {
		if s[i] == s[i + 1]{
			idx = append(idx, i)
		}
	}	
	if len(idx) <= 1{
		return len(s)
	}
	res := idx[1] + 1
	for i := 2 ; i < len(idx) ; i ++{
		res = max(res, idx[i] - idx[i - 2])
	}
	res = max(res, len(s) - 1 - idx[len(idx) - 2])
	return res 
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
// "52233"\n
// @lcpr case=end

// @lcpr case=start
// "5494"\n
// @lcpr case=end

// @lcpr case=start
// "1111111"\n
// @lcpr case=end

 */

