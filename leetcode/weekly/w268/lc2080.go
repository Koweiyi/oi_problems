/*
* @lc app=leetcode.cn id=2080 lang=golang
* @lcpr version=21913
*
* [2080] 区间内查询数字的频率
*
* https://leetcode.cn/problems/range-frequency-queries/description/
*
  - algorithms
  - Medium (31.54%)
  - Likes:    52
  - Dislikes: 0
  - Total Accepted:    8.8K
  - Total Submissions: 28K
  - Testcase Example:  '["RangeFreqQuery","query","query"]\n' +
    '[[[12,33,4,56,22,2,34,33,22,12,34,56]],[1,2,4],[0,11,33]]'

*
* 请你设计一个数据结构，它能求出给定子数组内一个给定值的 频率 。
*
* 子数组中一个值的 频率 指的是这个子数组中这个值的出现次数。
*
* 请你实现 RangeFreqQuery 类：
*
*
* RangeFreqQuery(int[] arr) 用下标从 0 开始的整数数组 arr 构造一个类的实例。
* int query(int left, int right, int value) 返回子数组 arr[left...right] 中 value 的
* 频率 。
*
*
* 一个 子数组 指的是数组中一段连续的元素。arr[left...right] 指的是 nums 中包含下标 left 和 right 在内
* 的中间一段连续元素。
*
*
*
* 示例 1：
*
* 输入：
* ["RangeFreqQuery", "query", "query"]
* [[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
* 输出：
* [null, 1, 2]
*
* 解释：
* RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2,
* 34, 33, 22, 12, 34, 56]);
* rangeFreqQuery.query(1, 2, 4); // 返回 1 。4 在子数组 [33, 4] 中出现 1 次。
* rangeFreqQuery.query(0, 11, 33); // 返回 2 。33 在整个子数组中出现 2 次。
*
*
*
*
* 提示：
*
*
* 1 <= arr.length <= 10^5
* 1 <= arr[i], value <= 10^4
* 0 <= left <= right < arr.length
* 调用 query 不超过 10^5 次。
*
*
*/
package leetcode

import (
	"sort"
)
type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}
// @lc code=start
type RangeFreqQuery struct {
    pos [1e4 + 1]sort.IntSlice
}

func Constructor(arr []int)(q RangeFreqQuery){
    for i, val := range arr{
        q.pos[val] = append(q.pos[val], i)   
    }
    return 
}

func (q *RangeFreqQuery) Query(left int, right int, value int) int {
    p := q.pos[value]
    return p[p.Search(left):].Search(right + 1)   
}
/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * obj := Constructor(arr);
 * param_1 := obj.Query(left,right,value);
 */
// @lc code=end



/*
// @lcpr case=start
// ["RangeFreqQuery", "query", "query"][[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]\n
// @lcpr case=end

 */

