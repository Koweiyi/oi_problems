#
# @lc app=leetcode.cn id=84 lang=python3
# @lcpr version=21913
#
# [84] 柱状图中最大的矩形
#
# https://leetcode.cn/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (45.12%)
# Likes:    2535
# Dislikes: 0
# Total Accepted:    360.6K
# Total Submissions: 799.2K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
# 
# 
# 示例 2：
# 
# 
# 
# 输入： heights = [2,4]
# 输出： 4
# 
# 
# 
# 提示：
# 
# 
# 1 <= heights.length <=10^5
# 0 <= heights[i] <= 10^4
# 
# 
#
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        right = [n] * n 
        st = []
        for i in range(n - 1, -1, -1):
            while st and heights[i] <= heights[st[-1]]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        st = []
        res = 0
        for i in range(n):
            while st and heights[i] <= heights[st[-1]]:
                st.pop()
            if not st:
                res = max(res, heights[i] * (right[i]))
            else:
                res = max(res, heights[i] * (right[i] - st[-1] - 1))
            st.append(i)
        return res 
# @lc code=end



#
# @lcpr case=start
# [2,1,5,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n
# @lcpr case=end

#

