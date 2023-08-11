/*
 * @lc app=leetcode.cn id=2672 lang=golang
 * @lcpr version=21913
 *
 * [2672] 有相同颜色的相邻元素数目
 *
 * https://leetcode.cn/problems/number-of-adjacent-elements-with-the-same-color/description/
 *
 * algorithms
 * Medium (58.23%)
 * Likes:    8
 * Dislikes: 0
 * Total Accepted:    4.8K
 * Total Submissions: 8.3K
 * Testcase Example:  '4\n[[0,2],[1,2],[3,1],[1,1],[2,1]]'
 *
 * 给你一个下标从 0 开始、长度为 n 的数组 nums 。一开始，所有元素都是 未染色 （值为 0 ）的。
 * 
 * 给你一个二维整数数组 queries ，其中 queries[i] = [indexi, colori] 。
 * 
 * 对于每个操作，你需要将数组 nums 中下标为 indexi 的格子染色为 colori 。
 * 
 * 请你返回一个长度与 queries 相等的数组 answer ，其中 answer[i]是前 i 个操作 之后 ，相邻元素颜色相同的数目。
 * 
 * 更正式的，answer[i] 是执行完前 i 个操作后，0 <= j < n - 1 的下标 j 中，满足 nums[j] == nums[j + 1]
 * 且 nums[j] != 0 的数目。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]
 * 输出：[0,1,1,0,2]
 * 解释：一开始数组 nums = [0,0,0,0] ，0 表示数组中还没染色的元素。
 * - 第 1 个操作后，nums = [2,0,0,0] 。相邻元素颜色相同的数目为 0 。
 * - 第 2 个操作后，nums = [2,2,0,0] 。相邻元素颜色相同的数目为 1 。
 * - 第 3 个操作后，nums = [2,2,0,1] 。相邻元素颜色相同的数目为 1 。
 * - 第 4 个操作后，nums = [2,1,0,1] 。相邻元素颜色相同的数目为 0 。
 * - 第 5 个操作后，nums = [2,1,1,1] 。相邻元素颜色相同的数目为 2 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：n = 1, queries = [[0,100000]]
 * 输出：[0]
 * 解释：一开始数组 nums = [0] ，0 表示数组中还没染色的元素。
 * - 第 1 个操作后，nums = [100000] 。相邻元素颜色相同的数目为 0 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n <= 10^5
 * 1 <= queries.length <= 10^5
 * queries[i].length == 2
 * 0 <= indexi <= n - 1
 * 1 <=  colori <= 10^5
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
func colorTheArray(n int, queries [][]int) []int {
	res := 0
	ans := make([]int, 0)
	a := make([]int, n)
	for _, q := range queries{
		idx, c := q[0], q[1]
		if a[idx] == 0{
			if idx - 1 >= 0 && a[idx - 1] == c {res ++}
			if idx + 1 < n && a[idx + 1] == c {res ++}
		}else{
			if idx - 1 >= 0 && a[idx - 1] == a[idx] {res --} 
			if idx + 1 < n && a[idx + 1] == a[idx] {res --} 
			if idx - 1 >= 0 && a[idx - 1] == c {res ++} 
			if idx + 1 < n && a[idx + 1] == c {res ++} 
		}
		a[idx] = c
		ans = append(ans, res)
	}
	return ans
}
// @lc code=end



/*
// @lcpr case=start
// 4\n[[0,2],[1,2],[3,1],[1,1],[2,1]]\n
// @lcpr case=end

// @lcpr case=start
// 1\n[[0,100000]]\n
// @lcpr case=end

 */

