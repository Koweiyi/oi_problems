/*
 * @lc app=leetcode.cn id=46 lang=golang
 * @lcpr version=21913
 *
 * [46] 全排列
 *
 * https://leetcode.cn/problems/permutations/description/
 *
 * algorithms
 * Medium (78.93%)
 * Likes:    2641
 * Dislikes: 0
 * Total Accepted:    906.8K
 * Total Submissions: 1.1M
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：nums = [1,2,3]
 * 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 * 
 * 
 * 示例 2：
 * 
 * 输入：nums = [0,1]
 * 输出：[[0,1],[1,0]]
 * 
 * 
 * 示例 3：
 * 
 * 输入：nums = [1]
 * 输出：[[1]]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length <= 6
 * -10 <= nums[i] <= 10
 * nums 中的所有整数 互不相同
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
func permute(nums []int) (res [][]int) {
	n := len(nums)
	used := make([]bool, n)
	var dfs func(i int)
	p := []int{}
	dfs = func(i int) {
		if i == n{
			res = append(res, append([]int(nil), p...))
		}
		for j := 0 ; j < n ; j ++ {
			if !used[j]{
				used[j] = true
				p = append(p, nums[j])
				dfs(i + 1)
				p = p[:len(p) - 1]
				used[j] = false
			}
		}
	}
	dfs(0)
	return res 
}
// @lc code=end



/*
// @lcpr case=start
// [1,2,3]\n
// @lcpr case=end

// @lcpr case=start
// [0,1]\n
// @lcpr case=end

// @lcpr case=start
// [1]\n
// @lcpr case=end

 */

