/*
 * @lc app=leetcode.cn id=2531 lang=golang
 * @lcpr version=21913
 *
 * [2531] 使字符串总不同字符的数目相等
 *
 * https://leetcode.cn/problems/make-number-of-distinct-characters-equal/description/
 *
 * algorithms
 * Medium (29.77%)
 * Likes:    25
 * Dislikes: 0
 * Total Accepted:    5.7K
 * Total Submissions: 19.2K
 * Testcase Example:  '"ac"\n"b"'
 *
 * 给你两个下标从 0 开始的字符串 word1 和 word2 。
 * 
 * 一次 移动 由以下两个步骤组成：
 * 
 * 
 * 选中两个下标 i 和 j ，分别满足 0 <= i < word1.length 和 0 <= j < word2.length ，
 * 交换 word1[i] 和 word2[j] 。
 * 
 * 
 * 如果可以通过 恰好一次 移动，使 word1 和 word2 中不同字符的数目相等，则返回 true ；否则，返回 false 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：word1 = "ac", word2 = "b"
 * 输出：false
 * 解释：交换任何一组下标都会导致第一个字符串中有 2 个不同的字符，而在第二个字符串中只有 1 个不同字符。
 * 
 * 
 * 示例 2：
 * 
 * 输入：word1 = "abcc", word2 = "aab"
 * 输出：true
 * 解释：交换第一个字符串的下标 2 和第二个字符串的下标 0 。之后得到 word1 = "abac" 和 word2 = "cab" ，各有 3
 * 个不同字符。
 * 
 * 
 * 示例 3：
 * 
 * 输入：word1 = "abcde", word2 = "fghij"
 * 输出：true
 * 解释：无论交换哪一组下标，两个字符串中都会有 5 个不同字符。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= word1.length, word2.length <= 10^5
 * word1 和 word2 仅由小写英文字母组成。
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
func isItPossible(word1 string, word2 string) bool {
	c1 := map[rune]int{}
	c2 := map[rune]int{}
	for _, x := range word1{
		c1[x] ++ 
	}
	for _, x := range word2{
		c2[x] ++
	}
	for k1, v1 := range c1{
		for k2, v2 := range c2 {
			if k1 == k2{
				if len(c1) == len(c2){
					return true
				}
			}else{
				l1 := len(c1) 
				if v1 == 1{
					l1 -- 
				}
				if _, ok := c1[k2] ; !ok {
					l1 ++ 
				}
				l2 := len(c2) 
				if v2 == 1{
					l2 -- 
				}
				if _, ok := c2[k1] ; !ok {
					l2 ++ 
				}
				if l1 == l2 {
					return true
				}
			}
		}
	}
	return false

	
}
// @lc code=end



/*
// @lcpr case=start
// "ac"\n"b"\n
// @lcpr case=end

// @lcpr case=start
// "abcc"\n"aab"\n
// @lcpr case=end

// @lcpr case=start
// "abcde"\n"fghij"\n
// @lcpr case=end

 */

