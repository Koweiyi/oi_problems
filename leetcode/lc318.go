/*
 * @lc app=leetcode.cn id=318 lang=golang
 * @lcpr version=30105
 *
 * [318] 最大单词长度乘积
 *
 * https://leetcode.cn/problems/maximum-product-of-word-lengths/description/
 *
 * algorithms
 * Medium (72.46%)
 * Likes:    468
 * Dislikes: 0
 * Total Accepted:    80K
 * Total Submissions: 110.2K
 * Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
 *
 * 给你一个字符串数组 words ，找出并返回 length(words[i]) * length(words[j])
 * 的最大值，并且这两个单词不含有公共字母。如果不存在这样的两个单词，返回 0 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：words = ["abcw","baz","foo","bar","xtfn","abcdef"]
 * 输出：16
 * 解释：这两个单词为 "abcw", "xtfn"。
 *
 * 示例 2：
 *
 * 输入：words = ["a","ab","abc","d","cd","bcd","abcd"]
 * 输出：4
 * 解释：这两个单词为 "ab", "cd"。
 *
 * 示例 3：
 *
 * 输入：words = ["a","aa","aaa","aaaa"]
 * 输出：0
 * 解释：不存在这样的两个单词。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 2 <= words.length <= 1000
 * 1 <= words[i].length <= 1000
 * words[i] 仅包含小写字母
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
func maxProduct(words []string) int {
	n := len(words)
	masks := make([]int, n) 
	for i, w := range words{
		for _, ch := range w{
			masks[i] |= 1 << (ch - 'a')
		}
	}
	res := 0 
	for i:= 0 ; i < n ; i ++ {
		for j := 0; j < n ; j ++ {
			if masks[i] & masks[j] == 0{
				res = max(res, len(words[i]) * len(words[j]))
			}
		}
	}
	return res 
}

// @lc code=end

/*
// @lcpr case=start
// ["abcw","baz","foo","bar","xtfn","abcdef"]\n
// @lcpr case=end

// @lcpr case=start
// ["a","ab","abc","d","cd","bcd","abcd"]\n
// @lcpr case=end

// @lcpr case=start
// ["a","aa","aaa","aaaa"]\n
// @lcpr case=end

*/
