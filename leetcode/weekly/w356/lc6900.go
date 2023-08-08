/*
 * @lc app=leetcode.cn id=6900 lang=golang
 * @lcpr version=21913
 *
 * [6900] 统计完全子数组的数目
 *
 * https://leetcode.cn/problems/count-complete-subarrays-in-an-array/description/
 *
 * algorithms
 * Medium (54.37%)
 * Likes:    6
 * Dislikes: 0
 * Total Accepted:    4.4K
 * Total Submissions: 8.1K
 * Testcase Example:  '[1,3,1,2,2]'
 *
 * 给你一个由 正 整数组成的数组 nums 。
 * 
 * 如果数组中的某个子数组满足下述条件，则称之为 完全子数组 ：
 * 
 * 
 * 子数组中 不同 元素的数目等于整个数组不同元素的数目。
 * 
 * 
 * 返回数组中 完全子数组 的数目。
 * 
 * 子数组 是数组中的一个连续非空序列。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：nums = [1,3,1,2,2]
 * 输出：4
 * 解释：完全子数组有：[1,3,1,2]、[1,3,1,2,2]、[3,1,2] 和 [3,1,2,2] 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：nums = [5,5,5,5]
 * 输出：10
 * 解释：数组仅由整数 5 组成，所以任意子数组都满足完全子数组的条件。子数组的总数为 10 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length <= 1000
 * 1 <= nums[i] <= 2000
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
func countCompleteSubarrays(nums []int) int {
	s := map[int]struct{}{}
	for _, x := range nums{
		s[x] = struct{}{}
	}
	m := len(s)

	l, res := 0, 0
	cnt := map[int]int{}
	for _, v := range nums{
		cnt[v] ++ 
		for len(cnt) == m{
			x := nums[l]
			cnt[x] --
			if cnt[x] == 0 { delete(cnt, x) }
			l ++
		}
		res += l
	}
	return res 
}
// @lc code=end



/*
// @lcpr case=start
// [1,3,1,2,2]\n
// @lcpr case=end

// @lcpr case=start
// [5,5,5,5]\n
// @lcpr case=end

 */

