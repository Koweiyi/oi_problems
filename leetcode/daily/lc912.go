/*
 * @lc app=leetcode.cn id=912 lang=golang
 * @lcpr version=21913
 *
 * [912] 排序数组
 *
 * https://leetcode.cn/problems/sort-an-array/description/
 *
 * algorithms
 * Medium (51.16%)
 * Likes:    891
 * Dislikes: 0
 * Total Accepted:    563K
 * Total Submissions: 1.1M
 * Testcase Example:  '[5,2,3,1]'
 *
 * 给你一个整数数组 nums，请你将该数组升序排列。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [5,2,3,1]
 * 输出：[1,2,3,5]
 *
 *
 * 示例 2：
 *
 * 输入：nums = [5,1,1,2,0,0]
 * 输出：[0,0,1,1,2,5]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 5 * 10^4
 * -5 * 10^4 <= nums[i] <= 5 * 10^4
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
type ListNode struct {
    Val int
    Next *ListNode
}
// @lc code=start

var cnt int
func sortArray(nums []int) []int {
	QuickSort(nums, 0, len(nums) - 1)
	return nums 
}
func QuickSort(nums []int, l, r int) {
	if l >= r{
		return 
	}
	p := partition(nums, l, r)
	QuickSort(nums, l, p - 1)
	QuickSort(nums, p + 1, r)
}

func partition(nums []int, l, r int) int {
	i := l 
	for j := l ; j < r ; j ++ {
		cnt ++
		if nums[j] < nums[r]{
			if i != j{
				nums[i], nums[j] = nums[j], nums[i]
			}
			i ++
		}
	}
	nums[i], nums[r] = nums[r], nums[i]
	return i 
}

func main(){
	nums := []int{14,6,18,43,22,50}
	sortArray(nums)
	fmt.Println(cnt)
}
// @lc code=end



/*
// @lcpr case=start
// [5,2,3,1]\n
// @lcpr case=end

// @lcpr case=start
// [5,1,1,2,0,0]\n
// @lcpr case=end

 */

