/*
 * @lc app=leetcode.cn id=1090 lang=golang
 * @lcpr version=21912
 *
 * [1090] 受标签影响的最大值
 *
 * https://leetcode.cn/problems/largest-values-from-labels/description/
 *
 * algorithms
 * Medium (66.86%)
 * Likes:    87
 * Dislikes: 0
 * Total Accepted:    22.1K
 * Total Submissions: 33.1K
 * Testcase Example:  '[5,4,3,2,1]\n[1,1,2,2,3]\n3\n1'
 *
 * 我们有一个 n 项的集合。给出两个整数数组 values 和 labels ，第 i 个元素的值和标签分别是 values[i] 和
 * labels[i]。还会给出两个整数 numWanted 和 useLimit 。
 *
 * 从 n 个元素中选择一个子集 s :
 *
 *
 * 子集 s 的大小 小于或等于 numWanted 。
 * s 中 最多 有相同标签的 useLimit 项。
 *
 *
 * 一个子集的 分数 是该子集的值之和。
 *
 * 返回子集 s 的最大 分数 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1
 * 输出：9
 * 解释：选出的子集是第一项，第三项和第五项。
 *
 *
 * 示例 2：
 *
 * 输入：values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2
 * 输出：12
 * 解释：选出的子集是第一项，第二项和第三项。
 *
 *
 * 示例 3：
 *
 * 输入：values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1
 * 输出：16
 * 解释：选出的子集是第一项和第四项。
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == values.length == labels.length
 * 1 <= n <= 2 * 10^4
 * 0 <= values[i], labels[i] <= 2 * 10^4
 * 1 <= numWanted, useLimit <= n
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
func largestValsFromLabels(values []int, labels []int, numWanted int, useLimit int) int {
	type data struct{
		v, l int 
	}
	d := []data{}
	for i, x := range values{
		d = append(d, data{x, labels[i]})
	}
	sort.Slice(d, func(i, j int) bool {return d[i].v > d[j].v})

	res := 0
	cnt := map[int]int{}
	for _, x := range d{
		if numWanted <= 0{
			break
		}
		if cnt[x.l] < useLimit{
			res += x.v
			cnt[x.l] ++
			numWanted --
		}
	}
	return res 
}
// @lc code=end



/*
// @lcpr case=start
// [5,4,3,2,1]\n[1,1,2,2,3]\n3\n1\n
// @lcpr case=end

// @lcpr case=start
// [5,4,3,2,1]\n[1,3,3,3,2]\n3\n2\n
// @lcpr case=end

// @lcpr case=start
// [9,8,8,7,6]\n[0,0,0,1,1]\n3\n1\n
// @lcpr case=end

 */

