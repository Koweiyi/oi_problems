/*
 * @lc app=leetcode.cn id=148 lang=golang
 * @lcpr version=21913
 *
 * [148] 排序链表
 *
 * https://leetcode.cn/problems/sort-list/description/
 *
 * algorithms
 * Medium (65.67%)
 * Likes:    2077
 * Dislikes: 0
 * Total Accepted:    421.4K
 * Total Submissions: 641.8K
 * Testcase Example:  '[4,2,1,3]'
 *
 * 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：head = [4,2,1,3]
 * 输出：[1,2,3,4]
 *
 *
 * 示例 2：
 *
 * 输入：head = [-1,5,3,4,0]
 * 输出：[-1,0,3,4,5]
 *
 *
 * 示例 3：
 *
 * 输入：head = []
 * 输出：[]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 链表中节点的数目在范围 [0, 5 * 10^4] 内
 * -10^5 <= Node.val <= 10^5
 *
 *
 *
 *
 * 进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
 *
 */
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

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func megeList(h1, h2 *ListNode) *ListNode {
	dummy := &ListNode{}
	cur := dummy
	for h1 != nil && h2 != nil {
		if h1.Val < h2.Val {
			cur.Next = h1
			h1 = h1.Next
			cur = cur.Next
		} else {
			cur.Next = h2
			h2 = h2.Next
			cur = cur.Next
		}
	}
	if h1 != nil {
		cur.Next = h1
	} else {
		cur.Next = h2
	}
	return dummy.Next
}

func sortList(head *ListNode) *ListNode {

	// 分治
	// 先找到mid 中间节点
	// 链表归并排序O(nlogn) accepted
	if head == nil || head.Next == nil {
		return head
	}

	fast, slow := head.Next, head
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
	}
	h1 := head
	h2 := slow.Next //中点下一个节点
	slow.Next = nil
	h1 = sortList(h1)
	h2 = sortList(h2)
	return megeList(h1, h2)

	// O(n ^ 2) 解法 tle
	// cur := head
	// n := 0
	// for cur!= nil{
	// 	n ++
	// 	cur = cur.Next
	// }
	// cur = head
	// for ; n > 0 ; n --{
	// 	pre, nxt := cur, cur.Next
	// 	for nxt != nil{
	// 		if pre.Val > nxt.Val {
	// 			pre.Val, nxt.Val = nxt.Val, pre.Val
	// 		}
	// 		pre = nxt
	// 		nxt = nxt.Next
	// 	}
	// }
	// return head


}

// @lc code=end

/*
// @lcpr case=start
// [4,2,1,3]\n
// @lcpr case=end

// @lcpr case=start
// [-1,5,3,4,0]\n
// @lcpr case=end

// @lcpr case=start
// []\n
// @lcpr case=end

*/
