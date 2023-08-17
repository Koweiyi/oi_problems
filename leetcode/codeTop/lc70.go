/*
 * @lc app=leetcode.cn id=70 lang=golang
 * @lcpr version=21913
 *
 * [70] 爬楼梯
 *
 * https://leetcode.cn/problems/climbing-stairs/description/
 *
 * algorithms
 * Easy (54.09%)
 * Likes:    3181
 * Dislikes: 0
 * Total Accepted:    1.2M
 * Total Submissions: 2.2M
 * Testcase Example:  '2'
 *
 * 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
 *
 * 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
 *
 *
 *
 * 示例 1：
 *
 * 输入：n = 2
 * 输出：2
 * 解释：有两种方法可以爬到楼顶。
 * 1. 1 阶 + 1 阶
 * 2. 2 阶
 *
 * 示例 2：
 *
 * 输入：n = 3
 * 输出：3
 * 解释：有三种方法可以爬到楼顶。
 * 1. 1 阶 + 1 阶 + 1 阶
 * 2. 1 阶 + 2 阶
 * 3. 2 阶 + 1 阶
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 45
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

var dp []int = make([]int, 50)


func climbStairs(n int) int {
	// 递归写法
	// memo := make([]int, 50)
	// for i := range memo{
	// 	memo[i] = -1
	// }
	// var dfs func(i int) (res int) 
	// dfs = func(i int) (res int){
	// 	// i == 1 return 1
	// 	// i == 2 return 2
	// 	if i <= 2 {
	// 		return i 
	// 	}
	// 	if memo[i] != -1{
	// 		return memo[i]
	// 	}
	// 	defer func ()  {
	// 		memo[i] = res 	
	// 	}() // 退出函数前将res 赋值给 memo[i] 
	// 	res =  dfs(i - 1) + dfs(i - 2)
	// 	return 
	// }
	// return dfs(n)
	
	
	//dp 递推
	dp := [50]int{}
	dp[1], dp[2] = 1, 2
	for i := 3 ; i <= n ; i ++ {
		dp[i] = dp[i - 1] + dp[i - 2]
	}
	return dp[n]

}
// @lc code=end



/*
// @lcpr case=start
// 2\n
// @lcpr case=end

// @lcpr case=start
// 3\n
// @lcpr case=end

 */

