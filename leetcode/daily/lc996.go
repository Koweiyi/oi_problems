/*
 * @lc app=leetcode.cn id=996 lang=golang
 * @lcpr version=21913
 *
 * [996] 正方形数组的数目
 *
 * https://leetcode.cn/problems/number-of-squareful-arrays/description/
 *
 * algorithms
 * Hard (50.62%)
 * Likes:    112
 * Dislikes: 0
 * Total Accepted:    7.3K
 * Total Submissions: 14.4K
 * Testcase Example:  '[1,17,8]'
 *
 * 给定一个非负整数数组 A，如果该数组每对相邻元素之和是一个完全平方数，则称这一数组为正方形数组。
 *
 * 返回 A 的正方形排列的数目。两个排列 A1 和 A2 不同的充要条件是存在某个索引 i，使得 A1[i] != A2[i]。
 *
 *
 *
 * 示例 1：
 *
 * 输入：[1,17,8]
 * 输出：2
 * 解释：
 * [1,8,17] 和 [17,8,1] 都是有效的排列。
 *
 *
 * 示例 2：
 *
 * 输入：[2,2,2]
 * 输出：1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= A.length <= 12
 * 0 <= A[i] <= 1e9
 *
 *
 */
package leetcode

import (
	"math"
	"sort"
)
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
func numSquarefulPerms(nums []int) int {
	sort.Ints(nums)
	n := len(nums)
	g := make([][]bool, n)
	for i := range g{
		g[i] = make([]bool, n)
	} 
	
	check := func (x, y int) bool {
		i := int(math.Sqrt(float64(x + y)))
		return i * i == x + y 
		// s := x + y 
		// l,r := -1, s + 1
		// for l + 1 < r{
		// 	mid := l + (r - l) / 2 
		// 	mid = mid * mid
		// 	if mid == s{
		// 		return true
		// 	}else if mid > s{
		// 		l = mid
		// 	}else{
		// 		r = mid
		// 	}
		// }
		// return false
	}
	mp := map[[12]int]int{}
	vis := make([]bool, n)
	var dfs func(i int)
	path := [12]int{}
	for i:= range path{
		path[i] = -1
	}
	dfs = func(i int) {
		if i == n{
			// 搜索到一个答案
			mp[path] += 1
			return 
		}
		pre := -1
		for j := 0 ; j < n ; j ++ {
			if !vis[j] && check(path[i - 1], nums[j]){
				if nums[j] == pre {continue}
				pre = nums[j]
				path[i] = nums[j]
				vis[j] = true
				dfs(i + 1)
				vis[j] = false
			}
		}
	}
	pre := -1 
	for i := 0 ; i < n ; i ++ {
		if nums[i] == pre {continue}
		pre = nums[i]
		vis[i] = true
		path[0] = nums[i]
		dfs(1)
		vis[i] = false
	}
	return len(mp)
}
// @lc code=end



/*
// @lcpr case=start
// [1,17,8]\n
// @lcpr case=end

// @lcpr case=start
// [2,2,2]\n
// @lcpr case=end

 */

