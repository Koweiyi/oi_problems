/*
 * @lc app=leetcode.cn id=2397 lang=golang
 * @lcpr version=21913
 *
 * [2397] 被列覆盖的最多行数
 *
 * https://leetcode.cn/problems/maximum-rows-covered-by-columns/description/
 *
 * algorithms
 * Medium (55.32%)
 * Likes:    43
 * Dislikes: 0
 * Total Accepted:    6.1K
 * Total Submissions: 11.1K
 * Testcase Example:  '[[0,0,0],[1,0,1],[0,1,1],[0,0,1]]\n2'
 *
 * 给你一个下标从 0 开始的 m x n 二进制矩阵 mat 和一个整数 cols ，表示你需要选出的列数。
 *
 * 如果一行中，所有的 1 都被你选中的列所覆盖，那么我们称这一行 被覆盖 了。
 *
 * 请你返回在选择 cols 列的情况下，被覆盖 的行数 最大 为多少。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：mat = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], cols = 2
 * 输出：3
 * 解释：
 * 如上图所示，覆盖 3 行的一种可行办法是选择第 0 和第 2 列。
 * 可以看出，不存在大于 3 行被覆盖的方案，所以我们返回 3 。
 *
 *
 * 示例 2：
 *
 *
 *
 * 输入：mat = [[1],[0]], cols = 1
 * 输出：2
 * 解释：
 * 选择唯一的一列，两行都被覆盖了，原因是整个矩阵都被覆盖了。
 * 所以我们返回 2 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == mat.length
 * n == mat[i].length
 * 1 <= m, n <= 12
 * mat[i][j] 要么是 0 要么是 1 。
 * 1 <= cols <= n
 *
 *
 */
package main

import "fmt"

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}
// @lc code=start
func maximumRows(matrix [][]int, numSelect int) int {
	m := len(matrix)
	n := len(matrix[0])
	res := 0
	nums := []int{}
	for i := 0 ; i < m ; i ++ {
		num := 0
		for j := 0 ; j < n ; j ++{
			num = (num << 1) + matrix[i][j]
		}
		nums = append(nums, num)
	}
	var dfs func (i int, num int, cnt1 int) 
	dfs = func (i, num, cnt1 int)  {
		if i == n{
			if cnt1 == numSelect{
				s := 0
				for _, x := range nums{
					if (x & num) == x {
						s ++ 
					}
				}
				res = max(res, s) 
			}
			return 
		}
		dfs(i + 1, num << 1, cnt1)
		if cnt1 < numSelect{
			dfs(i + 1, (num << 1) + 1, cnt1 + 1)
		}
	}
	dfs(0, 0, 0)
	return res 
}
func max(a, b int) int {if a > b {return a}; return b}

// @lc code=end


func main(){
	matrix := [][]int{{0,0,0}, {1,0,1},{0,1,1},{0,0,1}}
	numSelect := 2 
	res := maximumRows(matrix, numSelect)
	fmt.Println(res)
}


/*
// @lcpr case=start
// [[0,0,0],[1,0,1],[0,1,1],[0,0,1]]\n2\n
// @lcpr case=end

// @lcpr case=start
// [[1],[0]]\n1\n
// @lcpr case=end

 */

