/*
 * @lc app=leetcode.cn id=1780 lang=golang
 * @lcpr version=21912
 *
 * [1780] 判断一个数字是否可以表示成三的幂的和
 *
 * https://leetcode.cn/problems/check-if-number-is-a-sum-of-powers-of-three/description/
 *
 * algorithms
 * Medium (74.79%)
 * Likes:    117
 * Dislikes: 0
 * Total Accepted:    31.4K
 * Total Submissions: 42K
 * Testcase Example:  '12'
 *
 * 给你一个整数 n ，如果你可以将 n 表示成若干个不同的三的幂之和，请你返回 true ，否则请返回 false 。
 *
 * 对于一个整数 y ，如果存在整数 x 满足 y == 3^x ，我们称这个整数 y 是三的幂。
 *
 *
 *
 * 示例 1：
 *
 * 输入：n = 12
 * 输出：true
 * 解释：12 = 3^1 + 3^2
 *
 *
 * 示例 2：
 *
 * 输入：n = 91
 * 输出：true
 * 解释：91 = 3^0 + 3^2 + 3^4
 *
 *
 * 示例 3：
 *
 * 输入：n = 21
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 10^7
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
func checkPowersOfThree(n int) bool {
	pow3 := [15]int{}
	pow3[0] = 1
	for i := 1 ; i < 15 ; i ++{
		pow3[i] = pow3[i - 1] * 3
	}
	var dfs func(i, s int)bool
	dfs = func(i, s int) bool {
		if s == n{
			return true
		}
		if i == 15{
			return false
		} 
		return dfs(i + 1, s) || dfs(i + 1, s + pow3[i]) 
	} 
	return dfs(0, 0)
}
// @lc code=end



/*
// @lcpr case=start
// 12\n
// @lcpr case=end

// @lcpr case=start
// 91\n
// @lcpr case=end

// @lcpr case=start
// 21\n
// @lcpr case=end

 */

