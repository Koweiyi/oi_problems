/*
 * @lc app=leetcode.cn id=948 lang=golang
 * @lcpr version=21913
 *
 * [948] 令牌放置
 *
 * https://leetcode.cn/problems/bag-of-tokens/description/
 *
 * algorithms
 * Medium (40.62%)
 * Likes:    88
 * Dislikes: 0
 * Total Accepted:    10.4K
 * Total Submissions: 25.6K
 * Testcase Example:  '[100]\n50'
 *
 * 你的初始 能量 为 power，初始 分数 为 0，只有一包令牌 tokens 。其中 tokens[i] 是第 i 个令牌的值（下标从 0 开始）。
 *
 * 令牌可能的两种使用方法如下：
 *
 *
 * 如果你至少有 token[i] 点 能量 ，可以将令牌 i 置为正面朝上，失去 token[i] 点 能量 ，并得到 1 分 。
 * 如果我们至少有 1 分 ，可以将令牌 i 置为反面朝上，获得 token[i] 点 能量 ，并失去 1 分 。
 *
 *
 * 每个令牌 最多 只能使用一次，使用 顺序不限 ，不需 使用所有令牌。
 *
 * 在使用任意数量的令牌后，返回我们可以得到的最大 分数 。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：tokens = [100], power = 50
 * 输出：0
 * 解释：无法使用唯一的令牌，因为能量和分数都太少了。
 *
 * 示例 2：
 *
 * 输入：tokens = [100,200], power = 150
 * 输出：1
 * 解释：令牌 0 正面朝上，能量变为 50，分数变为 1 。
 * 不必使用令牌 1 ，因为你无法使用它来提高分数。
 *
 * 示例 3：
 *
 * 输入：tokens = [100,200,300,400], power = 200
 * 输出：2
 * 解释：按下面顺序使用令牌可以得到 2 分：
 * 1. 令牌 0 正面朝上，能量变为 100 ，分数变为 1
 * 2. 令牌 3 正面朝下，能量变为 500 ，分数变为 0
 * 3. 令牌 1 正面朝上，能量变为 300 ，分数变为 1
 * 4. 令牌 2 正面朝上，能量变为 0 ，分数变为 2
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= tokens.length <= 1000
 * 0 <= tokens[i], power < 10^4
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
type ListNode struct {
    Val int
    Next *ListNode
}
// @lc code=start
func bagOfTokensScore(tokens []int, power int) int {
	// 贪心

	if len(tokens) == 0{
		return 0
	}
	sort.Ints(tokens)
	n := len(tokens)
	s := make([]int, n + 1)
	for i := 0 ; i < n ; i ++ {
		s[i + 1] = s[i] + tokens[i]
	}
	res := 0
	for cur := 0 ; cur <= n / 2 ; cur ++ {
		p := power - s[cur] + s[n] - s[n - cur]
		r := cur
		for r < n - cur && p >= tokens[r]{
			p -= tokens[r]
			r ++
		}
		res = max(res, r - cur)
		if (r == cur) {break}
	}
	return res 
}
func max(a, b int) int {if a > b {return a}; return b}

// @lc code=end



/*
// @lcpr case=start
// [100]\n50\n
// @lcpr case=end

// @lcpr case=start
// [100,200]\n150\n
// @lcpr case=end

// @lcpr case=start
// [100,200,300,400]\n200\n
// @lcpr case=end

// @lcpr case=start
// []\n85\n
// @lcpr case=end

// @lcpr case=start
// [26]\n51\n
// @lcpr case=end
// @lcpr case=start
// [71, 55, 82]\n54\n
// @lcpr case=end
 */

