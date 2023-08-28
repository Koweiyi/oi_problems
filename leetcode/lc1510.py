#
# @lc app=leetcode.cn id=1510 lang=python3
# @lcpr version=21913
#
# [1510] 石子游戏 IV
#
# https://leetcode.cn/problems/stone-game-iv/description/
#
# algorithms
# Hard (60.36%)
# Likes:    55
# Dislikes: 0
# Total Accepted:    8.6K
# Total Submissions: 14.3K
# Testcase Example:  '1'
#
# Alice 和 Bob 两个人轮流玩一个游戏，Alice 先手。
# 
# 一开始，有 n 个石子堆在一起。每个人轮流操作，正在操作的玩家可以从石子堆里拿走 任意 非零 平方数 个石子。
# 
# 如果石子堆里没有石子了，则无法操作的玩家输掉游戏。
# 
# 给你正整数 n ，且已知两个人都采取最优策略。如果 Alice 会赢得比赛，那么返回 True ，否则返回 False 。
# 
# 
# 
# 示例 1：
# 
# 输入：n = 1
# 输出：true
# 解释：Alice 拿走 1 个石子并赢得胜利，因为 Bob 无法进行任何操作。
# 
# 示例 2：
# 
# 输入：n = 2
# 输出：false
# 解释：Alice 只能拿走 1 个石子，然后 Bob 拿走最后一个石子并赢得胜利（2 -> 1 -> 0）。
# 
# 示例 3：
# 
# 输入：n = 4
# 输出：true
# 解释：n 已经是一个平方数，Alice 可以一次全拿掉 4 个石子并赢得胜利（4 -> 0）。
# 
# 
# 示例 4：
# 
# 输入：n = 7
# 输出：false
# 解释：当 Bob 采取最优策略时，Alice 无法赢得比赛。
# 如果 Alice 一开始拿走 4 个石子， Bob 会拿走 1 个石子，然后 Alice 只能拿走 1 个石子，Bob 拿走最后一个石子并赢得胜利（7
# -> 3 -> 2 -> 1 -> 0）。
# 如果 Alice 一开始拿走 1 个石子， Bob 会拿走 4 个石子，然后 Alice 只能拿走 1 个石子，Bob 拿走最后一个石子并赢得胜利（7
# -> 6 -> 2 -> 1 -> 0）。
# 
# 示例 5：
# 
# 输入：n = 17
# 输出：false
# 解释：如果 Bob 采取最优策略，Alice 无法赢得胜利。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 10^5
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
# 预处理平方数
mx = 100005
is_squre = [False] * mx 
i = 1 
while i * i < mx:
    is_squre[i * i] = True
    i += 1

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def solve(x: int) -> bool:
            # 如果是平方数 返回必胜
            if is_squre[x]:
                return True
            
            # 如果存在某个平方数使得对方不能必胜， 那么也就是自己必胜
            j = 1 
            while j * j < x:
                if not solve(x - j * j):
                    return True
                j += 1

            # 不存在以上状态使得自己必胜 也就是必败
            return False
        return solve(n)
            
# @lc code=end



#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 7\n
# @lcpr case=end

# @lcpr case=start
# 17\n
# @lcpr case=end

#

