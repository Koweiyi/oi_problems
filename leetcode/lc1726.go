/*
 * @lc app=leetcode.cn id=1726 lang=golang
 * @lcpr version=21912
 *
 * [1726] 同积元组
 *
 * https://leetcode.cn/problems/tuple-with-same-product/description/
 *
 * algorithms
 * Medium (52.26%)
 * Likes:    26
 * Dislikes: 0
 * Total Accepted:    8.2K
 * Total Submissions: 15.7K
 * Testcase Example:  '[2,3,4,6]'
 *
 * 给你一个由 不同 正整数组成的数组 nums ，请你返回满足 a * b = c * d 的元组 (a, b, c, d) 的数量。其中 a、b、c 和
 * d 都是 nums 中的元素，且 a != b != c != d 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：nums = [2,3,4,6]
 * 输出：8
 * 解释：存在 8 个满足题意的元组：
 * (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
 * (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
 * 
 * 
 * 示例 2：
 * 
 * 输入：nums = [1,2,4,5,10]
 * 输出：16
 * 解释：存在 16 个满足题意的元组：
 * (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
 * (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
 * (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,4,5)
 * (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length <= 1000
 * 1 <= nums[i] <= 10^4
 * nums 中的所有元素 互不相同
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
func tupleSameProduct(nums []int) int {
	res := 0
	record := map[int]int{}
	for i := 0 ; i < len(nums) - 1 ; i ++ {
		for j := i + 1; j < len(nums) ; j ++ {
			record[nums[i] * nums[j]] ++ 
		}
	}
	for _, v := range record{
		res += v * (v - 1) / 2 
	}
	return res * 8

}
// @lc code=end



/*
// @lcpr case=start
// [2,3,4,6]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,4,5,10]\n
// @lcpr case=end

 */

