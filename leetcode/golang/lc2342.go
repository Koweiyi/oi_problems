/*
 * @lc app=leetcode.cn id=2342 lang=golang
 * @lcpr version=30109
 *
 * [2342] 数位和相等数对的最大和
 *
 * https://leetcode.cn/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/
 *
 * algorithms
 * Medium (53.81%)
 * Likes:    65
 * Dislikes: 0
 * Total Accepted:    24.8K
 * Total Submissions: 40.9K
 * Testcase Example:  '[18,43,36,13,7]'
 *
 * 给你一个下标从 0 开始的数组 nums ，数组中的元素都是 正 整数。请你选出两个下标 i 和 j（i != j），且 nums[i] 的数位和 与
 * nums[j] 的数位和相等。
 *
 * 请你找出所有满足条件的下标 i 和 j ，找出并返回 nums[i] + nums[j] 可以得到的 最大值 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [18,43,36,13,7]
 * 输出：54
 * 解释：满足条件的数对 (i, j) 为：
 * - (0, 2) ，两个数字的数位和都是 9 ，相加得到 18 + 36 = 54 。
 * - (1, 4) ，两个数字的数位和都是 7 ，相加得到 43 + 7 = 50 。
 * 所以可以获得的最大和是 54 。
 *
 * 示例 2：
 *
 * 输入：nums = [10,12,19,14]
 * 输出：-1
 * 解释：不存在满足条件的数对，返回 -1 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^9
 *
 *
 */

// @lcpr-template-start
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
// @lcpr-template-end
// @lc code=start
func maximumSum(nums []int) int {
	mp := map[int]int{}
	res := -1 
	for i := 0 ; i < len(nums) ; i ++ {
		if val, ok := mp[sum(nums[i])] ; ok {
			res = max(res,  nums[val] + nums[i]) 
			if nums[val] < nums[i] {
				mp[sum(nums[i])] = i 
			}
		}else{
			mp[sum(nums[i])] = i 
		}
	}
	return res 
}
func sum(i int) int {
	res := 0 
	for ; i > 0 ; i /= 10 {
		res += i % 10 
	}
	return res 
}
// @lc code=end



/*
// @lcpr case=start
// [18,43,36,13,7]\n
// @lcpr case=end

// @lcpr case=start
// [10,12,19,14]\n
// @lcpr case=end

 */

