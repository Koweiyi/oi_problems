/*
 * @lc app=leetcode.cn id=2708 lang=golang
 * @lcpr version=30109
 *
 * [2708] 一个小组的最大实力值
 *
 * https://leetcode.cn/problems/maximum-strength-of-a-group/description/
 *
 * algorithms
 * Medium (30.40%)
 * Likes:    13
 * Dislikes: 0
 * Total Accepted:    4.5K
 * Total Submissions: 14.8K
 * Testcase Example:  '[3,-1,-5,2,5,-9]'
 *
 * 给你一个下标从 0 开始的整数数组 nums ，它表示一个班级中所有学生在一次考试中的成绩。老师想选出一部分同学组成一个 非空 小组，且这个小组的
 * 实力值 最大，如果这个小组里的学生下标为 i0, i1, i2, ... , ik ，那么这个小组的实力值定义为 nums[i0] * nums[i1]
 * * nums[i2] * ... * nums[ik​] 。
 *
 * 请你返回老师创建的小组能得到的最大实力值为多少。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [3,-1,-5,2,5,-9]
 * 输出：1350
 * 解释：一种构成最大实力值小组的方案是选择下标为 [0,2,3,4,5] 的学生。实力值为 3 * (-5) * 2 * 5 * (-9) = 1350
 * ，这是可以得到的最大实力值。
 *
 *
 * 示例 2：
 *
 * 输入：nums = [-4,-5,-4]
 * 输出：20
 * 解释：选择下标为 [0, 1] 的学生。得到的实力值为 20 。我们没法得到更大的实力值。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 13
 * -9 <= nums[i] <= 9
 *
 *
 */

// @lcpr-template-start
package leetcode

import (
	"slices"
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

// @lcpr-template-end
// @lc code=start
func maxStrength(nums []int) int64 {

	var res int64 = 1
	negs := []int{}
	pos := []int{}
	hasZero := false
	for _,x := range nums{
		if x > 0{
			res *= int64(x)
			pos = append(pos, x)
		}else if x == 0{
			hasZero = true
		}else {
			negs = append(negs, x)
		}
	}

	if len(pos) == 0{
		if len(negs) == 0{
			if hasZero{
				return 0
			}
		}
		if len(negs) == 1{
			if hasZero{
				return 0 
			}else{
				return int64(negs[0])
			}
		}
	}

	slices.Sort(negs)
	for i := 0 ; i + 1 < len(negs) ; i += 2{
		res *= int64(negs[i]) * int64(negs[i + 1])
	}
	return res 
}	

func abs(x int) int {
	if x < 0{
		return -x
	}
	return x 
}
// @lc code=end

/*
// @lcpr case=start
// [3,-1,-5,2,5,-9]\n
// @lcpr case=end

// @lcpr case=start
// [-4,-5,-4]\n
// @lcpr case=end

// @lcpr case=start
// [8,6,0,5,-4,-8,-4,9,-1,6,-4,8,-5]\n
// @lcpr case=end
*/
