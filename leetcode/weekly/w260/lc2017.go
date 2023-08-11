/*
 * @lc app=leetcode.cn id=2017 lang=golang
 * @lcpr version=21913
 *
 * [2017] 网格游戏
 *
 * https://leetcode.cn/problems/grid-game/description/
 *
 * algorithms
 * Medium (38.72%)
 * Likes:    35
 * Dislikes: 0
 * Total Accepted:    5.8K
 * Total Submissions: 15.1K
 * Testcase Example:  '[[2,5,4],[1,5,1]]'
 *
 * 给你一个下标从 0 开始的二维数组 grid ，数组大小为 2 x n ，其中 grid[r][c] 表示矩阵中 (r, c)
 * 位置上的点数。现在有两个机器人正在矩阵上参与一场游戏。
 *
 * 两个机器人初始位置都是 (0, 0) ，目标位置是 (1, n-1) 。每个机器人只会 向右 ((r, c) 到 (r, c + 1)) 或 向下
 * ((r, c) 到 (r + 1, c)) 。
 *
 * 游戏开始，第一个 机器人从 (0, 0) 移动到 (1, n-1) ，并收集路径上单元格的全部点数。对于路径上所有单元格 (r, c) ，途经后
 * grid[r][c] 会重置为 0 。然后，第二个 机器人从 (0, 0) 移动到 (1, n-1)
 * ，同样收集路径上单元的全部点数。注意，它们的路径可能会存在相交的部分。
 *
 * 第一个 机器人想要打击竞争对手，使 第二个 机器人收集到的点数 最小化 。与此相对，第二个 机器人想要 最大化
 * 自己收集到的点数。两个机器人都发挥出自己的 最佳水平 的前提下，返回 第二个 机器人收集到的 点数 。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：grid = [[2,5,4],[1,5,1]]
 * 输出：4
 * 解释：第一个机器人的最佳路径如红色所示，第二个机器人的最佳路径如蓝色所示。
 * 第一个机器人访问过的单元格将会重置为 0 。
 * 第二个机器人将会收集到 0 + 0 + 4 + 0 = 4 个点。
 *
 *
 * 示例 2：
 *
 * 输入：grid = [[3,3,1],[8,5,2]]
 * 输出：4
 * 解释：第一个机器人的最佳路径如红色所示，第二个机器人的最佳路径如蓝色所示。
 * 第一个机器人访问过的单元格将会重置为 0 。
 * 第二个机器人将会收集到 0 + 3 + 1 + 0 = 4 个点。
 *
 *
 * 示例 3：
 *
 * 输入：grid = [[1,3,1,15],[1,3,3,1]]
 * 输出：7
 * 解释：第一个机器人的最佳路径如红色所示，第二个机器人的最佳路径如蓝色所示。
 * 第一个机器人访问过的单元格将会重置为 0 。
 * 第二个机器人将会收集到 0 + 1 + 3 + 3 + 0 = 7 个点。
 *
 *
 *
 *
 * 提示：
 *
 *
 * grid.length == 2
 * n == grid[r].length
 * 1 <= n <= 5 * 10^4
 * 1 <= grid[r][c] <= 10^5
 *
 *
 */
package leetcode

import "math"
type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}
// @lc code=start
func gridGame(grid [][]int) (res int64) {
	n := len(grid[0])
	s := make([][]int64, 2)
	s[0] = make([]int64, n + 1)
	s[1] = make([]int64, n + 1)
	for i :=  0 ; i < n ; i ++ {
		s[0][i + 1] = int64(grid[0][i]) + s[0][i]
		s[1][i + 1] = int64(grid[1][i]) + s[1][i]
	}
	res = math.MaxInt64
	for i := 0 ; i < n ; i ++ {
		res = min(res, max(s[1][i],s[0][n] - s[0][i + 1]))
	}
	return res 
} 
func min(a, b int64) int64 {if a < b {return a}; return b}
func max(a, b int64) int64 {if a > b {return a}; return b}

// @lc code=end



/*
// @lcpr case=start
// [[2,5,4],[1,5,1]]\n
// @lcpr case=end

// @lcpr case=start
// [[3,3,1],[8,5,2]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,3,1,15],[1,3,3,1]]\n
// @lcpr case=end

 */

