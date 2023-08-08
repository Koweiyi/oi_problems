/*
 * @lc app=leetcode.cn id=2485 lang=golang
 * @lcpr version=21912
 *
 * [2485] 找出中枢整数
 *
 * https://leetcode.cn/problems/find-the-pivot-integer/description/
 *
 * algorithms
 * Easy (80.69%)
 * Likes:    54
 * Dislikes: 0
 * Total Accepted:    29.9K
 * Total Submissions: 37K
 * Testcase Example:  '8'
 *
 * 给你一个正整数 n ，找出满足下述条件的 中枢整数 x ：
 * 
 * 
 * 1 和 x 之间的所有元素之和等于 x 和 n 之间所有元素之和。
 * 
 * 
 * 返回中枢整数 x 。如果不存在中枢整数，则返回 -1 。题目保证对于给定的输入，至多存在一个中枢整数。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：n = 8
 * 输出：6
 * 解释：6 是中枢整数，因为 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：n = 1
 * 输出：1
 * 解释：1 是中枢整数，因为 1 = 1 。
 * 
 * 
 * 示例 3：
 * 
 * 输入：n = 4
 * 输出：-1
 * 解释：可以证明不存在满足题目要求的整数。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n <= 1000
 * 
 * 
 */
package leetcode
// @lc code=start
func pivotInteger(n int) int {
	l, r := 0, n + 1
	for l + 1 < r{
		mid := l + (r - l) / 2
		x, y := mid * (mid + 1), (mid + n) * (n - mid + 1)
		if x == y {
			return mid
		}else if x > y {
			r = mid
		}else{
			l = mid
		}
	}
	return -1
}
// @lc code=end



/*
// @lcpr case=start
// 8\n
// @lcpr case=end

// @lcpr case=start
// 1\n
// @lcpr case=end

// @lcpr case=start
// 4\n
// @lcpr case=end

 */

