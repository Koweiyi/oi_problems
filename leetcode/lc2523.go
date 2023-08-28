/*
 * @lc app=leetcode.cn id=2523 lang=golang
 * @lcpr version=21913
 *
 * [2523] 范围内最接近的两个质数
 *
 * https://leetcode.cn/problems/closest-prime-numbers-in-range/description/
 *
 * algorithms
 * Medium (41.44%)
 * Likes:    19
 * Dislikes: 0
 * Total Accepted:    6.8K
 * Total Submissions: 16.5K
 * Testcase Example:  '10\n19'
 *
 * 给你两个正整数 left 和 right ，请你找到两个整数 num1 和 num2 ，它们满足：
 *
 *
 * left <= nums1 < nums2 <= right  。
 * nums1 和 nums2 都是 质数 。
 * nums2 - nums1 是满足上述条件的质数对中的 最小值 。
 *
 *
 * 请你返回正整数数组 ans = [nums1, nums2] 。如果有多个整数对满足上述条件，请你返回 nums1
 * 最小的质数对。如果不存在符合题意的质数对，请你返回 [-1, -1] 。
 *
 * 如果一个整数大于 1 ，且只能被 1 和它自己整除，那么它是一个质数。
 *
 *
 *
 * 示例 1：
 *
 * 输入：left = 10, right = 19
 * 输出：[11,13]
 * 解释：10 到 19 之间的质数为 11 ，13 ，17 和 19 。
 * 质数对的最小差值是 2 ，[11,13] 和 [17,19] 都可以得到最小差值。
 * 由于 11 比 17 小，我们返回第一个质数对。
 *
 *
 * 示例 2：
 *
 * 输入：left = 4, right = 6
 * 输出：[-1,-1]
 * 解释：给定范围内只有一个质数，所以题目条件无法被满足。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= left <= right <= 10^6
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
func closestPrimes(left int, right int) []int {

	// 埃氏筛 92 ms 
	mx := 1000001
	primes := make([]int, 0)
	vis := make([]bool, mx)
	for i := 2 ; i * i < mx ; i ++{
		if !vis[i]{
			for j := i * i ; j < mx ; j += i {
				vis[j] = true;
			} 
		}
	} 
	for i:= 2 ; i <= right ; i ++ {
		if !vis[i]{
			primes = append(primes, i)
		}
	}

	// 欧拉筛 200 ms 
	// for i := 2 ; i < mx ; i ++ {
	// 	if !vis[i] {
	// 		primes = append(primes, i)
	// 	}
	// 	for j := 0 ; j < len(primes) ; j ++ {
	// 		if i * primes[j] >= mx {break}
	// 		vis[i * primes[j]] = true
	// 		if i % primes[j] == 0 {break}
	// 	}
	// }
	p0, p1 := -1, -1
	i := sort.SearchInts(primes, left)
	for i + 1 < len(primes) && primes[i + 1] <= right{
		if p0 < 0 || primes[i + 1] - primes[i] < p1 - p0{
			p0, p1 = primes[i], primes[i + 1]
		}
		i ++ 
	}
	return []int{p0, p1}
}
// @lc code=end



/*
// @lcpr case=start
// 10\n19\n
// @lcpr case=end

// @lcpr case=start
// 4\n6\n
// @lcpr case=end

 */

