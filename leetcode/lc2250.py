#
# @lc app=leetcode.cn id=2250 lang=python3
# @lcpr version=21917
#
# [2250] 统计包含每个点的矩形数目
#
# https://leetcode.cn/problems/count-number-of-rectangles-containing-each-point/description/
#
# algorithms
# Medium (34.95%)
# Likes:    47
# Dislikes: 0
# Total Accepted:    6.9K
# Total Submissions: 19.6K
# Testcase Example:  '[[1,2],[2,3],[2,5]]\n[[2,1],[1,4]]'
#
# 给你一个二维整数数组 rectangles ，其中 rectangles[i] = [li, hi] 表示第 i 个矩形长为 li 高为 hi
# 。给你一个二维整数数组 points ，其中 points[j] = [xj, yj] 是坐标为 (xj, yj) 的一个点。
# 
# 第 i 个矩形的 左下角 在 (0, 0) 处，右上角 在 (li, hi) 。
# 
# 请你返回一个整数数组 count ，长度为 points.length，其中 count[j]是 包含 第 j 个点的矩形数目。
# 
# 如果 0 <= xj <= li 且 0 <= yj <= hi ，那么我们说第 i 个矩形包含第 j 个点。如果一个点刚好在矩形的 边上
# ，这个点也被视为被矩形包含。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]
# 输出：[2,1]
# 解释：
# 第一个矩形不包含任何点。
# 第二个矩形只包含一个点 (2, 1) 。
# 第三个矩形包含点 (2, 1) 和 (1, 4) 。
# 包含点 (2, 1) 的矩形数目为 2 。
# 包含点 (1, 4) 的矩形数目为 1 。
# 所以，我们返回 [2, 1] 。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]
# 输出：[1,3]
# 解释：
# 第一个矩形只包含点 (1, 1) 。
# 第二个矩形只包含点 (1, 1) 。
# 第三个矩形包含点 (1, 3) 和 (1, 1) 。
# 包含点 (1, 3) 的矩形数目为 1 。
# 包含点 (1, 1) 的矩形数目为 3 。
# 所以，我们返回 [1, 3] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= rectangles.length, points.length <= 5 * 10^4
# rectangles[i].length == points[j].length == 2
# 1 <= li, xj <= 10^9
# 1 <= hi, yj <= 100
# 所有 rectangles 互不相同 。
# 所有 points 互不相同 。
# 
# 
#
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from itertools import accumulate
from functools import cache
from typing import Optional
from typing import List
from cmath import inf
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        mp = [[] for _ in range(101)]
        for l, h in rectangles:
            mp[h] .append(l)
        for i in range(101):
            mp[i].sort()
        res = []
        for x, y in points:
            cur = 0
            for i in range(y, 101):
                cur += len(mp[i]) - bisect_left(mp[i], x)
            res.append(cur)
        return res 
# @lc code=end



#
# @lcpr case=start
# [[1,2],[2,3],[2,5]]\n[[2,1],[1,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[2,2],[3,3]]\n[[1,3],[1,1]]\n
# @lcpr case=end

# @lcpr case=start
#[[81,69],[85,18],[4,89],[2,23],[29,25],[19,98],[77,74],[100,98],[61,5],[11,57],[23,4],[2,55],[8,77],[23,79],[4,69],[4,33],[44,69],[93,47],[77,4],[44,91],[11,54],[35,67],[59,90],[34,59],[16,25],[93,6],[37,14],[88,51],[13,69],[16,26],[77,7],[6,63],[3,41],[90,89],[97,35],[75,49],[96,94],[80,16],[96,59]]\n[[26,16],[58,70],[64,58],[52,2],[85,98],[75,93],[12,3],[2,25],[79,90],[36,35],[45,40],[12,34],[2,71],[63,88],[74,91],[78,90],[73,19],[95,92],[43,7],[9,28]]
# @lcpr case=end
#

