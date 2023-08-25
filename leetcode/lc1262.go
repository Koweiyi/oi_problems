/*
 * @lc app=leetcode.cn id=1262 lang=golang
 * @lcpr version=21913
 *
 * [1262] 可被三整除的最大和
 *
 * https://leetcode.cn/problems/greatest-sum-divisible-by-three/description/
 *
 * algorithms
 * Medium (56.33%)
 * Likes:    315
 * Dislikes: 0
 * Total Accepted:    38.3K
 * Total Submissions: 68K
 * Testcase Example:  '[3,6,5,1,8]'
 *
 * 给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [3,6,5,1,8]
 * 输出：18
 * 解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
 *
 * 示例 2：
 *
 * 输入：nums = [4]
 * 输出：0
 * 解释：4 不能被 3 整除，所以无法选出数字，返回 0。
 *
 *
 * 示例 3：
 *
 * 输入：nums = [1,2,3,4,4]
 * 输出：12
 * 解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 4 * 10^4
 * 1 <= nums[i] <= 10^4
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
type ListNode struct {
    Val int
    Next *ListNode
}
// @lc code=start
func maxSumDivThree(nums []int) int {
	record := [3][]int{} 
	s := 0
	for i := 0 ; i < len(nums) ; i ++ {
		s += nums[i]
		record[nums[i] % 3] = append(record[nums[i] % 3], nums[i])
	}
	if s % 3 == 0{
		return s 
	}
	sort.Slice(record[1], func(i, j int) bool {return record[1][i] > record[1][j]})
	sort.Slice(record[2], func(i, j int) bool {return record[2][i] > record[2][j]})

	// 最多只有两个数没被选 
	res := 0
	//一个数没被选
	for i := 0 ; i < len(nums) ; i ++ {
		if (s - nums[i]) % 3 == 0{
			res = max(res, s - nums[i])
		}
	}

	// 有两个数没选
	if len(record[1]) >= 2 && (s - record[1][len(record[1]) - 1] - record[1][len(record[1]) - 2]) % 3 == 0{
		res = max(s - record[1][len(record[1]) - 1] - record[1][len(record[1]) - 2], res)  	
	}
	if len(record[2]) >= 2 && (s - record[2][len(record[2]) - 1] - record[2][len(record[2]) - 2]) % 3 == 0{
		res = max(s - record[2][len(record[2]) - 1] - record[2][len(record[2]) - 2], res)  	
	}
	return res 
}
func max(a, b int) int {if a > b {return a}; return b}
// @lc code=end



/*
// @lcpr case=start
// [3,6,5,1,8]\n
// @lcpr case=end

// @lcpr case=start
// [4]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,4]\n
// @lcpr case=end

 */

