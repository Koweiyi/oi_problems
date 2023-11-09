#
# @lc app=leetcode.cn id=1340 lang=python3
# @lcpr version=21913
#
# [1340] 跳跃游戏 V
#
# https://leetcode.cn/problems/jump-game-v/description/
#
# algorithms
# Hard (59.52%)
# Likes:    106
# Dislikes: 0
# Total Accepted:    7.3K
# Total Submissions: 12.3K
# Testcase Example:  '[6,4,14,6,8,13,9,7,10,6,12]\n2'
#
# 给你一个整数数组 arr 和一个整数 d 。每一步你可以从下标 i 跳到：
# 
# 
# i + x ，其中 i + x < arr.length 且 0 < x <= d 。
# i - x ，其中 i - x >= 0 且 0 < x <= d 。
# 
# 
# 除此以外，你从下标 i 跳到下标 j 需要满足：arr[i] > arr[j] 且 arr[i] > arr[k] ，其中下标 k 是所有 i 到 j
# 之间的数字（更正式的，min(i, j) < k < max(i, j)）。
# 
# 你可以选择数组的任意下标开始跳跃。请你返回你 最多 可以访问多少个下标。
# 
# 请注意，任何时刻你都不能跳到数组的外面。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
# 输出：4
# 解释：你可以从下标 10 出发，然后如上图依次经过 10 --> 8 --> 6 --> 7 。
# 注意，如果你从下标 6 开始，你只能跳到下标 7 处。你不能跳到下标 5 处因为 13 > 9 。你也不能跳到下标 4 处，因为下标 5 在下标 4 和
# 6 之间且 13 > 9 。
# 类似的，你不能从下标 3 处跳到下标 2 或者下标 1 处。
# 
# 
# 示例 2：
# 
# 输入：arr = [3,3,3,3,3], d = 3
# 输出：1
# 解释：你可以从任意下标处开始且你永远无法跳到任何其他坐标。
# 
# 
# 示例 3：
# 
# 输入：arr = [7,6,5,4,3,2,1], d = 1
# 输出：7
# 解释：从下标 0 处开始，你可以按照数值从大到小，访问所有的下标。
# 
# 
# 示例 4：
# 
# 输入：arr = [7,1,7,1,7,1], d = 2
# 输出：2
# 
# 
# 示例 5：
# 
# 输入：arr = [66], d = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 10^5
# 1 <= d <= arr.length
# 
# 
#
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter
from functools import cache
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        left = [0] * n
        st = []
        for i in range(n):
            while st and arr[i] > arr[st[-1]]:
                st.pop()
            left[i] = (st[-1] if st else -1) + 1
            st.append(i)
        right = [0] * n 
        st = []
        for i in range(n - 1, -1, -1):
            while st and arr[i] > arr[st[-1]]:
                st.pop()
            right[i] = st[-1] - 1 if st else n - 1
            st.append(i)
        
        @cache
        def dfs(x: int) -> int:
            if left[x] == x and right[x] == x:
                return 0
            res = 0
            for y in range(max(left[x], x - d), min(right[x], x + d) + 1):
                if y != x:
                    res = max(res, dfs(y) + 1)
            return res
            
        return max(dfs(i) + 1 for i in range(n))
# @lc code=end



#
# @lcpr case=start
# [6,4,14,6,8,13,9,7,10,6,12]\n2\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [7,6,5,4,3,2,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [7,1,7,1,7,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [66]\n1\n
# @lcpr case=end

#

