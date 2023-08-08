/*
 * @lc app=leetcode.cn id=1695 lang=golang
 * @lcpr version=21912
 *
 * [1695] 删除子数组的最大得分
 *
 * https://leetcode.cn/problems/maximum-erasure-value/description/
 *
 * algorithms
 * Medium (51.98%)
 * Likes:    67
 * Dislikes: 0
 * Total Accepted:    14.3K
 * Total Submissions: 27.5K
 * Testcase Example:  '[4,2,4,5,6]'
 *
 * 给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。
 *
 * 返回 只删除一个 子数组可获得的 最大得分 。
 *
 * 如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [4,2,4,5,6]
 * 输出：17
 * 解释：最优子数组是 [2,4,5,6]
 *
 *
 * 示例 2：
 *
 * 输入：nums = [5,2,1,2,5,2,1,2,5]
 * 输出：8
 * 解释：最优子数组是 [5,2,1] 或 [1,2,5]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^4
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
func maximumUniqueSubarray(nums []int) int {
	l, res := 0, 0 
	record := map[int]int{}
	s := make([]int, len(nums) + 1)
	for i := 1 ; i < len(s) ; i ++ {
		s[i] = s[i - 1] + nums[i - 1]
	}
	for i := 0 ; i < len(nums) ; i ++ {
		record[nums[i]] ++
		for record[nums[i]] > 1{
			record[nums[l]] --
			l ++
		}
		res = max(res, s[i + 1] - s[l])
	}
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
// [4,2,4,5,6]\n
// @lcpr case=end

// @lcpr case=start
// [5,2,1,2,5,2,1,2,5]\n
// @lcpr case=end

 */

