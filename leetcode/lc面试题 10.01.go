/*
 * @lc app=leetcode.cn id=面试题 10.01 lang=golang
 * @lcpr version=21912
 *
 * [面试题 10.01] 合并排序的数组
 *
 * https://leetcode.cn/problems/sorted-merge-lcci/description/
 *
 * LCCI
 * Easy (56.13%)
 * Likes:    169
 * Dislikes: 0
 * Total Accepted:    77.6K
 * Total Submissions: 138.3K
 * Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
 *
 * 给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
 * 
 * 初始化 A 和 B 的元素数量分别为 m 和 n。
 * 
 * 示例:
 * 
 * 输入:
 * A = [1,2,3,0,0,0], m = 3
 * B = [2,5,6],       n = 3
 * 
 * 输出: [1,2,2,3,5,6]
 * 
 * 说明:
 * 
 * 
 * A.length == n + m
 * 
 * 
 */
package leetcode
// @lc code=start
func merge(A []int, m int, B []int, n int)  {
	j := len(A) - 1
	m -- 
	n --
	for m >= 0 && n >= 0{
		if A[m] >= B[n]{
			A[j] = A[m]
			m -- 
		}else{
			A[j] = B[n]
			n -- 
		}
		j --
	}
	for n >= 0{
		A[j] = B[n]
		j --
		n --
	}
	
}
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,0,0,0]\n3\n[2,5,6]\n3
// @lcpr case=end

 */

