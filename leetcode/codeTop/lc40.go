/*
 * @lc app=leetcode.cn id=40 lang=golang
 * @lcpr version=21913
 *
 * [40] 组合总和 II
 *
 * https://leetcode.cn/problems/combination-sum-ii/description/
 *
 * algorithms
 * Medium (59.63%)
 * Likes:    1426
 * Dislikes: 0
 * Total Accepted:    455.9K
 * Total Submissions: 764.6K
 * Testcase Example:  '[10,1,2,7,6,1,5]\n8'
 *
 * 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
 *
 * candidates 中的每个数字在每个组合中只能使用 一次 。
 *
 * 注意：解集不能包含重复的组合。
 *
 *
 *
 * 示例 1:
 *
 * 输入: candidates = [10,1,2,7,6,1,5], target = 8,
 * 输出:
 * [
 * [1,1,6],
 * [1,2,5],
 * [1,7],
 * [2,6]
 * ]
 *
 * 示例 2:
 *
 * 输入: candidates = [2,5,2,1,2], target = 5,
 * 输出:
 * [
 * [1,2,2],
 * [5]
 * ]
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= candidates.length <= 100
 * 1 <= candidates[i] <= 50
 * 1 <= target <= 30
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

func combinationSum2(candidates []int, target int) (res [][]int) {
    
    path := []int{}
    var dfs func(i, left int) 
    dfs = func(i, left int) {
        if left == 0{
            res = append(res, append([]int{}, path...))
            return 
        }
        if i == len(candidates){
            return 
        }
        // 去重来考虑选哪个 而不是选或者不选
        for j := i ; j < len(candidates) ; j ++ {
            if j > i && candidates[j] == candidates[j - 1] {continue}
            if left >= candidates[j]{
                path = append(path, candidates[j])
                dfs(j + 1, left - candidates[j])
                path = path[:len(path) - 1]
            }
        }
        return 
    }
    dfs(0, target)
    return res 
}


// @lc code=end



/*
// @lcpr case=start
// [10,1,2,7,6,1,5]\n8,\n
// @lcpr case=end

// @lcpr case=start
// [2,5,2,1,2]\n5,\n
// @lcpr case=end

 */

