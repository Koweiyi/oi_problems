#
# @lc app=leetcode.cn id=1301 lang=python3
# @lcpr version=21913
#
# [1301] 最大得分的路径数目
#
# https://leetcode.cn/problems/number-of-paths-with-max-score/description/
#
# algorithms
# Hard (37.75%)
# Likes:    78
# Dislikes: 0
# Total Accepted:    7.3K
# Total Submissions: 19.3K
# Testcase Example:  '["E23","2X2","12S"]\r'
#
# 给你一个正方形字符数组 board ，你从数组最右下方的字符 'S' 出发。
# 
# 你的目标是到达数组最左上角的字符 'E' ，数组剩余的部分为数字字符 1, 2, ..., 9 或者障碍
# 'X'。在每一步移动中，你可以向上、向左或者左上方移动，可以移动的前提是到达的格子没有障碍。
# 
# 一条路径的 「得分」 定义为：路径上所有数字的和。
# 
# 请你返回一个列表，包含两个整数：第一个整数是 「得分」 的最大值，第二个整数是得到最大得分的方案数，请把结果对 10^9 + 7 取余。
# 
# 如果没有任何路径可以到达终点，请返回 [0, 0] 。
# 
# 
# 
# 示例 1：
# 
# 输入：board = ["E23","2X2","12S"]
# 输出：[7,1]
# 
# 
# 示例 2：
# 
# 输入：board = ["E12","1X1","21S"]
# 输出：[4,2]
# 
# 
# 示例 3：
# 
# 输入：board = ["E11","XXX","11S"]
# 输出：[0,0]
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= board.length == board[i].length <= 100
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
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = 10 ** 9 + 7
        m, n = len(board), len(board[0])
        @cache 
        def dfs(x: int, y: int) -> (int, int):
            if x == m - 1 and y == n - 1:
                return 0, 1
            if board[x][y] == 'X':
                return -1, 0 
            if x == m - 1:
                score, t =  dfs(x, y + 1)
                if score != -1:
                    score += int(board[x][y])
                return score, t 
            if y == n - 1:
                score, t = dfs(x + 1, y)
                if score != - 1:
                    score += int(board[x][y])
                return score, t
            rs, rt = -1, 0 
            score, t = dfs(x + 1, y)
            if score > rs:
                rs = score
                rt = t 
            elif score == rs:
                rt = (rt + t) % mod 
            score, t = dfs(x, y + 1)
            if score > rs:
                rs = score
                rt = t 
            elif score == rs:
                rt = (rt + t) % mod
            score, t = dfs(x + 1, y + 1)
            if score > rs:
                rs = score
                rt = t 
            elif score == rs:
                rt = (rt + t) % mod 
            return rs + (0 if board[x][y] == 'E' else int(board[x][y])), rt 
        s, t = dfs(0, 0)
        if s == -1 or t == 0:
            return [0, 0]
        return [s, t]
        



# @lc code=end



#
# @lcpr case=start
# ["E23","2X2","12S"]\n
# @lcpr case=end

# @lcpr case=start
# ["E12","1X1","21S"]\n
# @lcpr case=end

# @lcpr case=start
#["E11345","X452XX","3X43X4","44X312","2345XX","1342XS"]\n
# @lcpr case=end

#

