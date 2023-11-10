/*
 * @lc app=leetcode.cn id=1849 lang=golang
 * @lcpr version=21913
 *
 * [1849] 将字符串拆分为递减的连续值
 *
 * https://leetcode.cn/problems/splitting-a-string-into-descending-consecutive-values/description/
 *
 * algorithms
 * Medium (33.30%)
 * Likes:    36
 * Dislikes: 0
 * Total Accepted:    7.7K
 * Total Submissions: 23.1K
 * Testcase Example:  '"1234"'
 *
 * 给你一个仅由数字组成的字符串 s 。
 *
 * 请你判断能否将 s 拆分成两个或者多个 非空子字符串 ，使子字符串的 数值 按 降序 排列，且每两个 相邻子字符串 的数值之 差 等于 1
 * 。
 *
 *
 * 例如，字符串 s = "0090089" 可以拆分成 ["0090", "089"] ，数值为 [90,89] 。这些数值满足按降序排列，且相邻值相差
 * 1 ，这种拆分方法可行。
 * 另一个例子中，字符串 s = "001" 可以拆分成 ["0", "01"]、["00", "1"] 或 ["0", "0", "1"]
 * 。然而，所有这些拆分方法都不可行，因为对应数值分别是 [0,1]、[0,1] 和 [0,0,1] ，都不满足按降序排列的要求。
 *
 *
 * 如果可以按要求拆分 s ，返回 true ；否则，返回 false 。
 *
 * 子字符串 是字符串中的一个连续字符序列。
 *
 *
 *
 * 示例 1：
 *
 * 输入：s = "1234"
 * 输出：false
 * 解释：不存在拆分 s 的可行方法。
 *
 *
 * 示例 2：
 *
 * 输入：s = "050043"
 * 输出：true
 * 解释：s 可以拆分为 ["05", "004", "3"] ，对应数值为 [5,4,3] 。
 * 满足按降序排列，且相邻值相差 1 。
 *
 *
 * 示例 3：
 *
 * 输入：s = "9080701"
 * 输出：false
 * 解释：不存在拆分 s 的可行方法。
 *
 *
 * 示例 4：
 *
 * 输入：s = "10009998"
 * 输出：true
 * 解释：s 可以拆分为 ["100", "099", "98"] ，对应数值为 [100,99,98] 。
 * 满足按降序排列，且相邻值相差 1 。
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 20
 * s 仅由数字组成
 *
 *
 */
package leetcode

import (
	"strconv"
)
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
func splitString(s string) bool {

	var dfs func(i, pre, pre_num, cnt int) bool
	dfs = func(i, pre, pre_num, cnt int) bool {
		if i == len(s){
			if pre == len(s) && cnt > 1{
				return true
			}
			return false
		}
		// 枚举分割与否
		// 不进行分割
		res := false
		res = res || dfs(i + 1, pre, pre_num, cnt)
		// 如果可以进行分割的话

		num, _ := strconv.Atoi(s[pre:i + 1])
		if pre_num == -1 || pre_num == num + 1{
			res = res || dfs(i + 1, i + 1, num, cnt + 1)
		} 
		return res 
	}
	return dfs(0, 0, -1, 0)
}
// @lc code=end



/*
// @lcpr case=start
// "1234"\n
// @lcpr case=end

// @lcpr case=start
// "050043"\n
// @lcpr case=end

// @lcpr case=start
// "9080701"\n
// @lcpr case=end

// @lcpr case=start
// "10009998"\n
// @lcpr case=end

// @lcpr case=start
// "94650723337775781477"\n
// @lcpr case=end
 */
