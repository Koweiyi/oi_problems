/*
 * @lc app=leetcode.cn id=1673 lang=golang
 * @lcpr version=21913
 *
 * [1673] 找出最具竞争力的子序列
 *
 * https://leetcode.cn/problems/find-the-most-competitive-subsequence/description/
 *
 * algorithms
 * Medium (39.80%)
 * Likes:    107
 * Dislikes: 0
 * Total Accepted:    12.1K
 * Total Submissions: 30.5K
 * Testcase Example:  '[3,5,2,6]\n2'
 *
 * 给你一个整数数组 nums 和一个正整数 k ，返回长度为 k 且最具 竞争力 的 nums 子序列。
 *
 * 数组的子序列是从数组中删除一些元素（可能不删除元素）得到的序列。
 *
 * 在子序列 a 和子序列 b 第一个不相同的位置上，如果 a 中的数字小于 b 中对应的数字，那么我们称子序列 a 比子序列 b（相同长度下）更具 竞争力
 * 。 例如，[1,3,4] 比 [1,3,5] 更具竞争力，在第一个不相同的位置，也就是最后一个位置上， 4 小于 5 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [3,5,2,6], k = 2
 * 输出：[2,6]
 * 解释：在所有可能的子序列集合 {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]} 中，[2,6] 最具竞争力。
 *
 *
 * 示例 2：
 *
 * 输入：nums = [2,4,3,3,5,4,9,6], k = 4
 * 输出：[2,3,3,4]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10^5
 * 0 <= nums[i] <= 10^9
 * 1 <= k <= nums.length
 *
 *
 */
package leetcode

import "sort"
type TreeNode struct {
    Val int
    Right *TreeNode
    Left *TreeNode
}
// @lc code=start
func mostCompetitive(nums []int, k int) []int {
	res := make([]int, 0, k)
	for i, x := range nums{
		if len(res) == 0{
			res = append(res, x)
		}else{
			j := sort.SearchInts(res, x + 1)
			if j == len(res){
				if len(res) < k{
					res = append(res, x)
				}
			}else{
				if j + len(nums) - i >= k{
					res[j] = x 
					res = res[:j + 1]
				}else{
					jr := k - len(nums) + i 
					if jr < len(res){
						res[jr] = x
						res = res[:jr + 1]
					}else{
						res = append(res, x)
					}
				}
			}
		}
	}
	return res 

}
// @lc code=end



/*
// @lcpr case=start
// [3,5,2,6]\n2\n
// @lcpr case=end

// @lcpr case=start
// [2,4,3,3,5,4,9,6]\n4\n
// @lcpr case=end

 */

