/*
 * @lc app=leetcode.cn id=2449 lang=golang
 * @lcpr version=21913
 *
 * [2449] 使数组相似的最少操作次数
 *
 * https://leetcode.cn/problems/minimum-number-of-operations-to-make-arrays-similar/description/
 *
 * algorithms
 * Hard (65.43%)
 * Likes:    25
 * Dislikes: 0
 * Total Accepted:    4K
 * Total Submissions: 6.1K
 * Testcase Example:  '[8,12,6]\n[2,14,10]'
 *
 * 给你两个正整数数组 nums 和 target ，两个数组长度相等。
 *
 * 在一次操作中，你可以选择两个 不同 的下标 i 和 j ，其中 0 <= i, j < nums.length ，并且：
 *
 *
 * 令 nums[i] = nums[i] + 2 且
 * 令 nums[j] = nums[j] - 2 。
 *
 *
 * 如果两个数组中每个元素出现的频率相等，我们称两个数组是 相似 的。
 *
 * 请你返回将 nums 变得与 target 相似的最少操作次数。测试数据保证 nums 一定能变得与 target 相似。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [8,12,6], target = [2,14,10]
 * 输出：2
 * 解释：可以用两步操作将 nums 变得与 target 相似：
 * - 选择 i = 0 和 j = 2 ，nums = [10,12,4] 。
 * - 选择 i = 1 和 j = 2 ，nums = [10,14,2] 。
 * 2 次操作是最少需要的操作次数。
 *
 *
 * 示例 2：
 *
 * 输入：nums = [1,2,5], target = [4,1,3]
 * 输出：1
 * 解释：一步操作可以使 nums 变得与 target 相似：
 * - 选择 i = 1 和 j = 2 ，nums = [1,4,3] 。
 *
 *
 * 示例 3：
 *
 * 输入：nums = [1,1,1,1,1], target = [1,1,1,1,1]
 * 输出：0
 * 解释：数组 nums 已经与 target 相似。
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == nums.length == target.length
 * 1 <= n <= 10^5
 * 1 <= nums[i], target[i] <= 10^6
 * nums 一定可以变得与 target 相似。
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
func makeSimilar(nums []int, target []int) (res int64) {
	odd1, odd2 := make([]int, 0), make([]int, 0)
	even1, even2 := make([]int, 0), make([]int, 0)

	for _, x := range nums{
		if x % 2 == 0{
			odd1 = append(odd1, x)
		}else{
			even1 = append(even1, x)
		}
	}

	for _, x := range target{
		if x % 2 == 0{
			odd2 = append(odd2, x)
		}else{
			even2 = append(even2, x)
		}
	}

	sovle := func(nums1 []int, nums2 []int) (res int64){
		sort.Ints(nums1)
		sort.Ints(nums2)
		for i := 0 ; i < len(nums1) ; i ++ {
			if nums1[i] < nums2[i]{
				res  += int64(nums2[i] - nums1[i]) / 2
			}
		}
		return 
	}

	return sovle(odd1, odd2) + sovle(even1, even2)

}
// @lc code=end



/*
// @lcpr case=start
// [8,12,6]\n[2,14,10]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,5]\n[4,1,3]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1,1,1]\n[1,1,1,1,1]\n
// @lcpr case=end

 */

