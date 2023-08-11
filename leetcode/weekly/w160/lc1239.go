/*
 * @lc app=leetcode.cn id=1239 lang=golang
 * @lcpr version=21913
 *
 * [1239] 串联字符串的最大长度
 *
 * https://leetcode.cn/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
 *
 * algorithms
 * Medium (49.09%)
 * Likes:    224
 * Dislikes: 0
 * Total Accepted:    40.9K
 * Total Submissions: 83.4K
 * Testcase Example:  '["un","iq","ue"]'
 *
 * 给定一个字符串数组 arr，字符串 s 是将 arr 的含有 不同字母 的 子序列 字符串 连接 所得的字符串。
 *
 * 请返回所有可行解 s 中最长长度。
 *
 * 子序列 是一种可以从另一个数组派生而来的数组，通过删除某些元素或不删除元素而不改变其余元素的顺序。
 *
 *
 *
 * 示例 1：
 *
 * 输入：arr = ["un","iq","ue"]
 * 输出：4
 * 解释：所有可能的串联组合是：
 * - ""
 * - "un"
 * - "iq"
 * - "ue"
 * - "uniq" ("un" + "iq")
 * - "ique" ("iq" + "ue")
 * 最大长度为 4。
 *
 *
 * 示例 2：
 *
 * 输入：arr = ["cha","r","act","ers"]
 * 输出：6
 * 解释：可能的解答有 "chaers" 和 "acters"。
 *
 *
 * 示例 3：
 *
 * 输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
 * 输出：26
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= arr.length <= 16
 * 1 <= arr[i].length <= 26
 * arr[i] 中只含有小写英文字母
 *
 *
 */
package main

import "fmt"
type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}
// @lc code=start
func maxLength(arr []string) int {
	nums := make([]int, len(arr))
	canUse := make([]bool, len(arr))
	nxt:
	for i := 0 ; i < len(arr) ; i ++ {
		num := 0 
		canUse[i] = true
		for _, x := range arr[i]{
			if num >> (x - 'a') & 1 != 0{
				canUse[i] = false
				continue nxt
			}
			num |= (1 << (x - 'a'))
		}
		nums[i] = num
	}
	res := 0
	var dfs func(i, s int)
	dfs = func(i, s int) {
		if i == len(arr){
			res = max(res, bitLength(s))
			return
		}
		dfs(i + 1, s)
		if canUse[i] && s & nums[i] == 0{
			dfs(i + 1, s | nums[i])
		}
	}
	dfs(0, 0)
	return res 
}
func max(a, b int) int {if a > b {return a}; return b}

func bitLength(x int) int {
	res := 0
	for x > 0{
		if x & 1 == 1{
			res ++
		}
		x /= 2
	}
	return res 
}
// @lc code=end

func main(){
	arr := []string{"aa", "bb", "cc"}
	res := maxLength(arr)
	fmt.Println(res)
}


/*
// @lcpr case=start
// ["un","iq","ue"]\n
// @lcpr case=end

// @lcpr case=start
// ["aa","bb","cc"]\n
// @lcpr case=end
// @lcpr case=start
// ["cha","r","act","ers"]\n
// @lcpr case=end

// @lcpr case=start
// ["abcdefghijklmnopqrstuvwxyz"]\n
// @lcpr case=end

 */

