/*
 * @lc app=leetcode.cn id=2547 lang=golang
 * @lcpr version=30104
 *
 * [2547] 拆分数组的最小代价
 *
 * https://leetcode.cn/problems/minimum-cost-to-split-an-array/description/
 *
 * algorithms
 * Hard (56.75%)
 * Likes:    27
 * Dislikes: 0
 * Total Accepted:    3.5K
 * Total Submissions: 6.2K
 * Testcase Example:  '[1,2,1,2,1,3,3]\n2'
 *
 * 给你一个整数数组 nums 和一个整数 k 。
 *
 * 将数组拆分成一些非空子数组。拆分的 代价 是每个子数组中的 重要性 之和。
 *
 * 令 trimmed(subarray) 作为子数组的一个特征，其中所有仅出现一次的数字将会被移除。
 *
 *
 * 例如，trimmed([3,1,2,4,3,4]) = [3,4,3,4] 。
 *
 *
 * 子数组的 重要性 定义为 k + trimmed(subarray).length 。
 *
 *
 * 例如，如果一个子数组是 [1,2,3,3,3,4,4] ，trimmed([1,2,3,3,3,4,4]) = [3,3,3,4,4]
 * 。这个子数组的重要性就是 k + 5 。
 *
 *
 * 找出并返回拆分 nums 的所有可行方案中的最小代价。
 *
 * 子数组 是数组的一个连续 非空 元素序列。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [1,2,1,2,1,3,3], k = 2
 * 输出：8
 * 解释：将 nums 拆分成两个子数组：[1,2], [1,2,1,3,3]
 * [1,2] 的重要性是 2 + (0) = 2 。
 * [1,2,1,3,3] 的重要性是 2 + (2 + 2) = 6 。
 * 拆分的代价是 2 + 6 = 8 ，可以证明这是所有可行的拆分方案中的最小代价。
 *
 *
 * 示例 2：
 *
 * 输入：nums = [1,2,1,2,1], k = 2
 * 输出：6
 * 解释：将 nums 拆分成两个子数组：[1,2], [1,2,1] 。
 * [1,2] 的重要性是 2 + (0) = 2 。
 * [1,2,1] 的重要性是 2 + (2) = 4 。
 * 拆分的代价是 2 + 4 = 6 ，可以证明这是所有可行的拆分方案中的最小代价。
 *
 *
 * 示例 3：
 *
 * 输入：nums = [1,2,1,2,1], k = 5
 * 输出：10
 * 解释：将 nums 拆分成一个子数组：[1,2,1,2,1].
 * [1,2,1,2,1] 的重要性是 5 + (3 + 2) = 10 。
 * 拆分的代价是 10 ，可以证明这是所有可行的拆分方案中的最小代价。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 1000
 * 0 <= nums[i] < nums.length
 * 1 <= k <= 10^9
 *
 *
 *
 *
 */

// @lcpr-template-start
package leetcode

import (
	"fmt"
	"runtime/internal/math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
type ListNode struct {
	Val  int
	Next *ListNode
}

// @lcpr-template-end
// @lc code=start
func minCost(nums []int, k int) int {

	// dp 
	// 子数组中有多少单一数字
	n := len(nums)
	cnt := make([][]int64, n)
	for i := range cnt{
		cnt[i] = make([]int64, n)
	}
	for i := 0 ; i < n ; i ++ {
		s := map[int]int{}
		c := 0
		for j := i ; j < n ; j ++ {
			s[nums[j]] += 1 
			if s[nums[j]] == 1{
				c += 1
			}else if s[nums[j]] == 2{
				c -= 1 
			}
			cnt[i][j] = int64(j - i + 1) - int64(c)
		}
	}
	// fmt.Println(cnt)

	dp := make([]int64, n + 1)
	for i := 1 ; i <= n ; i ++{
		dp[i] = 1e13 + 7
	}
	for i := 0 ; i < n ; i ++ {
		for j := i; j >= 0 ; j -- {
			dp[i + 1] = min(dp[i + 1], dp[j] + cnt[j][i] + int64(k))
		}
	}
	// fmt.Println(dp)
	return int(dp[len(dp) - 1])

}

func min(a, b int64) int64{if a < b{return a} ; return b}

// @lc code=end

/*
// @lcpr case=start
// [1,2,1,2,1,3,3]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1,2,1,2,1]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1,2,1,2,1]\n5\n
// @lcpr case=end

*/
