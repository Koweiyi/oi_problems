/*
 * @lc app=leetcode.cn id=93 lang=golang
 * @lcpr version=21913
 *
 * [93] 复原 IP 地址
 *
 * https://leetcode.cn/problems/restore-ip-addresses/description/
 *
 * algorithms
 * Medium (58.23%)
 * Likes:    1283
 * Dislikes: 0
 * Total Accepted:    355.8K
 * Total Submissions: 611K
 * Testcase Example:  '"25525511135"'
 *
 * 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
 *
 *
 * 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312"
 * 和 "192.168@1.1" 是 无效 IP 地址。
 *
 *
 * 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能
 * 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。
 *
 *
 *
 * 示例 1：
 *
 * 输入：s = "25525511135"
 * 输出：["255.255.11.135","255.255.111.35"]
 *
 *
 * 示例 2：
 *
 * 输入：s = "0000"
 * 输出：["0.0.0.0"]
 *
 *
 * 示例 3：
 *
 * 输入：s = "101023"
 * 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 20
 * s 仅由数字组成
 *
 *
 */
package leetcode

import (
	"strconv"
	"strings"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
type ListNode struct {
	Val  int
	Next *ListNode
}

// @lc code=start
func restoreIpAddresses(s string) (res []string) {
	// 因为只有20长度，直接暴力枚举三个分割位置就好了

	// 理论上最长长度时3 * 4 = 12 大于12 无法复原
	if len(s) > 12 {
		return
	}
	ip := []string{}
	var dfs func(i, pre, cnt int)
	dfs = func(i, pre, cnt int) {
		if i == len(s) {
			if pre == i && cnt == 4 {
				res = append(res, strings.Join(ip, "."))
			}
			return
		}
		// 选当前字母 check 的逻辑是 s[pre:i + 1]是否是合法数值字符串，并传化为数字之后 在[0, 255]之间
		if cnt < 4 && check(s[pre:i+1]) {
			ip = append(ip, s[pre:i+1])
			dfs(i+1, i+1, cnt+1)
			ip = ip[:len(ip)-1]
		}
		dfs(i+1, pre, cnt)
	}
	dfs(0, 0, 0)
	return
}

func check(s string) bool {
	if s == "0" {
		return true
	}
	if s[0] == '0' {
		return false
	}
	sint, _ := strconv.Atoi(s)
	return sint >= 0 && sint <= 255
}

// @lc code=end

/*
// @lcpr case=start
// "25525511135"\n
// @lcpr case=end

// @lcpr case=start
// "0000"\n
// @lcpr case=end

// @lcpr case=start
// "101023"\n
// @lcpr case=end

// @lcpr case=start
// "000256"\n
// @lcpr case=end
*/
