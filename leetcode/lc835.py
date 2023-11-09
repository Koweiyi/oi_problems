#
# @lc app=leetcode.cn id=835 lang=python3
# @lcpr version=21917
#
# [835] 图像重叠
#
# https://leetcode.cn/problems/image-overlap/description/
#
# algorithms
# Medium (58.01%)
# Likes:    94
# Dislikes: 0
# Total Accepted:    6.7K
# Total Submissions: 11.5K
# Testcase Example:  '[[1,1,0],[0,1,0],[0,1,0]]\n[[0,0,0],[0,1,1],[0,0,1]]'
#
# 给你两个图像 img1 和 img2 ，两个图像的大小都是 n x n ，用大小相同的二进制正方形矩阵表示。二进制矩阵仅由若干 0 和若干 1 组成。
# 
# 转换 其中一个图像，将所有的 1 向左，右，上，或下滑动任何数量的单位；然后把它放在另一个图像的上面。该转换的 重叠 是指两个图像 都 具有 1
# 的位置的数目。
# 
# 
# 
# 请注意，转换 不包括 向任何方向旋转。越过矩阵边界的 1 都将被清除。
# 
# 最大可能的重叠数量是多少？
# 
# 
# 
# 示例 1：
# 
# 输入：img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
# 输出：3
# 解释：将 img1 向右移动 1 个单位，再向下移动 1 个单位。
# 
# 两个图像都具有 1 的位置的数目是 3（用红色标识）。
# 
# 
# 
# 示例 2：
# 
# 输入：img1 = [[1]], img2 = [[1]]
# 输出：1
# 
# 
# 示例 3：
# 
# 输入：img1 = [[0]], img2 = [[0]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# n == img1.length == img1[i].length
# n == img2.length == img2[i].length
# 1 <= n <= 30
# img1[i][j] 为 0 或 1
# img2[i][j] 为 0 或 1
# 
# 
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
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        def solve(m1, m2, lx, ly):
            res = 0 
            for i in range(lx):
                for j in range(ly):
                    res += m1[i][j] == 1 and m2[n - lx + i][n - ly + j] == 1 
            return res 
        def solve2(m1, m2, lx, ly):
            res = 0 
            for i in range(lx):
                for j in range(n - ly, n):
                    res += m1[i][j] == 1 and m2[i + n - lx][j - n + ly] == 1
            return res 
        ans = 0 
        for lx in range(1, n + 1):
            for ly in range(1, n + 1):
                ans = max(ans, solve(img1, img2, lx, ly))
                ans = max(ans, solve(img2, img1, lx, ly))
                ans = max(ans, solve2(img1, img2, lx, ly))
                ans = max(ans, solve2(img2, img1, lx, ly))
        return ans 

# @lc code=end



#
# @lcpr case=start
# [[1,1,0],[0,1,0],[0,1,0]]\n[[0,0,0],[0,1,1],[0,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1]]\n[[1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0]]\n[[0]]\n
# @lcpr case=end


# @lcpr case=start
# [[0,1,1],[0,0,0],[0,0,0]]\n[[0,0,0],[0,0,0],[1,1,0]]\n
# @lcpr case=end

#

