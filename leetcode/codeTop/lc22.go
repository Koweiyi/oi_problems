/*
 * @lc app=leetcode.cn id=22 lang=golang
 * @lcpr version=21913
 *
 * [22] 括号生成
 *
 * https://leetcode.cn/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (77.46%)
 * Likes:    3346
 * Dislikes: 0
 * Total Accepted:    729.2K
 * Total Submissions: 941.3K
 * Testcase Example:  '3'
 *
 * 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
 *
 *
 *
 * 示例 1：
 *
 * 输入：n = 3
 * 输出：["((()))","(()())","(())()","()(())","()()()"]
 *
 *
 * 示例 2：
 *
 * 输入：n = 1
 * 输出：["()"]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 8
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
func generateParenthesis(n int) (res []string) {
	path := make([]byte, 0)
	var dfs func(i, L int)
	// L 表示已添加的左括号数目，i 表示已经添加的符号数目 i - L 表示右括号数目
	dfs = func(i, L int) {
		if i == 2 * n{
			res = append(res, string(path))
			return
		}
		if L < n {
			// 左括号数目小于n, 还可以添加左括号
			path = append(path, '(')
			dfs(i + 1, L + 1)
			path = path[:len(path) - 1]
		}
		if i - L < L{
			// 右括号数目小于左括号数目，可以添加右括号
			path = append(path, ')')
			dfs(i + 1, L)
			path = path[:len(path) - 1]
		}
	}
	dfs(0, 0)
	return
}
// @lc code=end



/*
// @lcpr case=start
// 3\n
// @lcpr case=end

// @lcpr case=start
// 1\n
// @lcpr case=end

 */

