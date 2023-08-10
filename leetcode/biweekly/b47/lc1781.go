/*
 * @lc app=leetcode.cn id=1781 lang=golang
 * @lcpr version=21913
 *
 * [1781] 所有子字符串美丽值之和
 *
 * https://leetcode.cn/problems/sum-of-beauty-of-all-substrings/description/
 *
 * algorithms
 * Medium (66.49%)
 * Likes:    85
 * Dislikes: 0
 * Total Accepted:    24.9K
 * Total Submissions: 37.4K
 * Testcase Example:  '"aabcb"'
 *
 * 一个字符串的 美丽值 定义为：出现频率最高字符与出现频率最低字符的出现次数之差。
 * 
 * 
 * 比方说，"abaacc" 的美丽值为 3 - 1 = 2 。
 * 
 * 
 * 给你一个字符串 s ，请你返回它所有子字符串的 美丽值 之和。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：s = "aabcb"
 * 输出：5
 * 解释：美丽值不为零的字符串包括 ["aab","aabc","aabcb","abcb","bcb"] ，每一个字符串的美丽值都为 1 。
 * 
 * 示例 2：
 * 
 * 输入：s = "aabcbaa"
 * 输出：17
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <=^ 500
 * s 只包含小写英文字母。
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
func beautySum(s string) int {
	res := 0
	for i := 0; i < len(s); i++ {
		cnt := make(map[byte]int)
		for j := i; j < len(s); j++ {
			cnt[s[j]]++
			maxVal, minVal := 0, len(s)
			for _, v := range cnt {
				if v > maxVal {
					maxVal = v
				}
				if v < minVal {
					minVal = v
				}
			}
			res += maxVal - minVal
		}
	}
	return res
}
// @lc code=end



/*
// @lcpr case=start
// "aabcb"\n
// @lcpr case=end

// @lcpr case=start
// "aabcbaa"\n
// @lcpr case=end

 */

