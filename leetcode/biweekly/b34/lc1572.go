/*
 * @lc app=leetcode.cn id=1572 lang=golang
 * @lcpr version=21913
 *
 * [1572] 矩阵对角线元素的和
 *
 * https://leetcode.cn/problems/matrix-diagonal-sum/description/
 *
 * algorithms
 * Easy (80.93%)
 * Likes:    76
 * Dislikes: 0
 * Total Accepted:    37.7K
 * Total Submissions: 46.6K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * 给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。
 * 
 * 请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。
 * 
 * 
 * 
 * 示例  1：
 * 
 * 
 * 
 * 输入：mat = [[1,2,3],
 * [4,5,6],
 * [7,8,9]]
 * 输出：25
 * 解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
 * 请注意，元素 mat[1][1] = 5 只会被计算一次。
 * 
 * 
 * 示例  2：
 * 
 * 输入：mat = [[1,1,1,1],
 * [1,1,1,1],
 * [1,1,1,1],
 * [1,1,1,1]]
 * 输出：8
 * 
 * 
 * 示例 3：
 * 
 * 输入：mat = [[5]]
 * 输出：5
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * n == mat.length == mat[i].length
 * 1 <= n <= 100
 * 1 <= mat[i][j] <= 100
 * 
 * 
 */
package leetcode
type TreeNode struct {
    Val int
    Right *TreeNode
    Left *TreeNode
}
// @lc code=start
func diagonalSum(mat [][]int) int {
	res := 0
	for i := 0 ; i < len(mat) ; i ++{
		res += mat[i][i]
		res += mat[len(mat) - 1 - i][i]
	}
	if len(mat) & 1 == 1{
		res -= mat[len(mat) / 2][len(mat) / 2]
	}
	return res
	
}
// @lc code=end



/*
// @lcpr case=start
// [[1,2,3],[4,5,6],[7,8,9]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]\n
// @lcpr case=end

// @lcpr case=start
// [[5]]\n
// @lcpr case=end

 */

