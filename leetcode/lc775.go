/*
 * @lc app=leetcode.cn id=775 lang=golang
 * @lcpr version=21912
 *
 * [775] 全局倒置与局部倒置
 *
 * https://leetcode.cn/problems/global-and-local-inversions/description/
 *
 * algorithms
 * Medium (49.45%)
 * Likes:    201
 * Dislikes: 0
 * Total Accepted:    33K
 * Total Submissions: 66.8K
 * Testcase Example:  '[1,0,2]'
 *
 * 给你一个长度为 n 的整数数组 nums ，表示由范围 [0, n - 1] 内所有整数组成的一个排列。
 *
 * 全局倒置 的数目等于满足下述条件不同下标对 (i, j) 的数目：
 *
 *
 * 0 <= i < j < n
 * nums[i] > nums[j]
 *
 *
 * 局部倒置 的数目等于满足下述条件的下标 i 的数目：
 *
 *
 * 0 <= i < n - 1
 * nums[i] > nums[i + 1]
 *
 *
 * 当数组 nums 中 全局倒置 的数量等于 局部倒置 的数量时，返回 true ；否则，返回 false 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [1,0,2]
 * 输出：true
 * 解释：有 1 个全局倒置，和 1 个局部倒置。
 *
 *
 * 示例 2：
 *
 * 输入：nums = [1,2,0]
 * 输出：false
 * 解释：有 2 个全局倒置，和 1 个局部倒置。
 *
 *
 *
 * 提示：
 *
 *
 * n == nums.length
 * 1 <= n <= 10^5
 * 0 <= nums[i] < n
 * nums 中的所有整数 互不相同
 * nums 是范围 [0, n - 1] 内所有数字组成的一个排列
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
func mergeAndCount(arr []int, l int, m int, r int) int {
	tmp := make([]int, r - l + 1)
	i, j, k, cnt := l, m + 1, 0, 0
	for i <= m && j <= r {
		if arr[i] <= arr[j] {
			tmp[k] = arr[i]
			k ++ 
			i ++
		}else{
			tmp[k] = arr[j]
			k ++
			j ++
			cnt += m - i + 1
		}
	}
	for i <= m {
		tmp[k] = arr[i]
		k ++
		i ++
	}
	for j <= r {
		tmp[k] = arr[j]
		k ++
		j ++
	}
	for p := l ; p <= r ; p ++ {
		arr[p] = tmp[p - l]
	}
	return cnt
}

func mergeSortAndCount(arr []int, l int, r int) int {
	inversions := 0
	if l < r {
		m := l + (r-l)/2
		inversions += mergeSortAndCount(arr, l, m)
		inversions += mergeSortAndCount(arr, m+1, r)
		inversions += mergeAndCount(arr, l, m, r)
	}
	return inversions
}

func countInversions(arr []int) int {
	return mergeSortAndCount(arr, 0, len(arr)-1)
}

func isIdealPermutation(nums []int) bool {
	tmp := make([]int, len(nums))
	copy(tmp, nums)
	tot := countInversions(tmp)

	cnt := 0 
	for i := 0 ; i < len(nums) - 1 ; i ++ {
		if nums[i] > nums[i + 1] {
			cnt ++
		}
	}
	return cnt == tot
}

func abs(x int) int{
	if x > 0{
		return x 
	}
	return -x 
}

// @lc code=end



/*
// @lcpr case=start
// [1,0,2]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,0]\n
// @lcpr case=end
// @lcpr case=start
// [0,2,1]\n
// @lcpr case=end

 */

