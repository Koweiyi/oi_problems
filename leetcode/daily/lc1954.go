/*
 * @lc app=leetcode.cn id=1954 lang=golang
 * @lcpr version=21913
 *
 * [1954] 收集足够苹果的最小花园周长
 *
 * https://leetcode.cn/problems/minimum-garden-perimeter-to-collect-enough-apples/description/
 *
 * algorithms
 * Medium (50.02%)
 * Likes:    23
 * Dislikes: 0
 * Total Accepted:    6.3K
 * Total Submissions: 12.6K
 * Testcase Example:  '1'
 *
 * 给你一个用无限二维网格表示的花园，每一个 整数坐标处都有一棵苹果树。整数坐标 (i, j) 处的苹果树有 |i| + |j| 个苹果。
 * 
 * 你将会买下正中心坐标是 (0, 0) 的一块 正方形土地 ，且每条边都与两条坐标轴之一平行。
 * 
 * 给你一个整数 neededApples ，请你返回土地的 最小周长 ，使得 至少 有 neededApples 个苹果在土地 里面或者边缘上。
 * 
 * |x| 的值定义为：
 * 
 * 
 * 如果 x >= 0 ，那么值为 x
 * 如果 x < 0 ，那么值为 -x
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：neededApples = 1
 * 输出：8
 * 解释：边长长度为 1 的正方形不包含任何苹果。
 * 但是边长为 2 的正方形包含 12 个苹果（如上图所示）。
 * 周长为 2 * 4 = 8 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：neededApples = 13
 * 输出：16
 * 
 * 
 * 示例 3：
 * 
 * 输入：neededApples = 1000000000
 * 输出：5040
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= neededApples <= 10^15
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
func minimumPerimeter(neededApples int64) int64 {
	l, r := 0, 100005 

	check := func (x int) bool {
		var i int64 = int64(x) 
		return 2 * i * (i + 1) * (2 * i + 1) >= neededApples
	}
	for l + 1 < r{
		mid := l + (r - l) / 2
		if check(mid) {
			r = mid 
		}else{
			l = mid
		}
	}
	return int64(8 * r) 
}
// @lc code=end



/*
// @lcpr case=start
// 1\n
// @lcpr case=end

// @lcpr case=start
// 13\n
// @lcpr case=end

// @lcpr case=start
// 1000000000\n
// @lcpr case=end

 */

