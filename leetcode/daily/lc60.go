/*
 * @lc app=leetcode.cn id=60 lang=golang
 * @lcpr version=21913
 *
 * [60] 排列序列
 *
 * https://leetcode.cn/problems/permutation-sequence/description/
 *
 * algorithms
 * Hard (53.51%)
 * Likes:    796
 * Dislikes: 0
 * Total Accepted:    131.9K
 * Total Submissions: 246.5K
 * Testcase Example:  '3\n3'
 *
 * 给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
 * 
 * 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
 * 
 * 
 * "123"
 * "132"
 * "213"
 * "231"
 * "312"
 * "321"
 * 
 * 
 * 给定 n 和 k，返回第 k 个排列。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：n = 3, k = 3
 * 输出："213"
 * 
 * 
 * 示例 2：
 * 
 * 输入：n = 4, k = 9
 * 输出："2314"
 * 
 * 
 * 示例 3：
 * 
 * 输入：n = 3, k = 1
 * 输出："123"
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n <= 9
 * 1 <= k <= n!
 72 * 42 * 120
 72 * (84+ 420) * 10
 72 * 504 * 10
 350000
 * 
 * 
 */
package leetcode
type TreeNode struct {
    Val int
    Right *TreeNode
    Left *TreeNode
}
// @lc code=start
func getPermutation(n int, k int) string {

}
// @lc code=end



/*
// @lcpr case=start
// 3\n3\n
// @lcpr case=end

// @lcpr case=start
// 4\n9\n
// @lcpr case=end

// @lcpr case=start
// 3\n1\n
// @lcpr case=end

 */

