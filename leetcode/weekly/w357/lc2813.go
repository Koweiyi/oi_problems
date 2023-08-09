/*
 * @lc app=leetcode.cn id=2813 lang=golang
 * @lcpr version=21913
 *
 * [2813] 子序列最大优雅度
 *
 * https://leetcode.cn/problems/maximum-elegance-of-a-k-length-subsequence/description/
 *
 * algorithms
 * Hard (38.74%)
 * Likes:    11
 * Dislikes: 0
 * Total Accepted:    1.3K
 * Total Submissions: 3.3K
 * Testcase Example:  '[[3,2],[5,1],[10,1]]\n2'
 *
 * 给你一个长度为 n 的二维整数数组 items 和一个整数 k 。
 *
 * items[i] = [profiti, categoryi]，其中 profiti 和 categoryi 分别表示第 i 个项目的利润和类别。
 *
 * 现定义 items 的 子序列 的 优雅度 可以用 total_profit + distinct_categories^2 计算，其中
 * total_profit 是子序列中所有项目的利润总和，distinct_categories 是所选子序列所含的所有类别中不同类别的数量。
 *
 * 你的任务是从 items 所有长度为 k 的子序列中，找出 最大优雅度 。
 *
 * 用整数形式表示并返回 items 中所有长度恰好为 k 的子序列的最大优雅度。
 *
 * 注意：数组的子序列是经由原数组删除一些元素（可能不删除）而产生的新数组，且删除不改变其余元素相对顺序。
 *
 *
 *
 * 示例 1：
 *
 * 输入：items = [[3,2],[5,1],[10,1]], k = 2
 * 输出：17
 * 解释：
 * 在这个例子中，我们需要选出长度为 2 的子序列。
 * 其中一种方案是 items[0] = [3,2] 和 items[2] = [10,1] 。
 * 子序列的总利润为 3 + 10 = 13 ，子序列包含 2 种不同类别 [2,1] 。
 * 因此，优雅度为 13 + 2^2 = 17 ，可以证明 17 是可以获得的最大优雅度。
 *
 *
 * 示例 2：
 *
 * 输入：items = [[3,1],[3,1],[2,2],[5,3]], k = 3
 * 输出：19
 * 解释：
 * 在这个例子中，我们需要选出长度为 3 的子序列。
 * 其中一种方案是 items[0] = [3,1] ，items[2] = [2,2] 和 items[3] = [5,3] 。
 * 子序列的总利润为 3 + 2 + 5 = 10 ，子序列包含 3 种不同类别 [1, 2, 3] 。
 * 因此，优雅度为 10 + 3^2 = 19 ，可以证明 19 是可以获得的最大优雅度。
 *
 * 示例 3：
 *
 * 输入：items = [[1,1],[2,1],[3,1]], k = 3
 * 输出：7
 * 解释：
 * 在这个例子中，我们需要选出长度为 3 的子序列。
 * 我们需要选中所有项目。
 * 子序列的总利润为 1 + 2 + 3 = 6，子序列包含 1 种不同类别 [1] 。
 * 因此，最大优雅度为 6 + 1^2 = 7 。
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= items.length == n <= 10^5
 * items[i].length == 2
 * items[i][0] == profiti
 * items[i][1] == categoryi
 * 1 <= profiti <= 10^9
 * 1 <= categoryi <= n
 * 1 <= k <= n
 *
 *
 */
package leetcode

import "sort"
type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}
// @lc code=start
func findMaximumElegance(items [][]int, k int) int64 {
	sort.Slice(items, func(i, j int) bool {return items[i][0] > items[j][0]})
	vis := map[int]bool{}
	total_profit, res := 0, 0  
	dup := []int{}
	for i, t := range items{
		if i < k {
			total_profit += t[0]
			if !vis[t[1]]{
				vis[t[1]] = true
			} else{
				dup = append(dup, t[0])
			}
		}else if len(dup) > 0 && !vis[t[1]]{
			vis[t[1]] = true
			total_profit += t[0] - dup[len(dup) - 1]
			dup = dup[:len(dup) - 1]
		}
		res = max(res, total_profit + len(vis) * len(vis))
	}
	return int64(res)
}
func max(a, b int) int {if a > b {return a}; return b}
// @lc code=end


/*
// @lcpr case=start
// [[3,2],[5,1],[10,1]]\n2\n
// @lcpr case=end

// @lcpr case=start
// [[3,1],[3,1],[2,2],[5,3]]\n3\n
// @lcpr case=end

// @lcpr case=start
// [[1,1],[2,1],[3,1]]\n3\n
// @lcpr case=end

 */
