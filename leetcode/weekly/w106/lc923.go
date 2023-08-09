/*
 * @lc app=leetcode.cn id=923 lang=golang
 * @lcpr version=21913
 *
 * [923] 三数之和的多种可能
 *
 * https://leetcode.cn/problems/3sum-with-multiplicity/description/
 *
 * algorithms
 * Medium (37.04%)
 * Likes:    123
 * Dislikes: 0
 * Total Accepted:    10.2K
 * Total Submissions: 27.5K
 * Testcase Example:  '[1,1,2,2,3,3,4,4,5,5]\n8'
 *
 * 给定一个整数数组 arr ，以及一个整数 target 作为目标值，返回满足 i < j < k 且 arr[i] + arr[j] + arr[k]
 * == target 的元组 i, j, k 的数量。
 *
 * 由于结果会非常大，请返回 10^9 + 7 的模。
 *
 *
 *
 * 示例 1：
 *
 * 输入：arr = [1,1,2,2,3,3,4,4,5,5], target = 8
 * 输出：20
 * 解释：
 * 按值枚举(arr[i], arr[j], arr[k])：
 * (1, 2, 5) 出现 8 次；
 * (1, 3, 4) 出现 8 次；
 * (2, 2, 4) 出现 2 次；
 * (2, 3, 3) 出现 2 次。
 *
 *
 * 示例 2：
 *
 * 输入：arr = [1,1,2,2,2,2], target = 5
 * 输出：12
 * 解释：
 * arr[i] = 1, arr[j] = arr[k] = 2 出现 12 次：
 * 我们从 [1,1] 中选择一个 1，有 2 种情况，
 * 从 [2,2,2,2] 中选出两个 2，有 6 种情况。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 3 <= arr.length <= 3000
 * 0 <= arr[i] <= 100
 * 0 <= target <= 300
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
const mod = 1_000_000_007

func threeSumMulti(arr []int, target int) int {
	sort.Ints(arr)
	n := len(arr)
	res := 0
	record := map[int]int{}
	for _, x := range arr{
		record[x] ++
	}

	if target % 3 == 0{
		v := record[target / 3]
		if v >= 3{
			res = (res + v * (v - 1) * (v - 2) / 6) % mod
		}
	}

	for i := 0 ; i < len(arr) ; i += record[arr[i]] {
		cnt := record[arr[i]]
		if cnt >= 2 && target > 3 *arr[i] && record[target - 2 * arr[i]] > 0{
			res = (res + ((cnt * (cnt - 1) / 2) * record[target - 2 * arr[i]]) % mod ) % mod
		}
		l, r := i + record[arr[i]], n - 1
		for l < r{
			s := arr[l] + arr[r] + arr[i]
			if s > target{
				r -= record[arr[r]]
			}else if s < target {
				l += record[arr[l]]
			}else{
				if (arr[l] != arr[r]){
					res = (res + (((cnt * record[arr[l]]) % mod) * record[arr[r]]) % mod) % mod
				}else{
					v := record[arr[l]]
					res = (res + (cnt * (v * (v - 1) / 2)) % mod) % mod
				}
				l += record[arr[l]]
				r -= record[arr[r]]
			}
		}
	}
	return res 
}
// @lc code=end



/*
// @lcpr case=start
// [92,4,59,23,100,16,7,15,3,78,98,17,77,33,83,15,87,35,54,72,58,14,87,47,58,31,72,58,87,22,25,54,27,53,13,54,61,12,96,24,35,43,94,1,88,76,89,89,41,56,61,65,60,91,89,79,86,52,27,2,97,46,50,46,87,93,71,87,95,78,65,10,35,51,34,66,61,7,49,38,10,1,88,37,50,84,35,20,7,83,51,85,11,12,89,93,54,23,36,95,100,19,82,67,96,77,53,56,51,16,54,7,30,68,78,13,38,52,91,44,54,17,21,44,4,10,85,19,11,88,73,36,47,53,3,21,41,24,60,53,88,35,48,89,35,3,43,85,45,67,56,78,44,49,29,35,68,96,29,21,51,17,52,99,3,48,65,51,22,38,77,81,30,64,99,35,88,72,73,29,29,2]\n105\n
// @lcpr case=end

// @lcpr case=start
// [1,1,2,2,2,2]\n5\n
// @lcpr case=end

 */

