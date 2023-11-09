/*
 * @lc app=leetcode.cn id=1878 lang=golang
 * @lcpr version=21913
 *
 * [1878] 矩阵中最大的三个菱形和
 *
 * https://leetcode.cn/problems/get-biggest-three-rhombus-sums-in-a-grid/description/
 *
 * algorithms
 * Medium (45.83%)
 * Likes:    23
 * Dislikes: 0
 * Total Accepted:    3.2K
 * Total Submissions: 7K
 * Testcase Example:  '[[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]'
 *
 * 给你一个 m x n 的整数矩阵 grid 。
 *
 * 菱形和 指的是 grid 中一个正菱形 边界
 * 上的元素之和。本题中的菱形必须为正方形旋转45度，且四个角都在一个格子当中。下图是四个可行的菱形，每个菱形和应该包含的格子都用了相应颜色标注在图中。
 *
 *
 *
 * 注意，菱形可以是一个面积为 0 的区域，如上图中右下角的紫色菱形所示。
 *
 * 请你按照 降序 返回 grid 中三个最大的 互不相同的菱形和 。如果不同的和少于三个，则将它们全部返回。
 *
 *
 *
 * 示例 1：
 *
 * 输入：grid =
 * [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
 * 输出：[228,216,211]
 * 解释：最大的三个菱形和如上图所示。
 * - 蓝色：20 + 3 + 200 + 5 = 228
 * - 红色：200 + 2 + 10 + 4 = 216
 * - 绿色：5 + 200 + 4 + 2 = 211
 *
 *
 * 示例 2：
 *
 * 输入：grid = [[1,2,3],[4,5,6],[7,8,9]]
 * 输出：[20,9,8]
 * 解释：最大的三个菱形和如上图所示。
 * - 蓝色：4 + 2 + 6 + 8 = 20
 * - 红色：9 （右下角红色的面积为 0 的菱形）
 * - 绿色：8 （下方中央面积为 0 的菱形）
 *
 *
 * 示例 3：
 *
 * 输入：grid = [[7,7,7]]
 * 输出：[7]
 * 解释：所有三个可能的菱形和都相同，所以返回 [7] 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 100
 * 1 <= grid[i][j] <= 10^5
 *
 *
 */
package leetcode

import (
	"sort"
)
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
func getBiggestThree(grid [][]int) []int {
	m, n := len(grid), len(grid[0])

	sl := make([][]int, m + 1)
	for i := range sl{
		sl[i] = make([]int, n + 1)
	} 
	sr := make([][]int, m + 1)
	for i := range sr{
		sr[i] = make([]int, n + 1)
	}

	for i := 0 ; i < m ; i ++ {
		for j := 0 ; j < n ; j ++ {
			sl[i + 1][j + 1] = sl[i][j] + grid[i][j]
		}
	}
	for i := 0 ; i < m ; i ++ {
		for j := n - 1; j >= 0 ; j -- {
			sr[i + 1][j] = sr[i][j + 1] + grid[i][j]
		}
	}

	record := map[int]struct{}{}
	res := []int{}
	for i := 0 ; i < m ; i ++ {
		for j := 0 ; j < n ; j ++ {
			// 枚举菱形长度 长度为1直接就是元素本身 
			if _, ok := record[grid[i][j]]; !ok{
				res = append(res, grid[i][j])
				record[grid[i][j]] = struct{}{}
			}

			for len := 2 ; j - len + 1 >= 0 && j + len - 1 < n && i - 2 * len + 2 >= 0; len ++{
				s := sl[i + 1][j + 1] - sl[i - len + 2][j - len + 2]
				s += sr[i - len + 2][j - len + 1] - sr[i - 2 * len + 3][j]
				s += sl[i - len + 1][j + len - 1] - sl[i - 2 * len + 2][j] 
				s += sr[i][j + 1] - sr[i - len + 1][j + len]
				if _, ok := record[s]; !ok{
					res = append(res, s)
					record[s] = struct{}{}
				}
			} 
		}
	}
	sort.Slice(res, func(i, j int) bool {return res[i] > res[j]})

	//  答案计算
	res = res[:min(len(res), 3)] 
	if len(res) == 3 && res[2] == res[1]{
		res = res[:len(res) - 1]
	}
	if len(res) >= 2 && res[1] == res[0]{
		res = res[1:]
	}
	return res 
}
func min(a, b int) int {if a < b {return a}; return b}

// @lc code=end



/*
// @lcpr case=start
// [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,2,3],[4,5,6],[7,8,9]]\n
// @lcpr case=end

// @lcpr case=start
// [[7,7,7]]\n
// @lcpr case=end

// @lcpr case=start
// [[7,7,7,7,7,4]]\n
// @lcpr case=end
 */

