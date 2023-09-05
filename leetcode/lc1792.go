/*
 * @lc app=leetcode.cn id=1792 lang=golang
 * @lcpr version=21913
 *
 * [1792] 最大平均通过率
 *
 * https://leetcode.cn/problems/maximum-average-pass-ratio/description/
 *
 * algorithms
 * Medium (58.83%)
 * Likes:    156
 * Dislikes: 0
 * Total Accepted:    24.5K
 * Total Submissions: 41.7K
 * Testcase Example:  '[[1,2],[3,5],[2,2]]\n2'
 *
 * 一所学校里有一些班级，每个班级里有一些学生，现在每个班都会进行一场期末考试。给你一个二维数组 classes ，其中 classes[i] =
 * [passi, totali] ，表示你提前知道了第 i 个班级总共有 totali 个学生，其中只有 passi 个学生可以通过考试。
 *
 * 给你一个整数 extraStudents ，表示额外有 extraStudents 个聪明的学生，他们 一定 能通过任何班级的期末考。你需要给这
 * extraStudents 个学生每人都安排一个班级，使得 所有 班级的 平均 通过率 最大 。
 *
 * 一个班级的 通过率 等于这个班级通过考试的学生人数除以这个班级的总人数。平均通过率 是所有班级的通过率之和除以班级数目。
 *
 * 请你返回在安排这 extraStudents 个学生去对应班级后的 最大 平均通过率。与标准答案误差范围在 10^-5
 * 以内的结果都会视为正确结果。
 *
 *
 *
 * 示例 1：
 *
 * 输入：classes = [[1,2],[3,5],[2,2]], extraStudents = 2
 * 输出：0.78333
 * 解释：你可以将额外的两个学生都安排到第一个班级，平均通过率为 (3/4 + 3/5 + 2/2) / 3 = 0.78333 。
 *
 *
 * 示例 2：
 *
 * 输入：classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
 * 输出：0.53485
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= classes.length <= 10^5
 * classes[i].length == 2
 * 1 <= passi <= totali <= 10^5
 * 1 <= extraStudents <= 10^5
 *
 *
 */
package leetcode

import "container/heap"
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

type pair struct{ x, y int }
type hpp []pair

func (h hpp) Len() int           { return len(h) }
func (h hpp) Less(i, j int) bool { 
	a1, b1, a2, b2 := h[i].x, h[i].y, h[j].x, h[j].y 
	return b2 * (b2 + 1) * (b1 - a1) > b1 * (b1 + 1) * (b2 - a2)
}
func (h hpp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h hpp) top() pair          { return h[0] }
func (h *hpp) Pop() any          { a := *h; v := a[len(a)-1]; a = a[:len(a)-1]; *h = a; return v }
func (h *hpp) Push(v any)        { *h = append(*h, v.(pair)) }
func (h *hpp) push(v pair)       { heap.Push(h, v) }
func (h *hpp) pop() pair          { return heap.Pop(h).(pair) }



func maxAverageRatio(classes [][]int, extraStudents int) float64 {
	hp := hpp{}
	for _, x := range classes{
		hp.push(pair{x[0], x[1]})
	}
	for i := 0 ; i < extraStudents ; i ++ {
		// 这样写可以减少一次pop操作， 所以跑的快一点
		hp[0].x ++ 
		hp[0].y ++ 
		heap.Fix(&hp, 0)
	}
	var res float64 
	for _, p := range hp{
		res += float64(p.x) / float64(p.y)
	}
	return res / float64(len(classes))
}



// @lc code=end



/*
// @lcpr case=start
// [[1,2],[3,5],[2,2]]\n2\n
// @lcpr case=end

// @lcpr case=start
// [[2,4],[3,9],[4,5],[2,10]]\n4\n
// @lcpr case=end

 */

