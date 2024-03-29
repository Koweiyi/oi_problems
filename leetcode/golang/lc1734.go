/*
 * @lc app=leetcode.cn id=1734 lang=golang
 * @lcpr version=30109
 *
 * [1734] 解码异或后的排列
 *
 * https://leetcode.cn/problems/decode-xored-permutation/description/
 *
 * algorithms
 * Medium (72.45%)
 * Likes:    164
 * Dislikes: 0
 * Total Accepted:    29.9K
 * Total Submissions: 41.3K
 * Testcase Example:  '[3,1]'
 *
 * 给你一个整数数组 perm ，它是前 n 个正整数的排列，且 n 是个 奇数 。
 *
 * 它被加密成另一个长度为 n - 1 的整数数组 encoded ，满足 encoded[i] = perm[i] XOR perm[i + 1]
 * 。比方说，如果 perm = [1,3,2] ，那么 encoded = [2,1] 。
 *
 * 给你 encoded 数组，请你返回原始数组 perm 。题目保证答案存在且唯一。
 *
 *
 *
 * 示例 1：
 *
 * 输入：encoded = [3,1]
 * 输出：[1,2,3]
 * 解释：如果 perm = [1,2,3] ，那么 encoded = [1 XOR 2,2 XOR 3] = [3,1]
 *
 *
 * 示例 2：
 *
 * 输入：encoded = [6,5,4,6]
 * 输出：[2,4,1,5,3]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 3 <= n < 10^5
 * n 是奇数。
 * encoded.length == n - 1
 *
 *
 */

// @lcpr-template-start
package leetcode

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
func decode(encoded []int) []int {
	     
	mask := 0 
	n := len(encoded) + 1
	for i := 1; i <= n ; i ++ {
		mask = mask ^ i 	
	}		
	res := make([]int, n)
	res[len(res) - 1] = mask
	for i := 0 ; i < n - 1; i += 2 {
		res[len(res) - 1] ^= encoded[i]
	}

	for j := n - 2 ; j >= 0 ; j -- {
		res[j] = res[j + 1] ^ encoded[j]
	}
	return res 
}

// @lc code=end

/*
// @lcpr case=start
// [3,1]\n
// @lcpr case=end

// @lcpr case=start
// [6,5,4,6]\n
// @lcpr case=end

*/
