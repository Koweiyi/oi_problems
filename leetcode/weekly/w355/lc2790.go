/*
 * @lc app=leetcode.cn id=2790 lang=golang
 * @lcpr version=21912
 *
 * [2790] 长度递增组的最大数目
 *
 * https://leetcode.cn/problems/maximum-number-of-groups-with-increasing-length/description/
 *
 * algorithms
 * Hard (18.74%)
 * Likes:    21
 * Dislikes: 0
 * Total Accepted:    1.8K
 * Total Submissions: 9.4K
 * Testcase Example:  '[1,2,5]'
 *
 * 给你一个下标从 0 开始、长度为 n 的数组 usageLimits 。
 *
 * 你的任务是使用从 0 到 n - 1 的数字创建若干组，并确保每个数字 i 在 所有组 中使用的次数总共不超过 usageLimits[i]
 * 次。此外，还必须满足以下条件：
 *
 *
 * 每个组必须由 不同 的数字组成，也就是说，单个组内不能存在重复的数字。
 * 每个组（除了第一个）的长度必须 严格大于 前一个组。
 *
 *
 * 在满足所有条件的情况下，以整数形式返回可以创建的最大组数。
 *
 *
 *
 * 示例 1：
 *
 * 输入：usageLimits = [1,2,5]
 * 输出：3
 * 解释：在这个示例中，我们可以使用 0 至多一次，使用 1 至多 2 次，使用 2 至多 5 次。
 * 一种既能满足所有条件，又能创建最多组的方式是：
 * 组 1 包含数字 [2] 。
 * 组 2 包含数字 [1,2] 。
 * 组 3 包含数字 [0,1,2] 。
 * 可以证明能够创建的最大组数是 3 。
 * 所以，输出是 3 。
 *
 * 示例 2：
 *
 * 输入：usageLimits = [2,1,2]
 * 输出：2
 * 解释：在这个示例中，我们可以使用 0 至多 2 次，使用 1 至多 1 次，使用 2 至多 2 次。
 * 一种既能满足所有条件，又能创建最多组的方式是：
 * 组 1 包含数字 [0] 。
 * 组 2 包含数字 [1,2] 。
 * 可以证明能够创建的最大组数是 2 。
 * 所以，输出是 2 。
 *
 *
 * 示例 3：
 *
 * 输入：usageLimits = [1,1]
 * 输出：1
 * 解释：在这个示例中，我们可以使用 0 和 1 至多 1 次。
 * 一种既能满足所有条件，又能创建最多组的方式是：
 * 组 1 包含数字 [0] 。
 * 可以证明能够创建的最大组数是 1 。
 * 所以，输出是 1 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= usageLimits.length <= 10^5
 * 1 <= usageLimits[i] <= 10^9
 *
 *
 */
package main

import "sort"

// @lc code=start
func maxIncreasingGroups(usageLimits []int) int {
	res := 0
	sort.Ints(usageLimits)
	s := 0
	for _, x := range usageLimits{
		s += x
		if (res + 1) * (res + 2) / 2 <= s{
			res ++
		}
	}
	return res
}
// @lc code=end



/*
// @lcpr case=start
// [1,2,5]\n
// @lcpr case=end

// @lcpr case=start
// [2,1,2]\n
// @lcpr case=end

// @lcpr case=start
// [1,1]\n
// @lcpr case=end

 */

