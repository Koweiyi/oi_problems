/*
 * @lc app=leetcode.cn id=2800 lang=golang
 * @lcpr version=21913
 *
 * [2800] 包含三个字符串的最短字符串
 *
 * https://leetcode.cn/problems/shortest-string-that-contains-three-strings/description/
 *
 * algorithms
 * Medium (34.03%)
 * Likes:    15
 * Dislikes: 0
 * Total Accepted:    4K
 * Total Submissions: 11.9K
 * Testcase Example:  '"abc"\n"bca"\n"aaa"'
 *
 * 给你三个字符串 a ，b 和 c ， 你的任务是找到长度 最短 的字符串，且这三个字符串都是它的 子字符串 。
 * 如果有多个这样的字符串，请你返回 字典序最小 的一个。
 *
 * 请你返回满足题目要求的字符串。
 *
 * 注意：
 *
 *
 * 两个长度相同的字符串 a 和 b ，如果在第一个不相同的字符处，a 的字母在字母表中比 b 的字母 靠前 ，那么字符串 a 比字符串 b 字典序小
 * 。
 * 子字符串 是一个字符串中一段连续的字符序列。
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：a = "abc", b = "bca", c = "aaa"
 * 输出："aaabca"
 * 解释：字符串 "aaabca" 包含所有三个字符串：a = ans[2...4] ，b = ans[3..5] ，c = ans[0..2]
 * 。结果字符串的长度至少为 6 ，且"aaabca" 是字典序最小的一个。
 *
 * 示例 2：
 *
 * 输入：a = "ab", b = "ba", c = "aba"
 * 输出："aba"
 * 解释：字符串 "aba" 包含所有三个字符串：a = ans[0..1] ，b = ans[1..2] ，c = ans[0..2] 。由于 c
 * 的长度为 3 ，结果字符串的长度至少为 3 。"aba" 是字典序最小的一个。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= a.length, b.length, c.length <= 100
 * a ，b ，c 只包含小写英文字母。
 *
 *
 */
package leetcode

import (
	"strings"
)
type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}
// @lc code=start	
func merge(x, y string) string {
	if strings.Contains(x, y){
		return x
	}
	if strings.Contains(y, x){
		return y
	}
	for i := min(len(x), len(y)) ;  ; i --{
		if x[len(x) - i:] ==y[:i] {
			return x + y[i:]
		}
	}
}
func min(a, b int) int {if a < b {return a}; return b}
func minimumString(a string, b string, c string)(res string) {

	strs := []string{a, b, c}
	for _, o := range [][]int{{0,1,2}, {0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}}{
		x, y, z := strs[o[0]], strs[o[1]], strs[o[2]]
		f := merge(merge(x, y), z)
		if res == "" || len(f) < len(res) || len(f) == len(res) && f < res{
			res = f
		}
	}
	return res 

}
// @lc code=end



/*
// @lcpr case=start
// "abc"\n"bca"\n"aaa"\n
// @lcpr case=end

// @lcpr case=start
// "ab"\n"ba"\n"aba"\n
// @lcpr case=end

// @lcpr case=start
// "ca"\n"ab"\n"cabc"\n
// @lcpr case=end
 */

