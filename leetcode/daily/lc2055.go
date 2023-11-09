/*
 * @lc app=leetcode.cn id=2055 lang=golang
 * @lcpr version=21913
 *
 * [2055] 蜡烛之间的盘子
 *
 * https://leetcode.cn/problems/plates-between-candles/description/
 *
 * algorithms
 * Medium (43.42%)
 * Likes:    163
 * Dislikes: 0
 * Total Accepted:    34.5K
 * Total Submissions: 79.4K
 * Testcase Example:  '"**|**|***|"\n[[2,5],[5,9]]'
 *
 * 给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 0 开始的字符串 s ，它只包含字符 '*' 和 '|' ，其中 '*' 表示一个 盘子
 * ，'|' 表示一支 蜡烛 。
 *
 * 同时给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [lefti, righti] 表示 子字符串
 * s[lefti...righti] （包含左右端点的字符）。对于每个查询，你需要找到 子字符串中 在 两支蜡烛之间 的盘子的 数目 。如果一个盘子在
 * 子字符串中 左边和右边 都 至少有一支蜡烛，那么这个盘子满足在 两支蜡烛之间 。
 *
 *
 * 比方说，s = "||**||**|*" ，查询 [3, 8] ，表示的是子字符串 "*||**|" 。子字符串中在两支蜡烛之间的盘子数目为 2
 * ，子字符串中右边两个盘子在它们左边和右边 都 至少有一支蜡烛。
 *
 *
 * 请你返回一个整数数组 answer ，其中 answer[i] 是第 i 个查询的答案。
 *
 *
 *
 * 示例 1:
 *
 *
 *
 * 输入：s = "**|**|***|", queries = [[2,5],[5,9]]
 * 输出：[2,3]
 * 解释：
 * - queries[0] 有两个盘子在蜡烛之间。
 * - queries[1] 有三个盘子在蜡烛之间。
 *
 *
 * 示例 2:
 *
 *
 *
 * 输入：s = "***|**|*****|**||**|*", queries =
 * [[1,17],[4,5],[14,17],[5,11],[15,16]]
 * 输出：[9,0,0,0,0]
 * 解释：
 * - queries[0] 有 9 个盘子在蜡烛之间。
 * - 另一个查询没有盘子在蜡烛之间。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 3 <= s.length <= 10^5
 * s 只包含字符 '*' 和 '|' 。
 * 1 <= queries.length <= 10^5
 * queries[i].length == 2
 * 0 <= lefti <= righti < s.length
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
func platesBetweenCandles(s string, queries [][]int) []int {	
	// 类似单调栈
	n := len(s)
	left := []int{}
	rigth := make([]int, n)
	pre_fix := make([]int, n + 1)
	for i := range s{
		var cnt int
		if s[i] == '|'{
			left = append(left, i)
		}else{
			if i == 0{
				left = append(left, -1)
			}else{
				left = append(left, left[len(left) - 1]) 
			}
			cnt ++ 
		}
		pre_fix[i + 1] = pre_fix[i] + cnt 
	}

	for j := n - 1; j >= 0 ; j -- {
		if s[j] == '|'{
			rigth[j] = j
		}else {
			if j == n - 1{
				rigth[j] = n 
			}else{
				rigth[j] = rigth[j + 1]
			}
		}
	}

	res := make([]int, len(queries))
	for i, q := range queries{
		l, r := rigth[q[0]], left[q[1]]
		if l + 1 >= r{
			res[i] = 0 
		}else{
			res[i] = pre_fix[r + 1] - pre_fix[l] 
		}
	}
	return res 
}
// @lc code=end



/*
// @lcpr case=start
// "**|**|***|"\n[[2,5],[5,9]]\n
// @lcpr case=end

// @lcpr case=start
// "***|**|*****|**||**|*"\n[[1,17],[4,5],[14,17],[5,11],[15,16]]\n
// @lcpr case=end

 */

