/*
 * @lc app=leetcode.cn id=2337 lang=golang
 * @lcpr version=21913
 *
 * [2337] 移动片段得到字符串
 *
 * https://leetcode.cn/problems/move-pieces-to-obtain-a-string/description/
 *
 * algorithms
 * Medium (39.33%)
 * Likes:    72
 * Dislikes: 0
 * Total Accepted:    14.1K
 * Total Submissions: 31.5K
 * Testcase Example:  '"_L__R__R_"\n"L______RR"'
 *
 * 给你两个字符串 start 和 target ，长度均为 n 。每个字符串 仅 由字符 'L'、'R' 和 '_' 组成，其中：
 *
 *
 * 字符 'L' 和 'R' 表示片段，其中片段 'L' 只有在其左侧直接存在一个 空位 时才能向 左 移动，而片段 'R' 只有在其右侧直接存在一个 空位
 * 时才能向 右 移动。
 * 字符 '_' 表示可以被 任意 'L' 或 'R' 片段占据的空位。
 *
 *
 * 如果在移动字符串 start 中的片段任意次之后可以得到字符串 target ，返回 true ；否则，返回 false 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：start = "_L__R__R_", target = "L______RR"
 * 输出：true
 * 解释：可以从字符串 start 获得 target ，需要进行下面的移动：
 * - 将第一个片段向左移动一步，字符串现在变为 "L___R__R_" 。
 * - 将最后一个片段向右移动一步，字符串现在变为 "L___R___R" 。
 * - 将第二个片段向右移动散步，字符串现在变为 "L______RR" 。
 * 可以从字符串 start 得到 target ，所以返回 true 。
 *
 *
 * 示例 2：
 *
 * 输入：start = "R_L_", target = "__LR"
 * 输出：false
 * 解释：字符串 start 中的 'R' 片段可以向右移动一步得到 "_RL_" 。
 * 但是，在这一步之后，不存在可以移动的片段，所以无法从字符串 start 得到 target 。
 *
 *
 * 示例 3：
 *
 * 输入：start = "_R", target = "R_"
 * 输出：false
 * 解释：字符串 start 中的片段只能向右移动，所以无法从字符串 start 得到 target 。
 *
 *
 *
 * 提示：
 *
 *
 * n == start.length == target.length
 * 1 <= n <= 10^5
 * start 和 target 由字符 'L'、'R' 和 '_' 组成
 *
 *
 */
package leetcode

import "strings"
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
func canChange(start string, target string) bool {

	// 每日一题
	// L, R的排列必须一致
	if strings.ReplaceAll(start, "_", "") != strings.ReplaceAll(target, "_", ""){
		return false
	}
	j := 0
	for i, x := range start{
		if x != '_'{
			for target[j] == '_'{
				j ++
			}
			// start中的L 下标i 与对应target中下标j 需要满足 i >= j
			// start中的R 下标i 与对应target中下标j 需要满足 i <= j
			if i != j && (x == 'L') == (i < j){
				return false
			} 
			j ++
		}
	}
	return true
}
// @lc code=end



/*
// @lcpr case=start
// "_L__R__R_"\n"L______RR"\n
// @lcpr case=end

// @lcpr case=start
// "R_L_"\n"__LR"\n
// @lcpr case=end

// @lcpr case=start
// "_R"\n"R_"\n
// @lcpr case=end

 */

