/*
 * @lc app=leetcode.cn id=895 lang=golang
 * @lcpr version=30109
 *
 * [895] 最大频率栈
 *
 * https://leetcode.cn/problems/maximum-frequency-stack/description/
 *
 * algorithms
 * Hard (64.14%)
 * Likes:    383
 * Dislikes: 0
 * Total Accepted:    32.4K
 * Total Submissions: 50.5K
 * Testcase Example:  '["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]\n' +
  '[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]'
 *
 * 设计一个类似堆栈的数据结构，将元素推入堆栈，并从堆栈中弹出出现频率最高的元素。
 *
 * 实现 FreqStack 类:
 *
 *
 * FreqStack() 构造一个空的堆栈。
 * void push(int val) 将一个整数 val 压入栈顶。
 * int pop() 删除并返回堆栈中出现频率最高的元素。
 *
 * 如果出现频率最高的元素不只一个，则移除并返回最接近栈顶的元素。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：
 *
 * ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
 * [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
 * 输出：[null,null,null,null,null,null,null,5,7,5,4]
 * 解释：
 * FreqStack = new FreqStack();
 * freqStack.push (5);//堆栈为 [5]
 * freqStack.push (7);//堆栈是 [5,7]
 * freqStack.push (5);//堆栈是 [5,7,5]
 * freqStack.push (7);//堆栈是 [5,7,5,7]
 * freqStack.push (4);//堆栈是 [5,7,5,7,4]
 * freqStack.push (5);//堆栈是 [5,7,5,7,4,5]
 * freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,5,7,4]。
 * freqStack.pop ();//返回 7 ，因为 5 和 7 出现频率最高，但7最接近顶部。堆栈变成 [5,7,5,4]。
 * freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,4]。
 * freqStack.pop ();//返回 4 ，因为 4, 5 和 7 出现频率最高，但 4 是最接近顶部的。堆栈变成 [5,7]。
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= val <= 10^9
 * push 和 pop 的操作数不大于 2 * 10^4。
 * 输入保证在调用 pop 之前堆栈中至少有一个元素。
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
type FreqStack struct {
    f map[int]int
    st [][]int
}

func Constructor() FreqStack {
    return FreqStack{f: map[int]int{}}
}

func (this *FreqStack) Push(val int) {
    c := this.f[val]
    if c == len(this.st) {
        this.st = append(this.st, []int{val})
    }else{
        this.st[c] = append(this.st[c], val)
    }
    this.f[val] ++ 
}

func (this *FreqStack) Pop() int {
    n := len(this.st) - 1 
    st := this.st[n]
    val := st[len(st) - 1] 
    if len(st) == 1 {
        this.st = this.st[:n]
    }else{
        this.st[n] = st[:len(st) - 1]
    }
    this.f[val] --
    return val
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * param_2 := obj.Pop();
 */
// @lc code=end

/*
// @lcpr case=start
// ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]\n[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]\n
// @lcpr case=end

*/
