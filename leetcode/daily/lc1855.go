/*
 * @lc app=leetcode.cn id=1855 lang=golang
 * @lcpr version=21912
 *
 * [1855] 下标对中的最大距离
 *
 * https://leetcode.cn/problems/maximum-distance-between-a-pair-of-values/description/
 *
 * algorithms
 * Medium (59.36%)
 * Likes:    72
 * Dislikes: 0
 * Total Accepted:    21.6K
 * Total Submissions: 36.3K
 * Testcase Example:  '[55,30,5,4,2]\n[100,20,10,10,5]'
 *
 * 给你两个 非递增 的整数数组 nums1​​​​​​ 和 nums2​​​​​​ ，数组下标均 从 0 开始 计数。
 * 
 * 下标对 (i, j) 中 0 <= i < nums1.length 且 0 <= j < nums2.length 。如果该下标对同时满足 i <=
 * j 且 nums1[i] <= nums2[j] ，则称之为 有效 下标对，该下标对的 距离 为 j - i​​ 。​​
 * 
 * 返回所有 有效 下标对 (i, j) 中的 最大距离 。如果不存在有效下标对，返回 0 。
 * 
 * 一个数组 arr ，如果每个 1 <= i < arr.length 均有 arr[i-1] >= arr[i] 成立，那么该数组是一个 非递增
 * 数组。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
 * 输出：2
 * 解释：有效下标对是 (0,0), (2,2), (2,3), (2,4), (3,3), (3,4) 和 (4,4) 。
 * 最大距离是 2 ，对应下标对 (2,4) 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：nums1 = [2,2,2], nums2 = [10,10,1]
 * 输出：1
 * 解释：有效下标对是 (0,0), (0,1) 和 (1,1) 。
 * 最大距离是 1 ，对应下标对 (0,1) 。
 * 
 * 示例 3：
 * 
 * 输入：nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
 * 输出：2
 * 解释：有效下标对是 (2,2), (2,3), (2,4), (3,3) 和 (3,4) 。
 * 最大距离是 2 ，对应下标对 (2,4) 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums1.length <= 10^5
 * 1 <= nums2.length <= 10^5
 * 1 <= nums1[i], nums2[j] <= 10^5
 * nums1 和 nums2 都是 非递增 数组
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
func maxDistance(nums1 []int, nums2 []int) int {
	i, j, res := 0, 0, 0
	for ; i < len(nums1) ; i ++ {
		if nums2[j] < nums1[i] {
			continue
		}
		for ; j + 1 < len(nums2) && nums2[j + 1] >= nums1[i] ; j ++{}
		if j >= i {
			if j - i > res{
				res = j - i 
			}
		}
	}
	return res 
}
// @lc code=end



/*
// @lcpr case=start
// [55,30,5,4,2]\n[100,20,10,10,5]\n
// @lcpr case=end

// @lcpr case=start
// [2,2,2]\n[10,10,1]\n
// @lcpr case=end

// @lcpr case=start
// [30,29,19,5]\n[25,25,25,25,25]\n
// @lcpr case=end

 */

