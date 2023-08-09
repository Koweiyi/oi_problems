/*
 * @lc app=leetcode.cn id=1401 lang=golang
 * @lcpr version=21913
 *
 * [1401] 圆和矩形是否有重叠
 *
 * https://leetcode.cn/problems/circle-and-rectangle-overlapping/description/
 *
 * algorithms
 * Medium (51.76%)
 * Likes:    99
 * Dislikes: 0
 * Total Accepted:    18K
 * Total Submissions: 34.8K
 * Testcase Example:  '1\n0\n0\n1\n-1\n3\n1'
 *
 * 给你一个以 (radius, xCenter, yCenter) 表示的圆和一个与坐标轴平行的矩形 (x1, y1, x2, y2) ，其中 (x1,
 * y1) 是矩形左下角的坐标，而 (x2, y2) 是右上角的坐标。
 * 
 * 如果圆和矩形有重叠的部分，请你返回 true ，否则返回 false 。
 * 
 * 换句话说，请你检测是否 存在 点 (xi, yi) ，它既在圆上也在矩形上（两者都包括点落在边界上的情况）。
 * 
 * 
 * 
 * 示例 1 ：
 * 
 * 输入：radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
 * 输出：true
 * 解释：圆和矩形存在公共点 (1,0) 。
 * 
 * 
 * 示例 2 ：
 * 
 * 输入：radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
 * 输出：false
 * 
 * 
 * 示例 3 ：
 * 
 * 输入：radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
 * 输出：true
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= radius <= 2000
 * -10^4 <= xCenter, yCenter <= 10^4
 * -10^4 <= x1 < x2 <= 10^4
 * -10^4 <= y1 < y2 <= 10^4
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

func judge1(r, xc, yc, x, y int) bool {
	return (x - xc) * (x - xc) + (y - yc) * (y - yc) <= r * r
}

func judge2(r, xc, yc, x, y1, y2 int) bool{
	return yc >= min(y1, y2) && yc <= max(y1, y2) && abs(x - xc) <= r 
}

func min(a, b int) int {if a < b {return a}; return b}
func max(a, b int) int {if a > b {return a}; return b}
func abs(a int) int {if a < 0 {return -a}; return a}

func checkOverlap(r int, xCenter int, yCenter int, x1 int, y1 int, x2 int, y2 int) bool {
	dis := 0
	if xCenter < x1 || xCenter > x2{
		dis += min((xCenter - x1) * (xCenter - x1), (xCenter - x2) * (xCenter - x2))
	}
	if yCenter < y1 || yCenter > y2{
		dis += min((yCenter - y1) * (yCenter - y1), (yCenter - y2) * (yCenter - y2))
	}
	return dis <= r * r
}
// @lc code=end



/*
// @lcpr case=start
// 1\n1\n1\n-3\n-3\n3\n3\n
// @lcpr case=end

// @lcpr case=start
// 1\n1\n1\n1\n-3\n2\n-1\n
// @lcpr case=end

// @lcpr case=start
// 1\n0\n0\n-1\n0\n0\n1\n
// @lcpr case=end

 */

