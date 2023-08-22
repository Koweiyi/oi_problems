/*
 * @lc app=leetcode.cn id=394 lang=golang
 * @lcpr version=21913
 *
 * [394] 字符串解码
 *
 * https://leetcode.cn/problems/decode-string/description/
 *
 * algorithms
 * Medium (56.77%)
 * Likes:    1566
 * Dislikes: 0
 * Total Accepted:    255.3K
 * Total Submissions: 449.7K
 * Testcase Example:  '"3[a]2[bc]"'
 *
 * 给定一个经过编码的字符串，返回它解码后的字符串。
 * 
 * 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
 * 
 * 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
 * 
 * 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：s = "3[a]2[bc]"
 * 输出："aaabcbc"
 * 
 * 
 * 示例 2：
 * 
 * 输入：s = "3[a2[c]]"
 * 输出："accaccacc"
 * 
 * 
 * 示例 3：
 * 
 * 输入：s = "2[abc]3[cd]ef"
 * 输出："abcabccdcdcdef"
 * 
 * 
 * 示例 4：
 * 
 * 输入：s = "abc3[cd]xyz"
 * 输出："abccdcdcdxyz"
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <= 30
 * s 由小写英文字母、数字和方括号 '[]' 组成
 * s 保证是一个 有效 的输入。
 * s 中所有整数的取值范围为 [1, 300] 
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


func decodeString(s string) string {
    // 预处理出每一个[ 对应的 ] 所在的位置， 遇到进行递归括号内字符串就好了

    // code
    st := []int{}
    record := map[int]int{}
    for i := 0 ; i < len(s) ; i ++{
        if s[i] == '['{
            st = append(st, i)
        }
        if s[i] == ']'{
            record[st[len(st) - 1]] = i 
            st = st[:len(st) - 1]
        }
    }

    var dfs func(l, r int) string
    dfs = func(l, r int) string {
        res := []rune{}
        for i := l ; i <= r ; {
            if isalph(s[i]) {
                res = append(res, rune(s[i]))
                i ++
            }else if isdigit(s[i]){
                num := int(s[i] - '0')
                for i + 1 <= r && isdigit(s[i + 1]){
                    i ++
                    num = num * 10 + int(s[i] - '0')
                }
                sub := dfs(i + 2, record[i + 1] - 1)
                for j := 0 ; j < num ; j ++ {
                    res = append(res, []rune(sub)...)
                }
                i = record[i + 1] + 1
            }
        }
        return string(res)
    }
    return dfs(0, len(s) - 1)
}

func isdigit(b byte) bool{
    return '0' <= b && b <= '9'
}

func isalph(b byte) bool{
    return 'a' <= b && b <= 'z'
}

// @lc code=end



/*
// @lcpr case=start
// "3[a]2[bc]"\n
// @lcpr case=end

// @lcpr case=start
// "3[a2[c]]"\n
// @lcpr case=end

// @lcpr case=start
// "2[abc]3[cd]ef"\n
// @lcpr case=end

// @lcpr case=start
// "abc3[cd]xyz"\n
// @lcpr case=end

 */

