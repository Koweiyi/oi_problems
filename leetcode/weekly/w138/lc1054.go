/*
 * @lc app=leetcode.cn id=1054 lang=golang
 * @lcpr version=21913
 *
 * [1054] 距离相等的条形码
 *
 * https://leetcode.cn/problems/distant-barcodes/description/
 *
 * algorithms
 * Medium (44.83%)
 * Likes:    175
 * Dislikes: 0
 * Total Accepted:    25.7K
 * Total Submissions: 57.3K
 * Testcase Example:  '[1,1,1,2,2,2]'
 *
 * 在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。
 *
 * 请你重新排列这些条形码，使其中任意两个相邻的条形码不能相等。 你可以返回任何满足该要求的答案，此题保证存在答案。
 *
 *
 *
 * 示例 1：
 *
 * 输入：barcodes = [1,1,1,2,2,2]
 * 输出：[2,1,2,1,2,1]
 *
 *
 * 示例 2：
 *
 * 输入：barcodes = [1,1,1,1,2,2,3,3]
 * 输出：[1,3,1,3,2,1,2,1]
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= barcodes.length <= 10000
 * 1 <= barcodes[i] <= 10000
 *
 *
 */
package leetcode

import "sort"
type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}
// @lc code=start
func rearrangeBarcodes(barcodes []int) []int {
	cnt := map[int]int{}
	for _, x := range barcodes{
		cnt[x] ++
	}
	sort.Slice(barcodes, func(i, j int) bool {return cnt[barcodes[i]] > cnt[barcodes[j]] || cnt[barcodes[i]] == cnt[barcodes[j]] && barcodes[i] < barcodes[j]})
	res := make([]int, len(barcodes))
	j := 0
	for i := 0 ; i < len(barcodes) ; i += 2{
		res[i] = barcodes[j]
		j ++
	}
	for i := 1 ; i < len(barcodes) ; i += 2{
		res[i] = barcodes[j]
		j ++
	} 
	return res 
}
// @lc code=end



/*
// @lcpr case=start
// [1,2,1]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1,2,2,2]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1,1,2,2,3,3]\n
// @lcpr case=end

 */

