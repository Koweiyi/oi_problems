/*
 * @lc app=leetcode.cn id=剑指 Offer 22 lang=golang
 * @lcpr version=21913
 *
 * [剑指 Offer 22] 链表中倒数第k个节点
 *
 * https://leetcode.cn/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/description/
 *
 * LCOF
 * Easy (80.08%)
 * Likes:    489
 * Dislikes: 0
 * Total Accepted:    480.1K
 * Total Submissions: 599.5K
 * Testcase Example:  '[1,2,3,4,5]\n2'
 *
 * 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
 * 
 * 例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。
 * 
 * 
 * 
 * 示例：
 * 
 * 给定一个链表: 1->2->3->4->5, 和 k = 2.
 * 
 * 返回链表 4->5.
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
func getKthFromEnd(head *ListNode, k int) *ListNode {
	// 快慢指针 快指针先走k步 然后和slow一起走
	// fast 为空时, slow 刚好到达倒数第k节点 
	fast := head
	for i := 0 ; i < k ; i ++{
		fast = fast.Next
	}
	slow := head
	for fast != nil{
		slow = slow.Next
		fast = fast.Next
	}
	return slow
}
// @lc code=end



