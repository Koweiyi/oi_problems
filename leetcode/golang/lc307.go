/*
 * @lc app=leetcode.cn id=307 lang=golang
 * @lcpr version=30109
 *
 * [307] 区域和检索 - 数组可修改
 *
 * https://leetcode.cn/problems/range-sum-query-mutable/description/
 *
 * algorithms
 * Medium (52.89%)
 * Likes:    667
 * Dislikes: 0
 * Total Accepted:    79.2K
 * Total Submissions: 149.7K
 * Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
 *
 * 给你一个数组 nums ，请你完成两类查询。
 *
 *
 * 其中一类查询要求 更新 数组 nums 下标对应的值
 * 另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
 *
 *
 * 实现 NumArray 类：
 *
 *
 * NumArray(int[] nums) 用整数数组 nums 初始化对象
 * void update(int index, int val) 将 nums[index] 的值 更新 为 val
 * int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含
 * ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]）
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：
 * ["NumArray", "sumRange", "update", "sumRange"]
 * [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
 * 输出：
 * [null, 9, null, 8]
 *
 * 解释：
 * NumArray numArray = new NumArray([1, 3, 5]);
 * numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
 * numArray.update(1, 2);   // nums = [1,2,5]
 * numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 3 * 10^4
 * -100 <= nums[i] <= 100
 * 0 <= index < nums.length
 * -100 <= val <= 100
 * 0 <= left <= right < nums.length
 * 调用 update 和 sumRange 方法次数不大于 3 * 10^4
 *
 *
 */

// @lcpr-template-start
package leetcode

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
type NumArray []int


func Constructor(nums []int) NumArray {
	na := NumArray(make([]int, len(nums) + 1))
	for i := 0 ; i < len(nums) ; i ++ {
		na.Update(i, nums[i])
	}
	return na 
}

func (this *NumArray) Update(index int, val int) {
	add := val - this.SumRange(index, index)

	for i := index + 1 ; i < len(*this) ; i += i & -i {
		(*this)[i] += add 
	}

}

func (nums NumArray) pre(index int) (res int){
	for i := index; i > 0 ; i -= i & -i{
		res += nums[i]
	}
	return 
}

func (this *NumArray) SumRange(left int, right int) int {
	return this.pre(right + 1) - this.pre(left)
}

/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * obj.Update(index,val);
 * param_2 := obj.SumRange(left,right);
 */
// @lc code=end

/*
// @lcpr case=start
// ["NumArray", "sumRange", "update", "sumRange"]\n[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]\n
// @lcpr case=end

*/
