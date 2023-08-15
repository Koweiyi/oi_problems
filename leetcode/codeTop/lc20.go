/*
 * @lc app=leetcode.cn id=20 lang=golang
 * @lcpr version=21913
 *
 * [20] 有效的括号
 *
 * https://leetcode.cn/problems/valid-parentheses/description/
 *
 * algorithms
 * Easy (43.99%)
 * Likes:    4079
 * Dislikes: 0
 * Total Accepted:    1.6M
 * Total Submissions: 3.5M
 * Testcase Example:  '"()"'
 *
 * 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
 *
 * 有效字符串需满足：
 *
 *
 * 左括号必须用相同类型的右括号闭合。
 * 左括号必须以正确的顺序闭合。
 * 每个右括号都有一个对应的相同类型的左括号。
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：s = "()"
 * 输出：true
 *
 *
 * 示例 2：
 *
 * 输入：s = "()[]{}"
 * 输出：true
 *
 *
 * 示例 3：
 *
 * 输入：s = "(]"
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 10^4
 * s 仅由括号 '()[]{}' 组成
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
func isValid(s string) bool {
	st := []byte{}
	match := func (b, a byte) bool {
		return a == '(' && b == ')' || a == '[' && b == ']' || a == '{' && b == '}'
	}
	for i := 0 ; i < len(s) ; i ++ {
		if s[i] == '(' || s[i] == '[' || s[i] == '{' {
			st = append(st, s[i])
		}else{
			if len(st) == 0 || !match(s[i], st[len(st) - 1]) {
				return false
			}
			st = st[:len(st) - 1]
		}
	}
	return len(st) == 0
}
// @lc code=end



/*
// @lcpr case=start
// "()"\n
// @lcpr case=end

// @lcpr case=start
// "()[]{}"\n
// @lcpr case=end

// @lcpr case=start
// "(]"\n
// @lcpr case=end

 */

