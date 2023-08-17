/*
 * @lc app=leetcode.cn id=1220 lang=golang
 * @lcpr version=21913
 *
 * [1220] 统计元音字母序列的数目
 *
 * https://leetcode.cn/problems/count-vowels-permutation/description/
 *
 * algorithms
 * Hard (60.73%)
 * Likes:    165
 * Dislikes: 0
 * Total Accepted:    27K
 * Total Submissions: 44.4K
 * Testcase Example:  '1'
 *
 * 给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：
 * 
 * 
 * 字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
 * 每个元音 'a' 后面都只能跟着 'e'
 * 每个元音 'e' 后面只能跟着 'a' 或者是 'i'
 * 每个元音 'i' 后面 不能 再跟着另一个 'i'
 * 每个元音 'o' 后面只能跟着 'i' 或者是 'u'
 * 每个元音 'u' 后面只能跟着 'a'
 * 
 * 
 * 由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：n = 1
 * 输出：5
 * 解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。
 * 
 * 
 * 示例 2：
 * 
 * 输入：n = 2
 * 输出：10
 * 解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和
 * "ua"。
 * 
 * 
 * 示例 3：
 * 
 * 输入：n = 5
 * 输出：68
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n <= 2 * 10^4
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
func countVowelPermutation(n int) int {
	// dp[i][0] ~ dp[i][4] 分别表示长度为 i+ 1 的字符串并且结尾是 aeiou 的字符串种数
	const mod int = 1_000_000_007
	dp := make([][]int, 2)
	for i := range dp {
		dp[i] = make([]int, 5)
	}	
	for i := 0 ; i < 5 ; i ++ {
		dp[0][i] = 1
	}
	for i := 1 ; i < n ; i ++ {
		dp[i % 2][0] = ((dp[(i - 1) % 2][1] + dp[(i - 1) % 2][2] ) % mod + dp[(i - 1) % 2][4]) % mod
		dp[i % 2][1] = (dp[(i - 1) % 2][0] + dp[(i - 1) % 2][2]) % mod 
		dp[i % 2][2] = (dp[(i - 1) % 2][1] + dp[(i - 1) % 2][3]) % mod
		dp[i % 2][3] = dp[(i - 1) % 2][2]
		dp[i % 2][4] = (dp[(i - 1) % 2][2] + dp[(i - 1) % 2][3]) % mod
	}
	res := 0
	for  i := 0 ; i < 5 ; i ++ {
		res = (res + dp[(n - 1) % 2][i]) % mod
	}
	return res
}
// @lc code=end



/*
// @lcpr case=start
// 1\n
// @lcpr case=end

// @lcpr case=start
// 2\n
// @lcpr case=end

// @lcpr case=start
// 5\n
// @lcpr case=end

 */

