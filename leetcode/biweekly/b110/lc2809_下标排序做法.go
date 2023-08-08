/*
 * @lc app=leetcode.cn id=2809 lang=golang
 * @lcpr version=21913
 *
 * [2809] 使数组和小于等于 x 的最少时间
 *
 * https://leetcode.cn/problems/minimum-time-to-make-array-sum-at-most-x/description/
 *
 * algorithms
 * Hard (28.32%)
 * Likes:    7
 * Dislikes: 0
 * Total Accepted:    552
 * Total Submissions: 1.9K
 * Testcase Example:  '[1,2,3]\n[1,2,3]\n4'
 *
 * 给你两个长度相等下标从 0 开始的整数数组 nums1 和 nums2 。每一秒，对于所有下标 0 <= i < nums1.length
 * ，nums1[i] 的值都增加 nums2[i] 。操作 完成后 ，你可以进行如下操作：
 *
 *
 * 选择任一满足 0 <= i < nums1.length 的下标 i ，并使 nums1[i] = 0 。
 *
 *
 * 同时给你一个整数 x 。
 *
 * 请你返回使 nums1 中所有元素之和 小于等于 x 所需要的 最少 时间，如果无法实现，那么返回 -1 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums1 = [1,2,3], nums2 = [1,2,3], x = 4
 * 输出：3
 * 解释：
 * 第 1 秒，我们对 i = 0 进行操作，得到 nums1 = [0,2+2,3+3] = [0,4,6] 。
 * 第 2 秒，我们对 i = 1 进行操作，得到 nums1 = [0+1,0,6+3] = [1,0,9] 。
 * 第 3 秒，我们对 i = 2 进行操作，得到 nums1 = [1+1,0+2,0] = [2,2,0] 。
 * 现在 nums1 的和为 4 。不存在更少次数的操作，所以我们返回 3 。
 *
 *
 * 示例 2：
 *
 * 输入：nums1 = [1,2,3], nums2 = [3,3,3], x = 4
 * 输出：-1
 * 解释：不管如何操作，nums1 的和总是会超过 x 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums1.length <= 10^3
 * 1 <= nums1[i] <= 10^3
 * 0 <= nums2[i] <= 10^3
 * nums1.length == nums2.length
 * 0 <= x <= 10^6
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
func minimumTime(nums1 []int, nums2 []int, x int) int {
	n, s1, s2 := len(nums1), 0, 0
	idx := make([]int, n)
	for i := 0 ; i < n ; i ++ {
		idx[i] = i 
		s1 += nums1[i]
		s2 += nums2[i]
	}
	sort.Slice(idx, func(i, j int) bool {return nums2[idx[i]] < nums2[idx[j]]})
	f := make([]int, n + 1)
	for _, i := range idx{
		for j := n ; j > 0 ; j -- {
			f[j] = max(f[j], f[j - 1] + nums1[i] + nums2[i] * j)
		}
	}
	for t, v := range f{
		if s1 + t * s2 - v <= x{
			return t
		}
	}
	return -1
	
}

func max(a, b int) int {if a > b {return a} ; return b}
// @lc code=end



/*
// @lcpr case=start
// [1,2,3]\n[1,2,3]\n4\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3]\n[3,3,3]\n4\n
// @lcpr case=end

 */

