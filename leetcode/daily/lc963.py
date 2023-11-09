#
# @lc app=leetcode.cn id=963 lang=python3
# @lcpr version=21917
#
# [963] 最小面积矩形 II
#
# https://leetcode.cn/problems/minimum-area-rectangle-ii/description/
#
# algorithms
# Medium (51.42%)
# Likes:    67
# Dislikes: 0
# Total Accepted:    4K
# Total Submissions: 7.7K
# Testcase Example:  '[[1,2],[2,1],[1,0],[0,1]]'
#
# 给定在 xy 平面上的一组点，确定由这些点组成的任何矩形的最小面积，其中矩形的边不一定平行于 x 轴和 y 轴。
# 
# 如果没有任何矩形，就返回 0。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：[[1,2],[2,1],[1,0],[0,1]]
# 输出：2.00000
# 解释：最小面积的矩形出现在 [1,2],[2,1],[1,0],[0,1] 处，面积为 2。
# 
# 示例 2：
# 
# 
# 
# 输入：[[0,1],[2,1],[1,1],[1,0],[2,0]]
# 输出：1.00000
# 解释：最小面积的矩形出现在 [1,0],[1,1],[2,1],[2,0] 处，面积为 1。
# 
# 
# 示例 3：
# 
# 
# 
# 输入：[[0,3],[1,2],[3,1],[1,3],[2,1]]
# 输出：0
# 解释：没法从这些点中组成任何矩形。
# 
# 
# 示例 4：
# 
# 
# 
# 输入：[[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
# 输出：2.00000
# 解释：最小面积的矩形出现在 [2,1],[2,3],[3,3],[3,1] 处，面积为 2。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= points.length <= 50
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# 所有的点都是不同的。
# 与真实值误差不超过 10^-5 的答案将视为正确结果。
# 
# 
#
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from itertools import accumulate
from functools import cache
from typing import Optional
from typing import List
from cmath import inf, sqrt
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def minAreaFreeRect(self, p: List[List[int]]) -> float:
        n = len(p)
        res = inf

        ps = {(x, y): i for i, (x, y) in enumerate(p)}
        # 向量 平行 
        def check(A, B):
            return A[0] * B[1] - A[1] * B[0] == 0
        
        # 向量 垂直 
        def check2(A, B):
            return A[0] * B[0] + A[1] * B[1] == 0

        # 交差积
        def cross(A, B):
            return A[0] * B[1] - A[1] * B[0]
        
        # 计算向量 
        def vec(a, b):
            return (b[0] - a[0], b[1] - a[1])
        
        @cache
        def calc(i, j, k, m):
            a, b, c, d = p[i], p[j], p[k], p[m]
            if check(vec(a, d), vec(b, c)) and check(vec(a, b), vec(d, c)) and check2(vec(a, b), vec(a, d)) and check2(vec(b, a), vec(b, c)):
                return abs(cross(vec(a, b),vec(a, d)))
            return inf 

        for i in range(n):
            for j in range(n):
                if j == i:continue
                for k in range(n):
                    if k == i or k == j:continue
                    v = vec(p[j], p[k])
                    x, y = p[i][0] + v[0], p[i][1] + v[1]
                    if (x, y) not in ps:
                        continue
                    res = min(res, calc(i, j, k, ps[x, y]))
        return res if res != inf else 0


                        


# @lc code=end



#
# @lcpr case=start
# [[1,2],[2,1],[1,0],[0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[2,1],[1,1],[1,0],[2,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,3],[1,2],[3,1],[1,3],[2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]\n
# @lcpr case=end

# @lcpr case=start
#[[0,2],[0,1],[3,3],[1,0],[2,3],[1,2],[1,3]]
# @lcpr case=end
#

# @lcpr case=start
# [[20214,34113],[5172,14529],[2099,3149],[12650,10018],[13932,15636],[20951,20718],[10343,1948],[12150,11804],[4391,9635],[5151,2363],[14243,2258],[17383,1283],[13751,17958],[5182,130],[8670,9644],[12570,13665],[23573,13878],[11034,24423],[14138,1453],[4694,18],[9492,10425],[20623,6323],[4800,1706],[2450,3806],[4104,4827],[10448,2753],[23232,12867],[20180,12598],[17087,13221],[20084,12850],[14931,12528],[12746,9766],[7631,14675],[10776,6251],[16088,16329],[8250,17769],[32412,22557],[14256,8411],[3616,4715],[16373,11118]]
# @lcpr case=end

