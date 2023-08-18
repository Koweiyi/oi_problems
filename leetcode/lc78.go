/*
 * @lc app=leetcode.cn id=78 lang=golang
 * @lcpr version=21913
 *
 * [78] 子集
 *
 * https://leetcode.cn/problems/subsets/description/
 *
 * algorithms
 * Medium (81.14%)
 * Likes:    2117
 * Dislikes: 0
 * Total Accepted:    661.1K
 * Total Submissions: 814.8K
 * Testcase Example:  '[1,2,3]'
 *
 * 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
 *
 * 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [1,2,3]
 * 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
 *
 *
 * 示例 2：
 *
 * 输入：nums = [0]
 * 输出：[[],[0]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10
 * -10 <= nums[i] <= 10
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
type ListNode struct {
    Val int
    Next *ListNode
}
// @lc code=start
func subsets(nums []int) (res [][]int) {
	var dfs func(i int) 
	p := []int{}
	dfs = func(i int) {
		if i == len(nums){
			res = append(res, append([]int{}, p...))
			return
		}
		dfs(i + 1)
		p = append(p, nums[i])
		dfs(i + 1)
		p = p[:len(p) - 1]
		return
	}
	dfs(0)
	return
}
// @lc code=end



/*
// @lcpr case=start
// [1,2,3]\n
// @lcpr case=end

// @lcpr case=start
// [0]\n
// @lcpr case=end

 */

