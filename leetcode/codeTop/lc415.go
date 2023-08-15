/*
 * @lc app=leetcode.cn id=415 lang=golang
 * @lcpr version=21913
 *
 * [415] 字符串相加
 *
 * https://leetcode.cn/problems/add-strings/description/
 *
 * algorithms
 * Easy (54.76%)
 * Likes:    782
 * Dislikes: 0
 * Total Accepted:    295.6K
 * Total Submissions: 539.8K
 * Testcase Example:  '"11"\n"123"'
 *
 * 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
 * 
 * 你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：num1 = "11", num2 = "123"
 * 输出："134"
 * 
 * 
 * 示例 2：
 * 
 * 输入：num1 = "456", num2 = "77"
 * 输出："533"
 * 
 * 
 * 示例 3：
 * 
 * 输入：num1 = "0", num2 = "0"
 * 输出："0"
 * 
 * 
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= num1.length, num2.length <= 10^4
 * num1 和num2 都只包含数字 0-9
 * num1 和num2 都不包含任何前导零
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
func addStrings(num1 string, num2 string) string {
	// 十进制模拟
	carry := 0 
	res := []byte{}
	for len(num1) > 0 && len(num2) > 0 {
		a, b := num1[len(num1) - 1] - '0', num2[len(num2) - 1] - '0'
		num1 = num1[:len(num1) - 1]
		num2 = num2[:len(num2) - 1]
		s := int(a) + int(b) + carry
		res = append(res, byte(s % 10 + '0'))
		carry = s / 10 
	}
	for len(num1) > 0{
		s := int(num1[len(num1) - 1] - '0') + carry 
		carry = s / 10 
		res = append(res, byte(s % 10 + '0'))
		num1 = num1[:len(num1) - 1]
	} 
	for len(num2) > 0{
		s := int(num2[len(num2) - 1] - '0') + carry 
		carry = s / 10 
		res = append(res, byte(s % 10 + '0'))
		num2 = num2[:len(num2) - 1]
	}
	if carry == 1{
		res = append(res, '1')
	}
	for i := 0 ; i < len(res) / 2 ; i ++ {
		res[i], res[len(res) - i - 1] = res[len(res) - i - 1], res[i]
	} 
	return string(res)
}
// @lc code=end



/*
// @lcpr case=start
// "11"\n"123"\n
// @lcpr case=end

// @lcpr case=start
// "456"\n"77"\n
// @lcpr case=end

// @lcpr case=start
// "0"\n"0"\n
// @lcpr case=end

// @lcpr case=start
// "6"\n"501"\n
// @lcpr case=end
 */

