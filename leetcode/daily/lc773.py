#
# @lc app=leetcode.cn id=773 lang=python3
# @lcpr version=21913
#
# [773] 滑动谜题
#
# https://leetcode.cn/problems/sliding-puzzle/description/
#
# algorithms
# Hard (70.05%)
# Likes:    317
# Dislikes: 0
# Total Accepted:    35.8K
# Total Submissions: 51.1K
# Testcase Example:  '[[1,2,3],[4,0,5]]'
#
# 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示。一次 移动 定义为选择 0
# 与一个相邻的数字（上下左右）进行交换.
# 
# 最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
# 
# 给出一个谜板的初始状态 board ，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：board = [[1,2,3],[4,0,5]]
# 输出：1
# 解释：交换 0 和 5 ，1 步完成
# 
# 
# 示例 2:
# 
# 
# 
# 输入：board = [[1,2,3],[5,4,0]]
# 输出：-1
# 解释：没有办法完成谜板
# 
# 
# 示例 3:
# 
# 
# 
# 输入：board = [[4,1,2],[5,0,3]]
# 输出：5
# 解释：
# 最少完成谜板的最少移动次数是 5 ，
# 一种移动路径:
# 尚未移动: [[4,1,2],[5,0,3]]
# 移动 1 次: [[4,1,2],[0,5,3]]
# 移动 2 次: [[0,1,2],[4,5,3]]
# 移动 3 次: [[1,0,2],[4,5,3]]
# 移动 4 次: [[1,2,0],[4,5,3]]
# 移动 5 次: [[1,2,3],[4,5,0]]
# 
# 
# 
# 
# 提示：
# 
# 
# board.length == 2
# board[i].length == 3
# 0 <= board[i][j] <= 5
# board[i][j] 中每个值都 不同
# 
# 
#
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter,deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # BFS  
        s = "".join(str(x) for row in board for x in row)
        vis, q = {s}, [s]
        mapping = [[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]
        def change(s: str) -> List[str]:
            res = []
            s = list(s)
            for i in range(6):
                if s[i] == '0':
                    for j in mapping[i]:
                        s[i], s[j] = s[j], s[i]
                        res.append("".join(s))
                        s[i], s[j] = s[j], s[i]
            return res 
        res = 0
        while len(q) > 0:
            tmp = q 
            q = []
            for x in tmp:
                if x == "123450": return res 
                for nx in change(x):
                    if nx not in vis:
                        vis.add(nx)
                        q.append(nx)      
            res += 1
        return -1
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,0,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[5,4,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,1,2],[5,0,3]]\n
# @lcpr case=end

#

