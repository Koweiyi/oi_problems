/*
 * @lc app=leetcode.cn id=1362 lang=golang
 * @lcpr version=21912
 *
 * [1362] 最接近的因数
 *
 * https://leetcode.cn/problems/closest-divisors/description/
 *
 * algorithms
 * Medium (54.75%)
 * Likes:    33
 * Dislikes: 0
 * Total Accepted:    8.1K
 * Total Submissions: 14.8K
 * Testcase Example:  '8'
 *
 * 给你一个整数 num，请你找出同时满足下面全部要求的两个整数：
 *
 *
 * 两数乘积等于  num + 1 或 num + 2
 * 以绝对差进行度量，两数大小最接近
 *
 *
 * 你可以按任意顺序返回这两个整数。
 *
 *
 *
 * 示例 1：
 *
 * 输入：num = 8
 * 输出：[3,3]
 * 解释：对于 num + 1 = 9，最接近的两个因数是 3 & 3；对于 num + 2 = 10, 最接近的两个因数是 2 & 5，因此返回 3 &
 * 3 。
 *
 *
 * 示例 2：
 *
 * 输入：num = 123
 * 输出：[5,25]
 *
 *
 * 示例 3：
 *
 * 输入：num = 999
 * 输出：[40,25]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= num <= 10^9
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
// @lc code=start
func closestDivisors(num int) []int {
	res := make([]int, 2)
	dif := math.MaxInt32
	for x := 1 ; x * x <= num + 1 ; x ++ {
		v := num + 1
		if v % x == 0  && (v / x  - x) < dif{
			res[0] = x 
			res[1] = v / x 
			dif = v / x - x 
		}
	}
	for x := 1 ; x * x <= num + 2 ; x ++ {
		v := num + 2
		if v % x == 0  && (v / x  - x) < dif{
			res[0] = x 
			res[1] = v / x 
			dif = v / x - x 
		}
	}
	return res 
}
// @lc code=end



/*
// @lcpr case=start
// 8\n
// @lcpr case=end

// @lcpr case=start
// 123\n
// @lcpr case=end

// @lcpr case=start
// 999\n
// @lcpr case=end

 */

