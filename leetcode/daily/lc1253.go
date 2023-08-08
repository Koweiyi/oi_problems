/*
 * @lc app=leetcode.cn id=1253 lang=golang
 * @lcpr version=21912
 *
 * [1253] 重构 2 行二进制矩阵
 *
 * https://leetcode.cn/problems/reconstruct-a-2-row-binary-matrix/description/
 *
 * algorithms
 * Medium (48.29%)
 * Likes:    81
 * Dislikes: 0
 * Total Accepted:    22.4K
 * Total Submissions: 46.4K
 * Testcase Example:  '2\n1\n[1,1,1]'
 *
 * 给你一个 2 行 n 列的二进制数组：
 * 
 * 
 * 矩阵是一个二进制矩阵，这意味着矩阵中的每个元素不是 0 就是 1。
 * 第 0 行的元素之和为 upper。
 * 第 1 行的元素之和为 lower。
 * 第 i 列（从 0 开始编号）的元素之和为 colsum[i]，colsum 是一个长度为 n 的整数数组。
 * 
 * 
 * 你需要利用 upper，lower 和 colsum 来重构这个矩阵，并以二维整数数组的形式返回它。
 * 
 * 如果有多个不同的答案，那么任意一个都可以通过本题。
 * 
 * 如果不存在符合要求的答案，就请返回一个空的二维数组。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：upper = 2, lower = 1, colsum = [1,1,1]
 * 输出：[[1,1,0],[0,0,1]]
 * 解释：[[1,0,1],[0,1,0]] 和 [[0,1,1],[1,0,0]] 也是正确答案。
 * 
 * 
 * 示例 2：
 * 
 * 输入：upper = 2, lower = 3, colsum = [2,2,1,1]
 * 输出：[]
 * 
 * 
 * 示例 3：
 * 
 * 输入：upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
 * 输出：[[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= colsum.length <= 10^5
 * 0 <= upper, lower <= colsum.length
 * 0 <= colsum[i] <= 2
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
func reconstructMatrix(upper int, lower int, colsum []int) (res [][]int) {
	res = make([][]int, 2)	
	for _, x := range colsum {
		if x == 2{
			if upper <= 0 || lower <= 0{
				return nil
			}
			res[0] = append(res[0], 1)
			res[1] = append(res[1], 1)
			upper --
			lower --
		}
		if x == 0 {
			res[0] = append(res[0], 0)
			res[1] = append(res[1], 0)
		}
		if x == 1{
			if upper <= 0 && lower <= 0{
				return nil
			}
			if upper >= lower{
				res[0] = append(res[0], 1)
				upper --
				res[1] = append(res[1], 0)
			}else {
				res[1] = append(res[1], 1)
				lower --
				res[0] = append(res[0], 0)
			}
		}
	}
	if upper !=  0 || lower != 0{
		return nil
	}
	return
}
// @lc code=end



/*
// @lcpr case=start
// 2\n1\n[1,1,1]\n
// @lcpr case=end

// @lcpr case=start
// 2\n3\n[2,2,1,1]\n
// @lcpr case=end

// @lcpr case=start
// 5\n5\n[2,1,2,0,1,0,1,2,0,1]\n
// @lcpr case=end

 */

