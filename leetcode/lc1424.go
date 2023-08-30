/*
 * @lc app=leetcode.cn id=1424 lang=golang
 * @lcpr version=21913
 *
 * [1424] 对角线遍历 II
 *
 * https://leetcode.cn/problems/diagonal-traverse-ii/description/
 *
 * algorithms
 * Medium (42.33%)
 * Likes:    79
 * Dislikes: 0
 * Total Accepted:    10.7K
 * Total Submissions: 25.4K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * 给你一个列表 nums ，里面每一个元素都是一个整数列表。请你依照下面各图的规则，按顺序返回 nums 中对角线上的整数。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：nums = [[1,2,3],[4,5,6],[7,8,9]]
 * 输出：[1,4,2,7,5,3,8,6,9]
 *
 *
 * 示例 2：
 *
 *
 *
 * 输入：nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
 * 输出：[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
 *
 *
 * 示例 3：
 *
 * 输入：nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
 * 输出：[1,4,2,5,3,8,6,9,7,10,11]
 *
 *
 * 示例 4：
 *
 * 输入：nums = [[1,2,3,4,5,6]]
 * 输出：[1,2,3,4,5,6]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i].length <= 10^5
 * 1 <= nums[i][j] <= 10^9
 * nums 中最多有 10^5 个数字。
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
func findDiagonalOrder(nums [][]int) []int {
	type pair struct{val, col, row int}
	ps := []pair{}
	for i := range nums{
		for j := range nums[i]{
			ps = append(ps, pair{nums[i][j], j, i})
		}
	}
	sort.Slice(ps, func(i, j int) bool {
		t1, t2 := ps[i].col + ps[i].row, ps[j].col + ps[j].row
		return t1 < t2 || t1 == t2 && ps[i].col < ps[j].col
	})

	res := make([]int, 0)
	for i := 0 ; i < len(ps) ; i ++ {
		res = append(res, ps[i].val)
	}
	return res 
}
// @lc code=end



/*
// @lcpr case=start
// [[1,2,3],[4,5,6],[7,8,9]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,2,3],[4],[5,6,7],[8],[9,10,11]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,2,3,4,5,6]]\n
// @lcpr case=end

 */

