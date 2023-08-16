/*
 * @lc app=leetcode.cn id=4 lang=golang
 * @lcpr version=21913
 *
 * [4] 寻找两个正序数组的中位数
 *
 * https://leetcode.cn/problems/median-of-two-sorted-arrays/description/
 *
 * algorithms
 * Hard (41.57%)
 * Likes:    6699
 * Dislikes: 0
 * Total Accepted:    989.3K
 * Total Submissions: 2.4M
 * Testcase Example:  '[1,3]\n[2]'
 *
 * 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
 *
 * 算法的时间复杂度应该为 O(log (m+n)) 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums1 = [1,3], nums2 = [2]
 * 输出：2.00000
 * 解释：合并数组 = [1,2,3] ，中位数 2
 *
 *
 * 示例 2：
 *
 * 输入：nums1 = [1,2], nums2 = [3,4]
 * 输出：2.50000
 * 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
 *
 *
 *
 *
 *
 *
 * 提示：
 *
 *
 * nums1.length == m
 * nums2.length == n
 * 0 <= m <= 1000
 * 0 <= n <= 1000
 * 1 <= m + n <= 2000
 * -10^6 <= nums1[i], nums2[i] <= 10^6
 *
 *
 */
package leetcode

import "math"
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
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	// 如何二分
	// 傻逼了 再也不复制粘贴了

	n, m := len(nums1), len(nums2)
	if n > m {
		// 保证 n <= m
		return findMedianSortedArrays(nums2, nums1)
	}

	lmx1, lmx2, rmin1, rmin2 := 0, 0, 0, 0
	c1, c2 := 0, 0
	lo, hi := 0, 2 * n
	for lo <= hi {
		c1 = lo + (hi - lo) / 2
		c2 = m + n - c1 
		if c1 == 0{
			lmx1 = math.MinInt
		}else{
			lmx1 = nums1[(c1 - 1) / 2]
		}
		if c1 == 2 * n{
			rmin1 = math.MaxInt
		}else{
			rmin1 = nums1[c1 / 2]
		}
		if c2 == 0{
			lmx2 = math.MinInt
		}else{
			lmx2 = nums2[(c2 - 1) / 2]
		}
		if c2 == 2 * m{
			rmin2 = math.MaxInt
		}else{
			rmin2 = nums2[c2 / 2]
		}
		if lmx1 > rmin2{
			hi = c1 - 1
		}else if lmx2 > rmin1{
			lo = c1 + 1
		}else{
			break
		}
	}
	return float64(max(lmx1, lmx2) + min(rmin1, rmin2)) / 2.0
}
func min(a, b int) int {if a < b {return a}; return b}
func max(a, b int) int {if a > b {return a}; return b}
// @lc code=end



/*
// @lcpr case=start
// [1,3]\n[2]\n
// @lcpr case=end

// @lcpr case=start
// [1,2]\n[3,4]\n
// @lcpr case=end

// @lcpr case=start
// [3]\n[-2,-1]\n
// @lcpr case=end
[3]
[-2,-1]
 */

