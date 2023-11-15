/*
 * @lc app=leetcode.cn id=164 lang=golang
 * @lcpr version=30109
 *
 * [164] 最大间距
 *
 * https://leetcode.cn/problems/maximum-gap/description/
 *
 * algorithms
 * Medium (60.05%)
 * Likes:    599
 * Dislikes: 0
 * Total Accepted:    89K
 * Total Submissions: 148.2K
 * Testcase Example:  '[3,6,9,1]'
 *
 * 给定一个无序的数组 nums，返回 数组在排序之后，相邻元素之间最大的差值 。如果数组元素个数小于 2，则返回 0 。
 *
 * 您必须编写一个在「线性时间」内运行并使用「线性额外空间」的算法。
 *
 *
 *
 * 示例 1:
 *
 * 输入: nums = [3,6,9,1]
 * 输出: 3
 * 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
 *
 * 示例 2:
 *
 * 输入: nums = [10]
 * 输出: 0
 * 解释: 数组元素个数小于 2，因此返回 0。
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= nums.length <= 10^5
 * 0 <= nums[i] <= 10^9
 *
 *
 */

// @lcpr-template-start
package leetcode

import "slices"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
type ListNode struct {
	Val  int
	Next *ListNode
}

// @lcpr-template-end
// @lc code=start
func maximumGap(nums []int) int {
	// slices.Sort(nums)
	n := len(nums) 
	if n < 2 {
		return 0 
	}
	res := 0 
	mn, mx := slices.Min(nums), slices.Max(nums)

	d := max(1, (mx - mn) / (n - 1)) 
	type pair struct{first, second int} 
	box := make([]pair, (mx - mn) / d + 1)

	for i := range box {
		box[i] = pair{-1, -1} 
	}

	for _, x := range nums{
		if box[(x - mn) /d].first == -1{
			box[(x - mn) / d].first = x 
			box[(x - mn) / d].second = x 
		}else{
			box[(x - mn) / d].first = min(box[(x - mn) / d].first, x)
			box[(x - mn) / d].second = max(box[(x - mn) / d].second, x)
		}
	}

	pre := -1 
	for i, b := range box {
		if b.first == -1{
			continue
		}
		if pre != -1{
			res = max(res, b.first - box[pre].second)
		}
		pre = i
	}
	return res 
}

// @lc code=end

/*
// @lcpr case=start
// [3,6,9,1]\n
// @lcpr case=end

// @lcpr case=start
// [10]\n
// @lcpr case=end

*/
