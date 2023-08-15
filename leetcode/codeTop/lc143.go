/*
 * @lc app=leetcode.cn id=143 lang=golang
 * @lcpr version=21913
 *
 * [143] 重排链表
 *
 * https://leetcode.cn/problems/reorder-list/description/
 *
 * algorithms
 * Medium (65.69%)
 * Likes:    1346
 * Dislikes: 0
 * Total Accepted:    279.9K
 * Total Submissions: 426K
 * Testcase Example:  '[1,2,3,4]'
 *
 * 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
 *
 * L0 → L1 → … → Ln - 1 → Ln
 *
 *
 * 请将其重新排列后变为：
 *
 * L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
 *
 * 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：head = [1,2,3,4]
 * 输出：[1,4,2,3]
 *
 * 示例 2：
 *
 *
 *
 * 输入：head = [1,2,3,4,5]
 * 输出：[1,5,2,4,3]
 *
 *
 *
 * 提示：
 *
 *
 * 链表的长度范围为 [1, 5 * 10^4]
 * 1 <= node.val <= 1000
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
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func midNode (head *ListNode) *ListNode{
	fast, slow := head, head
	for fast != nil && fast.Next != nil{
		fast = fast.Next.Next
		slow = slow.Next
	}
	return slow
}

func reverseList(head *ListNode) *ListNode{
	var pre *ListNode
	cur := head
	for cur != nil{
		nxt := cur.Next
		cur.Next = pre 
		pre = cur
		cur = nxt
	}
	return pre 
}

func reorderList(head *ListNode)  {
	mid := midNode(head)
	nxt := 	reverseList(mid.Next)
	mid.Next = nil
	cur := head
	for nxt != nil{
		tmp := cur.Next
		cur.Next = nxt 
		nxt = nxt.Next
		cur.Next.Next = tmp 
		cur = cur.Next.Next
	} 
	return 
}
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,4]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5]\n
// @lcpr case=end

 */

