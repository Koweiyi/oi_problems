/*
 * @lc app=leetcode.cn id=939 lang=golang
 * @lcpr version=21913
 *
 * [939] 最小面积矩形
 *
 * https://leetcode.cn/problems/minimum-area-rectangle/description/
 *
 * algorithms
 * Medium (48.53%)
 * Likes:    146
 * Dislikes: 0
 * Total Accepted:    9.1K
 * Total Submissions: 18.7K
 * Testcase Example:  '[[1,1],[1,3],[3,1],[3,3],[2,2]]'
 *
 * 给定在 xy 平面上的一组点，确定由这些点组成的矩形的最小面积，其中矩形的边平行于 x 轴和 y 轴。
 *
 * 如果没有任何矩形，就返回 0。
 *
 *
 *
 * 示例 1：
 *
 * 输入：[[1,1],[1,3],[3,1],[3,3],[2,2]]
 * 输出：4
 *
 *
 * 示例 2：
 *
 * 输入：[[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
 * 输出：2
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= points.length <= 500
 * 0 <= points[i][0] <= 40000
 * 0 <= points[i][1] <= 40000
 * 所有的点都是不同的。
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
type ListNode struct {
    Val int
    Next *ListNode
}
// @lc code=start
func minAreaRect(points [][]int) int {
	type pair struct{x, y int} 
	mp := map[pair]struct{}{}

	for i := 0 ; i < len(points) ; i ++{
		mp[pair{points[i][0], points[i][1]}] = struct{}{}
	}


	// 枚举左上右下两个顶点
	// 根据左上右下判断左下右上是否在mp中，
	res := math.MaxInt
	n := len(points)
	for i := 0 ; i < n ; i ++ {
		for j := i + 1 ; j < n ; j ++ {

			// 枚举两个点不能在同一行或者同一列
			x1, y1, x2, y2 := points[i][0], points[i][1], points[j][0], points[j][1]
			if x1 == x2 || y1 == y2{continue}
			_, ok1 := mp[pair{x1, y2}]
			_, ok2 := mp[pair{x2, y1}]
			if ok1 && ok2{
				// 可以构成矩形
				res = min(res, abs(x2 - x1) * abs(y2 - y1))
			}
		}
	}
	if res == math.MaxInt{
		return 0
	}
	return res 
}
func min(a, b int) int {if a < b {return a}; return b}
func abs(a int) int {if a < 0 {return -a}; return a}

// @lc code=end



/*
// @lcpr case=start
// [[1,1],[1,3],[3,1],[3,3],[2,2]]\n
// @lcpr case=end

// @lcpr case=start
// [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]\n
// @lcpr case=end

 */

