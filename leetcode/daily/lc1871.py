#
# @lc app=leetcode.cn id=1871 lang=python3
# @lcpr version=21913
#
# [1871] 跳跃游戏 VII
#
# https://leetcode.cn/problems/jump-game-vii/description/
#
# algorithms
# Medium (28.50%)
# Likes:    77
# Dislikes: 0
# Total Accepted:    9.5K
# Total Submissions: 33.4K
# Testcase Example:  '"011010"\n2\n3'
#
# 给你一个下标从 0 开始的二进制字符串 s 和两个整数 minJump 和 maxJump 。一开始，你在下标 0 处，且该位置的值一定为 '0'
# 。当同时满足如下条件时，你可以从下标 i 移动到下标 j 处：
# 
# 
# i + minJump <= j <= min(i + maxJump, s.length - 1) 且
# s[j] == '0'.
# 
# 
# 如果你可以到达 s 的下标 s.length - 1 处，请你返回 true ，否则返回 false 。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "011010", minJump = 2, maxJump = 3
# 输出：true
# 解释：
# 第一步，从下标 0 移动到下标 3 。
# 第二步，从下标 3 移动到下标 5 。
# 
# 
# 示例 2：
# 
# 输入：s = "01101110", minJump = 2, maxJump = 3
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= s.length <= 10^5
# s[i] 要么是 '0' ，要么是 '1'
# s[0] == '0'
# 1 <= minJump <= maxJump < s.length
# 
# 
#

# @lc code=start
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False
        n = len(s) 
        d = [0] * (n + maxJump + 1)
        d[0] = 1
        d[1] = -1
        for i in range(n):
            d[i] += d[i - 1]
            if s[i] == '0' and d[i] > 0:
                d[i + minJump] += 1 
                d[i + maxJump + 1] -= 1
        return d[n - 1] > 0

# @lc code=end



#
# @lcpr case=start
# "011010"\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# "01101110"\n2\n3\n
# @lcpr case=end

#

