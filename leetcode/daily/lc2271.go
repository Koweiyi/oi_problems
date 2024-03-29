/*
 * @lc app=leetcode.cn id=2271 lang=golang
 * @lcpr version=30106
 *
 * [2271] 毯子覆盖的最多白色砖块数
 *
 * https://leetcode.cn/problems/maximum-white-tiles-covered-by-a-carpet/description/
 *
 * algorithms
 * Medium (33.29%)
 * Likes:    52
 * Dislikes: 0
 * Total Accepted:    6.5K
 * Total Submissions: 19.5K
 * Testcase Example:  '[[1,5],[10,11],[12,18],[20,25],[30,32]]\n10'
 *
 * 给你一个二维整数数组 tiles ，其中 tiles[i] = [li, ri] ，表示所有在 li <= j <= ri 之间的每个瓷砖位置 j
 * 都被涂成了白色。
 *
 * 同时给你一个整数 carpetLen ，表示可以放在 任何位置 的一块毯子的长度。
 *
 * 请你返回使用这块毯子，最多 可以盖住多少块瓷砖。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
 * 输出：9
 * 解释：将毯子从瓷砖 10 开始放置。
 * 总共覆盖 9 块瓷砖，所以返回 9 。
 * 注意可能有其他方案也可以覆盖 9 块瓷砖。
 * 可以看出，瓷砖无法覆盖超过 9 块瓷砖。
 *
 *
 * 示例 2：
 *
 *
 *
 * 输入：tiles = [[10,11],[1,1]], carpetLen = 2
 * 输出：2
 * 解释：将毯子从瓷砖 10 开始放置。
 * 总共覆盖 2 块瓷砖，所以我们返回 2 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= tiles.length <= 5 * 10^4
 * tiles[i].length == 2
 * 1 <= li <= ri <= 10^9
 * 1 <= carpetLen <= 10^9
 * tiles 互相 不会重叠 。
 *
 *
 */

// @lcpr-template-start
package leetcode

import (
	"cmp"
	"slices"
)

type TreeNode struct {
	Val   int
	Right *TreeNode
	Left  *TreeNode
}

// @lcpr-template-end
// @lc code=start
func maximumWhiteTiles(tiles [][]int, carpetLen int) int {
	slices.SortFunc(tiles, func(a, b []int) int {
		return cmp.Compare(a[0], b[0])
	})

	left, cover := 0, 0 
	res := 0 

	for i := 0 ; i < len(tiles) ; i ++{
		tl, tr := tiles[i][0], tiles[i][1]
		cover += tr - tl + 1
		for tiles[left][1] + carpetLen - 1 < tr{
			cover -= tiles[left][1] - tiles[left][0] + 1
			left ++ 
		}
		
		res = max(res, cover - max(tr - carpetLen + 1 - tiles[left][0], 0))
	}
	return res 
}

// @lc code=end

/*
// @lcpr case=start
// [[1,5],[10,11],[12,18],[20,25],[30,32]]\n10\n
// @lcpr case=end

// @lcpr case=start
// [[10,11],[1,1]]\n2\n
// @lcpr case=end

*/
