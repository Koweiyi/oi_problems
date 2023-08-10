/*
 * @lc app=leetcode.cn id=2384 lang=golang
 * @lcpr version=21913
 *
 * [2384] 最大回文数字
 *
 * https://leetcode.cn/problems/largest-palindromic-number/description/
 *
 * algorithms
 * Medium (31.18%)
 * Likes:    21
 * Dislikes: 0
 * Total Accepted:    10.2K
 * Total Submissions: 32.6K
 * Testcase Example:  '"444947137"'
 *
 * 给你一个仅由数字（0 - 9）组成的字符串 num 。
 *
 * 请你找出能够使用 num 中数字形成的 最大回文 整数，并以字符串形式返回。该整数不含 前导零 。
 *
 * 注意：
 *
 *
 * 你 无需 使用 num 中的所有数字，但你必须使用 至少 一个数字。
 * 数字可以重新排序。
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：num = "444947137"
 * 输出："7449447"
 * 解释：
 * 从 "444947137" 中选用数字 "4449477"，可以形成回文整数 "7449447" 。
 * 可以证明 "7449447" 是能够形成的最大回文整数。
 *
 *
 * 示例 2：
 *
 * 输入：num = "00009"
 * 输出："9"
 * 解释：
 * 可以证明 "9" 能够形成的最大回文整数。
 * 注意返回的整数不应含前导零。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= num.length <= 10^5
 * num 由数字（0 - 9）组成
 *
 *
 */
package leetcode

import (
	"strings"
)

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}
// @lc code=start
func largestPalindromic(num string) string {
	record := ['9' + 1]int{}
	for _, x := range num{
		record[x] ++
	}
	if record['0'] == len(num){
		return "0"
	}
	res := []byte{}
	for i := byte('9') ; i > '0' || i == '0' && len(res) > 0 ; i --{
		for j := 0 ; j < record[i] / 2 ; j ++ {
			res = append(res, i)
		}
	}
	j := len(res) - 1
	for i := byte('9') ; i >= '0' ; i --{
		if record[i] & 1 > 0{
			res = append(res, i)
			break
		}
	}
	for ; j >= 0 ; j --{
		res = append(res, res[j])
	}
	return string(res)

}
// @lc code=end



/*
// @lcpr case=start
// "444947137"\n
// @lcpr case=end

// @lcpr case=start
// "00009"\n
// @lcpr case=end

 */

