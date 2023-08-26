/*
 * @lc app=leetcode.cn id=1146 lang=golang
 * @lcpr version=21913
 *
 * [1146] 快照数组
 *
 * https://leetcode.cn/problems/snapshot-array/description/
 *
 * algorithms
 * Medium (33.74%)
 * Likes:    112
 * Dislikes: 0
 * Total Accepted:    9.8K
 * Total Submissions: 29K
 * Testcase Example:  '["SnapshotArray","set","snap","set","get"]\n[[3],[0,5],[],[0,6],[0,0]]'
 *
 * 实现支持下列接口的「快照数组」- SnapshotArray：
 * 
 * 
 * SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。
 * void set(index, val) - 会将指定索引 index 处的元素设置为 val。
 * int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。
 * int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。
 * 
 * 
 * 
 * 
 * 示例：
 * 
 * 输入：["SnapshotArray","set","snap","set","get"]
 * ⁠    [[3],[0,5],[],[0,6],[0,0]]
 * 输出：[null,null,0,null,5]
 * 解释：
 * SnapshotArray snapshotArr = new SnapshotArray(3); // 初始化一个长度为 3 的快照数组
 * snapshotArr.set(0,5);  // 令 array[0] = 5
 * snapshotArr.snap();  // 获取快照，返回 snap_id = 0
 * snapshotArr.set(0,6);
 * snapshotArr.get(0,0);  // 获取 snap_id = 0 的快照中 array[0] 的值，返回 5
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= length <= 50000
 * 题目最多进行50000 次set，snap，和 get的调用 。
 * 0 <= index < length
 * 0 <= snap_id < 我们调用 snap() 的总次数
 * 0 <= val <= 10^9
 * 
 * 
 */
package leetcode
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

type pair struct{val, id int} 
type SnapshotArray struct {
	data [][]pair
	snap_id int
}


func Constructor(length int) SnapshotArray {
	d := make([][]pair, length)
	for i := range d {
		d[i] = append(d[i], pair{0, 0})
	}
	return SnapshotArray{data: d, snap_id: 0}
}


func (this *SnapshotArray) Set(index int, val int)  {
	if this.data[index][len(this.data[index]) - 1].id == this.snap_id{
		this.data[index][len(this.data[index]) - 1].val = val 
	}
	this.data[index] = append(this.data[index], pair{val, this.snap_id})
}


func (this *SnapshotArray) Snap() int {
	res := this.snap_id
	this.snap_id ++ 
	return res 
}


func (this *SnapshotArray) Get(index int, snap_id int) int {
	v := this.data[index]
	l, r := -1, len(v) 
	for l + 1 < r {
		mid := l + (r - l) / 2 
		if v[mid].id <= snap_id{
			l = mid
		}else{
			r = mid
		}
	}
	return v[l].val
}	


/**
 * Your SnapshotArray object will be instantiated and called as such:
 * obj := Constructor(length);
 * obj.Set(index,val);
 * param_2 := obj.Snap();
 * param_3 := obj.Get(index,snap_id);
 */
// @lc code=end



/*
// @lcpr case=start
// ["SnapshotArray","set","snap","set","get"]\n[[3],[0,5],[],[0,6],[0,0]]\n
// @lcpr case=end

 */

