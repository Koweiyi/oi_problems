/*
 * @lc app=leetcode.cn id=2462 lang=golang
 * @lcpr version=21913
 *
 * [2462] 雇佣 K 位工人的总代价
 *
 * https://leetcode.cn/problems/total-cost-to-hire-k-workers/description/
 *
 * algorithms
 * Medium (38.16%)
 * Likes:    41
 * Dislikes: 0
 * Total Accepted:    8K
 * Total Submissions: 20.8K
 * Testcase Example:  '[17,12,10,2,7,2,11,20,8]\n3\n4'
 *
 * 给你一个下标从 0 开始的整数数组 costs ，其中 costs[i] 是雇佣第 i 位工人的代价。
 *
 * 同时给你两个整数 k 和 candidates 。我们想根据以下规则恰好雇佣 k 位工人：
 *
 *
 * 总共进行 k 轮雇佣，且每一轮恰好雇佣一位工人。
 * 在每一轮雇佣中，从最前面 candidates 和最后面 candidates
 * 人中选出代价最小的一位工人，如果有多位代价相同且最小的工人，选择下标更小的一位工人。
 *
 * 比方说，costs = [3,2,7,7,1,2] 且 candidates = 2 ，第一轮雇佣中，我们选择第 4 位工人，因为他的代价最小
 * [3,2,7,7,1,2] 。
 * 第二轮雇佣，我们选择第 1 位工人，因为他们的代价与第 4 位工人一样都是最小代价，而且下标更小，[3,2,7,7,2]
 * 。注意每一轮雇佣后，剩余工人的下标可能会发生变化。
 *
 *
 * 如果剩余员工数目不足 candidates 人，那么下一轮雇佣他们中代价最小的一人，如果有多位代价相同且最小的工人，选择下标更小的一位工人。
 * 一位工人只能被选择一次。
 *
 *
 * 返回雇佣恰好 k 位工人的总代价。
 *
 *
 *
 * 示例 1：
 *
 * 输入：costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
 * 输出：11
 * 解释：我们总共雇佣 3 位工人。总代价一开始为 0 。
 * - 第一轮雇佣，我们从 [17,12,10,2,7,2,11,20,8] 中选择。最小代价是 2 ，有两位工人，我们选择下标更小的一位工人，即第 3
 * 位工人。总代价是 0 + 2 = 2 。
 * - 第二轮雇佣，我们从 [17,12,10,7,2,11,20,8] 中选择。最小代价是 2 ，下标为 4 ，总代价是 2 + 2 = 4 。
 * - 第三轮雇佣，我们从 [17,12,10,7,11,20,8] 中选择，最小代价是 7 ，下标为 3 ，总代价是 4 + 7 = 11 。注意下标为
 * 3 的工人同时在最前面和最后面 4 位工人中。
 * 总雇佣代价是 11 。
 *
 *
 * 示例 2：
 *
 * 输入：costs = [1,2,4,1], k = 3, candidates = 3
 * 输出：4
 * 解释：我们总共雇佣 3 位工人。总代价一开始为 0 。
 * - 第一轮雇佣，我们从 [1,2,4,1] 中选择。最小代价为 1 ，有两位工人，我们选择下标更小的一位工人，即第 0 位工人，总代价是 0 + 1 =
 * 1 。注意，下标为 1 和 2 的工人同时在最前面和最后面 3 位工人中。
 * - 第二轮雇佣，我们从 [2,4,1] 中选择。最小代价为 1 ，下标为 2 ，总代价是 1 + 1 = 2 。
 * - 第三轮雇佣，少于 3 位工人，我们从剩余工人 [2,4] 中选择。最小代价是 2 ，下标为 0 。总代价为 2 + 2 = 4 。
 * 总雇佣代价是 4 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= costs.length <= 10^5
 * 1 <= costs[i] <= 10^5
 * 1 <= k, candidates <= costs.length
 *
 *
 */
package leetcode

import (
	"container/heap"
	"sort"
)
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
type pair struct{x, y int}
type hp []pair

func(h hp) Len() int {return len(h)}
func(h hp) Less(i, j int) bool {return h[i].x < h[j].x || h[i].x == h[j].x && h[i].y < h[j].y}
func(h hp) Swap(i, j int) {h[i], h[j] = h[j], h[i]}
func(h *hp) Pop() any {a := *h; v := a[len(a) - 1] ; a = a[:len(a) - 1] ; *h = a; return v}
func(h *hp) Push(v any) {*h = append(*h, v.(pair))}


func totalCost(costs []int, k int, candidates int) (res int64) {

	if candidates * 2 >= len(costs){
		sort.Ints(costs)
		for i := 0 ; i < k ; i ++ {
			res += int64(costs[i])
		}
		return res 
	}

	a := []pair{}
	n := len(costs)
	for i := 0 ; i < n ; i ++ {
		a = append(a, pair{costs[i], i})
	}

	h1, h2 := hp{}, hp{}
	l, r := candidates - 1, n - candidates
	for i := 0 ;i < candidates ; i ++ {
		heap.Push(&h1, pair{costs[i], i})
		heap.Push(&h2, pair{costs[n - i - 1], n - i - 1})
	}
	for i := 0 ; i < k ; i ++ {
		if len(h1) > 0 && len(h2) > 0{
			p1 := heap.Pop(&h1).(pair) 
			p2 := heap.Pop(&h2).(pair) 
			if p1.x < p2.x || p1.x == p2.x && p1.y < p2.y{
				res += int64(p1.x)
				if l + 1 < r{
					heap.Push(&h1, pair{costs[l + 1], l + 1})
					l ++
				}
				heap.Push(&h2, p2)
			}else{
				res += int64(p2.x)
				if r - 1 > l {
					heap.Push(&h2, pair{costs[r - 1], r - 1})
					r --
				}
				heap.Push(&h1, p1)
			}
		}else if len(h1) > 0{
			p := heap.Pop(&h1).(pair)
			res += int64(p.x)
		}else{
			p := heap.Pop(&h2).(pair)
			res += int64(p.x)
		}
	}
	return 
}



// @lc code=end



/*
// @lcpr case=start
// [17,12,10,2,7,2,11,20,8]\n3\n4\n
// @lcpr case=end

// @lcpr case=start
// [1,2,4,1]\n3\n3\n
// @lcpr case=end

 */

