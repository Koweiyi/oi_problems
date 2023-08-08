/*
 * @lc app=leetcode.cn id=1947 lang=golang
 * @lcpr version=21912
 *
 * [1947] 最大兼容性评分和
 *
 * https://leetcode.cn/problems/maximum-compatibility-score-sum/description/
 *
 * algorithms
 * Medium (58.12%)
 * Likes:    33
 * Dislikes: 0
 * Total Accepted:    6.8K
 * Total Submissions: 11.7K
 * Testcase Example:  '[[1,1,0],[1,0,1],[0,0,1]]\n[[1,0,0],[0,0,1],[1,1,0]]'
 *
 * 有一份由 n 个问题组成的调查问卷，每个问题的答案要么是 0（no，否），要么是 1（yes，是）。
 *
 * 这份调查问卷被分发给 m 名学生和 m 名导师，学生和导师的编号都是从 0 到 m - 1 。学生的答案用一个二维整数数组 students 表示，其中
 * students[i] 是一个整数数组，包含第 i 名学生对调查问卷给出的答案（下标从 0 开始）。导师的答案用一个二维整数数组 mentors
 * 表示，其中 mentors[j] 是一个整数数组，包含第 j 名导师对调查问卷给出的答案（下标从 0 开始）。
 *
 * 每个学生都会被分配给 一名 导师，而每位导师也会分配到 一名 学生。配对的学生与导师之间的兼容性评分等于学生和导师答案相同的次数。
 *
 *
 * 例如，学生答案为[1, 0, 1] 而导师答案为 [0, 0, 1] ，那么他们的兼容性评分为 2 ，因为只有第二个和第三个答案相同。
 *
 *
 * 请你找出最优的学生与导师的配对方案，以 最大程度上 提高 兼容性评分和 。
 *
 * 给你 students 和 mentors ，返回可以得到的 最大兼容性评分和 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]
 * 输出：8
 * 解释：按下述方式分配学生和导师：
 * - 学生 0 分配给导师 2 ，兼容性评分为 3 。
 * - 学生 1 分配给导师 0 ，兼容性评分为 2 。
 * - 学生 2 分配给导师 1 ，兼容性评分为 3 。
 * 最大兼容性评分和为 3 + 2 + 3 = 8 。
 *

 56 * 30 * 24
 56 * 720
 60 * 700 
 42000
 * 示例 2：
 *
 * 输入：students = [[0,0],[0,0],[0,0]], mentors = [[1,1],[1,1],[1,1]]
 * 输出：0
 * 解释：任意学生与导师配对的兼容性评分都是 0 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == students.length == mentors.length
 * n == students[i].length == mentors[j].length
 * 1 <= m, n <= 8
 * students[i][k] 为 0 或 1
 * mentors[j][k] 为 0 或 1
 *
 *
 */
package leetcode

import (
	
)
type TreeNode struct {
    Val int
    Right *TreeNode
    Left *TreeNode
}

// 0 - 0
// 0 - 1 2 4
// 0 - 3 5 6
// 0 - 7

// 1 - 1
// @lc code=start
func maxCompatibilitySum(students [][]int, mentors [][]int) int {
	res := 0
	m := len(students)
	arr := make([]int, m)
	for i := 0; i < m; i++ {
		arr[i] = i
	}
	for {
		s := 0
		for i := 0; i < m; i++ {
			for j := 0; j < len(students[i]); j++ {
				if students[i][j] == mentors[arr[i]][j] {
					s++
				}
			}
		}
		if s > res {
			res = s
		}
		if !nextPermutation(arr) {
			break
		}
	}
	return res
}

func nextPermutation(arr []int) bool {
	n := len(arr)
	i := n - 1
	for i > 0 && arr[i-1] >= arr[i] {
		i--
	}
	if i <= 0 {
		return false
	}
	j := n - 1
	for arr[j] <= arr[i-1] {
		j--
	}
	arr[i-1], arr[j] = arr[j], arr[i-1]
	j = n - 1
	for i < j {
		arr[i], arr[j] = arr[j], arr[i]
		i++
		j--
	}
	return true
}
// @lc code=end



/*
// @lcpr case=start
// [[1,1,0],[1,0,1],[0,0,1]]\n[[1,0,0],[0,0,1],[1,1,0]]\n
// @lcpr case=end

// @lcpr case=start
// [[0,0],[0,0],[0,0]]\n[[1,1],[1,1],[1,1]]\n
// @lcpr case=end

 */

