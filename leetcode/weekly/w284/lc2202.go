/*
 * @lc app=leetcode.cn id=2202 lang=golang
 * @lcpr version=21913
 *
 * [2202] K 次操作后最大化顶端元素
 *
 * https://leetcode.cn/problems/maximize-the-topmost-element-after-k-moves/description/
 *
 * algorithms
 * Medium (21.56%)
 * Likes:    27
 * Dislikes: 0
 * Total Accepted:    9K
 * Total Submissions: 41.8K
 * Testcase Example:  '[5,2,2,4,0,6]\n4'
 *
 * 给你一个下标从 0 开始的整数数组 nums ，它表示一个 栈 ，其中 nums[0] 是栈顶的元素。
 *
 * 每一次操作中，你可以执行以下操作 之一 ：
 *
 *
 * 如果栈非空，那么 删除 栈顶端的元素。
 * 如果存在 1 个或者多个被删除的元素，你可以从它们中选择任何一个，添加 回栈顶，这个元素成为新的栈顶元素。
 *
 *
 * 同时给你一个整数 k ，它表示你总共需要执行操作的次数。
 *
 * 请你返回 恰好 执行 k 次操作以后，栈顶元素的 最大值 。如果执行完 k 次操作以后，栈一定为空，请你返回 -1 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [5,2,2,4,0,6], k = 4
 * 输出：5
 * 解释：
 * 4 次操作后，栈顶元素为 5 的方法之一为：
 * - 第 1 次操作：删除栈顶元素 5 ，栈变为 [2,2,4,0,6] 。
 * - 第 2 次操作：删除栈顶元素 2 ，栈变为 [2,4,0,6] 。
 * - 第 3 次操作：删除栈顶元素 2 ，栈变为 [4,0,6] 。
 * - 第 4 次操作：将 5 添加回栈顶，栈变为 [5,4,0,6] 。
 * 注意，这不是最后栈顶元素为 5 的唯一方式。但可以证明，4 次操作以后 5 是能得到的最大栈顶元素。
 *
 *
 * 示例 2：
 *
 * 输入：nums = [2], k = 1
 * 输出：-1
 * 解释：
 * 第 1 次操作中，我们唯一的选择是将栈顶元素弹出栈。
 * 由于 1 次操作后无法得到一个非空的栈，所以我们返回 -1 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10^5
 * 0 <= nums[i], k <= 10^9
 *
 *
 */
package leetcode

import "sort"
type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}
// @lc code=start
func maximumTop(nums []int, k int) int {
	if len(nums) == 1 && k & 1 == 1 {
		return -1 
	}
	if k <= 1{
		return nums[k]
	}
	if k  > len(nums) {
		sort.Ints(nums)
		return nums[len(nums) - 1]
	}  
	s := nums[:k - 1]
	if k < len(nums){
		s = append(s, nums[k])
	}
	sort.Ints(s)
	return s[len(s) - 1]
}
// @lc code=end



/*
// @lcpr case=start
// [5,2,2,4,0,6]\n4\n
// @lcpr case=end

// @lcpr case=start
// [2]\n1\n
// @lcpr case=end

// @lcpr case=start
// [1,2,10000000]\n2\n
// @lcpr case=end

// @lcpr case=start
// [4,6,1,0,6,2,4]\n0\n
// @lcpr case=end
// @lcpr case=start
// [0,1,2]\n3\n
// @lcpr case=end
 */

