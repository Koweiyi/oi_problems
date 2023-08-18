/*
 * @lc app=leetcode.cn id=41 lang=golang
 * @lcpr version=21913
 *
 * [41] 缺失的第一个正数
 *
 * https://leetcode.cn/problems/first-missing-positive/description/
 *
 * algorithms
 * Hard (43.22%)
 * Likes:    1898
 * Dislikes: 0
 * Total Accepted:    310.6K
 * Total Submissions: 718.7K
 * Testcase Example:  '[1,2,0]'
 *
 * 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
 * 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：nums = [1,2,0]
 * 输出：3
 * 
 * 
 * 示例 2：
 * 
 * 输入：nums = [3,4,-1,1]
 * 输出：2
 * 
 * 
 * 示例 3：
 * 
 * 输入：nums = [7,8,9,11,12]
 * 输出：1
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length <= 5 * 10^5
 * -2^31 <= nums[i] <= 2^31 - 1
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
func firstMissingPositive(nums []int) int {
	n := len(nums)
	for i := 0 ; i < n ; i ++ {
		for nums[i] > 0 && nums[i] <= n && nums[i] - 1 != i{
			if nums[i] == nums[nums[i] - 1] {
				break
			}
			nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
		}
	}
	for i := 0 ; i < n ; i ++ {
		if nums[i] - 1 != i{
			return i + 1
		}
	}
	return n + 1
}
// @lc code=end



/*
// @lcpr case=start
// [1,1]\n
// @lcpr case=end

// @lcpr case=start
// [3,4,-1,1]\n
// @lcpr case=end

// @lcpr case=start
// [7,8,9,11,12]\n
// @lcpr case=end

 */

