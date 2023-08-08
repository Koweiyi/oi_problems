/*
 * @lc app=leetcode.cn id=1861 lang=golang
 * @lcpr version=21912
 *
 * [1861] 旋转盒子
 *
 * https://leetcode.cn/problems/rotating-the-box/description/
 *
 * algorithms
 * Medium (63.44%)
 * Likes:    23
 * Dislikes: 0
 * Total Accepted:    5.9K
 * Total Submissions: 9.3K
 * Testcase Example:  '[["#",".","#"]]'
 *
 * 给你一个 m x n 的字符矩阵 box ，它表示一个箱子的侧视图。箱子的每一个格子可能为：
 *
 *
 * '#' 表示石头
 * '*' 表示固定的障碍物
 * '.' 表示空位置
 *
 *
 * 这个箱子被 顺时针旋转 90 度 ，由于重力原因，部分石头的位置会发生改变。每个石头会垂直掉落，直到它遇到障碍物，另一个石头或者箱子的底部。重力 不会
 * 影响障碍物的位置，同时箱子旋转不会产生惯性 ，也就是说石头的水平位置不会发生改变。
 *
 * 题目保证初始时 box 中的石头要么在一个障碍物上，要么在另一个石头上，要么在箱子的底部。
 *
 * 请你返回一个 n x m的矩阵，表示按照上述旋转后，箱子内的结果。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：box = [["#",".","#"]]
 * 输出：[["."],
 * ["#"],
 * ["#"]]
 *
 *
 * 示例 2：
 *
 *
 *
 * 输入：box = [["#",".","*","."],
 * ["#","#","*","."]]
 * 输出：[["#","."],
 * ["#","#"],
 * ["*","*"],
 * [".","."]]
 *
 *
 * 示例 3：
 *
 *
 *
 * 输入：box = [["#","#","*",".","*","."],
 * ["#","#","#","*",".","."],
 * ["#","#","#",".","#","."]]
 * 输出：[[".","#","#"],
 * [".","#","#"],
 * ["#","#","*"],
 * ["#","*","."],
 * ["#",".","*"],
 * ["#",".","."]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == box.length
 * n == box[i].length
 * 1 <= m, n <= 500
 * box[i][j] 只可能是 '#' ，'*' 或者 '.' 。
 *
 *
 */
package leetcode

type TreeNode struct {
	Val   int
	Right *TreeNode
	Left  *TreeNode
}

// @lc code=start
func rotateTheBox(box [][]byte) [][]byte {
	return nil
}

// @lc code=end

/*
// @lcpr case=start
// [["#",".","#"]]\n
// @lcpr case=end

// @lcpr case=start
// [["#",".","*","."],["#","#","*","."]]\n
// @lcpr case=end

// @lcpr case=start
// [["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]]\n
// @lcpr case=end

*/
