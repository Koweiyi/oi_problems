/*
 * @lc app=leetcode.cn id=300 lang=golang
 * @lcpr version=21913
 *
 * [300] 最长递增子序列
 *
 * https://leetcode.cn/problems/longest-increasing-subsequence/description/
 *
 * algorithms
 * Medium (54.91%)
 * Likes:    3323
 * Dislikes: 0
 * Total Accepted:    771.4K
 * Total Submissions: 1.4M
 * Testcase Example:  '[10,9,2,5,3,7,101,18]'
 *
 * 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
 *
 * 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7]
 * 的子序列。
 *
 *
 * 示例 1：
 *
 * 输入：nums = [10,9,2,5,3,7,101,18]
 * 输出：4
 * 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
 *
 *
 * 示例 2：
 *
 * 输入：nums = [0,1,0,3,2,3]
 * 输出：4
 *
 *
 * 示例 3：
 *
 * 输入：nums = [7,7,7,7,7,7,7]
 * 输出：1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 2500
 * -10^4 <= nums[i] <= 10^4
 *
 *
 *
 *
 * 进阶：
 *
 *
 * 你能将算法的时间复杂度降低到 O(n log(n)) 吗?
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
func lengthOfLIS(nums []int) int {
	// // O(n ^ 2) 解法
	// res := 0 
	// dp := make([]int, len(nums))
	// for i := 0 ; i < len(nums) ; i ++{
	// 	dp[i] = 1
	// 	for j := 0 ; j < i ; j ++ {
	// 		if nums[i] > nums[j]{
	// 			dp[i] = max(dp[i], dp[j] + 1)
	// 		}
	// 	}
	// 	res = max(res, dp[i])
	// } 
	// return res

	// 二分贪心 O(n * logn)
	lis := []int{}
	for _, x := range nums{
		p := sort.SearchInts(lis, x)
		if p == len(lis){
			lis = append(lis, x)
		}else{
			lis[p] = x 
		}
	}
	return len(lis)
}
func max(a, b int) int {if a > b {return a}; return b}

// @lc code=end



/*
// @lcpr case=start
// [10,9,2,5,3,7,101,18]\n
// @lcpr case=end

// @lcpr case=start
// [0,1,0,3,2,3]\n
// @lcpr case=end

// @lcpr case=start
// [7,7,7,7,7,7,7]\n
// @lcpr case=end

 */

