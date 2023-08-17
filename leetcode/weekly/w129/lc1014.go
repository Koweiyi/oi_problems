/*
 * @lc app=leetcode.cn id=1014 lang=golang
 * @lcpr version=21913
 *
 * [1014] 最佳观光组合
 *
 * https://leetcode.cn/problems/best-sightseeing-pair/description/
 *
 * algorithms
 * Medium (57.14%)
 * Likes:    377
 * Dislikes: 0
 * Total Accepted:    62.2K
 * Total Submissions: 108.8K
 * Testcase Example:  '[8,1,5,2,6]'
 *
 * 给你一个正整数数组 values，其中 values[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的 距离 为 j - i。
 *
 * 一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，也就是景点的评分之和 减去
 * 它们两者之间的距离。
 *
 * 返回一对观光景点能取得的最高分。
 *
 *
 *
 * 示例 1：
 *
 * 输入：values = [8,1,5,2,6]
 * 输出：11
 * 解释：i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
 *
 *
 * 示例 2：
 *
 * 输入：values = [1,2]
 * 输出：2
 *
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= values.length <= 5 * 10^4
 * 1 <= values[i] <= 1000
 *
 *
 */
package leetcode

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
func maxScoreSightseeingPair(values []int) int {
	// 按照value从大到小进行排序
	// 选取最大两个value 后续选中其他景点判断距离是否能缩短，如果不能缩短距离则一定不可能获得更高分数

	// 动态规划 
	res := 0
	maxp := values[0]  // 表示values[i] + i
	for i := 1 ; i < len(values) ; i ++ {
		res = max(res, maxp + values[i] - i)
		maxp = max(maxp, values[i] + i)
	}
	return res 
}
func max(a, b int) int {if a > b {return a}; return b}

func abs(a int) int {if a < 0 {return -a}; return a}

// @lc code=end



/*
// @lcpr case=start
// [8,1,5,2,6]\n
// @lcpr case=end

// @lcpr case=start
// [1,2]\n
// @lcpr case=end

 */

