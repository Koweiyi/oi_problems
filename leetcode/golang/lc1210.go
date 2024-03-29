/*
 * @lc app=leetcode.cn id=1210 lang=golang
 * @lcpr version=30105
 *
 * [1210] 穿过迷宫的最少移动次数
 *
 * https://leetcode.cn/problems/minimum-moves-to-reach-target-with-rotations/description/
 *
 * algorithms
 * Hard (64.23%)
 * Likes:    136
 * Dislikes: 0
 * Total Accepted:    15.3K
 * Total Submissions: 23.7K
 * Testcase Example:  '[[0,0,0,0,0,1],[1,1,0,0,1,0],[0,0,0,0,1,1],[0,0,1,0,1,0],[0,1,1,0,0,0],[0,1,1,0,0,0]]\r'
 *
 * 你还记得那条风靡全球的贪吃蛇吗？
 *
 * 我们在一个 n*n 的网格上构建了新的迷宫地图，蛇的长度为 2，也就是说它会占去两个单元格。蛇会从左上角（(0, 0) 和 (0,
 * 1)）开始移动。我们用 0 表示空单元格，用 1 表示障碍物。蛇需要移动到迷宫的右下角（(n-1, n-2) 和 (n-1, n-1)）。
 *
 * 每次移动，蛇可以这样走：
 *
 *
 * 如果没有障碍，则向右移动一个单元格。并仍然保持身体的水平／竖直状态。
 * 如果没有障碍，则向下移动一个单元格。并仍然保持身体的水平／竖直状态。
 * 如果它处于水平状态并且其下面的两个单元都是空的，就顺时针旋转 90 度。蛇从（(r, c)、(r, c+1)）移动到 （(r, c)、(r+1,
 * c)）。
 *
 * 如果它处于竖直状态并且其右面的两个单元都是空的，就逆时针旋转 90 度。蛇从（(r, c)、(r+1, c)）移动到（(r, c)、(r,
 * c+1)）。
 *
 *
 *
 * 返回蛇抵达目的地所需的最少移动次数。
 *
 * 如果无法到达目的地，请返回 -1。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：grid = [[0,0,0,0,0,1],
 * ⁠              [1,1,0,0,1,0],
 * [0,0,0,0,1,1],
 * [0,0,1,0,1,0],
 * [0,1,1,0,0,0],
 * [0,1,1,0,0,0]]
 * 输出：11
 * 解释：
 * 一种可能的解决方案是 [右, 右, 顺时针旋转, 右, 下, 下, 下, 下, 逆时针旋转, 右, 下]。
 *
 *
 * 示例 2：
 *
 * 输入：grid = [[0,0,1,1,1,1],
 * [0,0,0,0,1,1],
 * [1,1,0,0,0,1],
 * [1,1,1,0,0,1],
 * [1,1,1,0,0,1],
 * [1,1,1,0,0,0]]
 * 输出：9
 *
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= n <= 100
 * 0 <= grid[i][j] <= 1
 * 蛇保证从空单元格开始出发。
 *
 *
 */

// @lcpr-template-start
package leetcode

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
type ListNode struct {
	Val  int
	Next *ListNode
}

// @lcpr-template-end
// @lc code=start
func minimumMoves(g [][]int) int {
	type sta struct{
		x, y, s int 
	}

	dirs := []sta{{1,0,0},{0,1,0}, {0,0,1}}

	n := len(g)
	vis := make([][][2]bool, n)
	for i := range vis{
		vis[i] = make([][2]bool, n)
	}

	vis[0][0][0] = true 
	q := []sta{{0,0,0}}
	for step := 1; len(q) > 0 ; step ++{
		tmp := q 
		q = nil 
		for _, t := range tmp{
			for _, d := range dirs{
				x, y, s := t.x + d.x, t.y + d.y, t.s ^ d.s 
				x2, y2 := x + s, y + (s ^ 1)

				if x2 < n && y2 < n && !vis[x][y][s] && g[x][y] == 0 && g[x2][y2] == 0 &&(d.s == 0 || g[x+1][y+1] == 0){
					if x == n -1 && y == n - 2{
						return step 
					} 
					vis[x][y][s] = true 
					q = append(q, sta{x,y,s})
				}
			}
		}
	}
	return -1
}

// @lc code=end

/*
// @lcpr case=start
// [[0,0,0,0,0,1],[1,1,0,0,1,0],[0,0,0,0,1,1],[0,0,1,0,1,0],[0,1,1,0,0,0],[0,1,1,0,0,0]]\n
// @lcpr case=end

// @lcpr case=start
// [[0,0,1,1,1,1],[0,0,0,0,1,1],[1,1,0,0,0,1],[1,1,1,0,0,1],[1,1,1,0,0,1],[1,1,1,0,0,0]]\n
// @lcpr case=end

*/
