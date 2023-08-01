#
# @lc app=leetcode.cn id=2801 lang=python3
# @lcpr version=21913
#
# [2801] 统计范围内的步进数字数目
#
# https://leetcode.cn/problems/count-stepping-numbers-in-range/description/
#
# algorithms
# Hard (39.53%)
# Likes:    9
# Dislikes: 0
# Total Accepted:    1.7K
# Total Submissions: 4.4K
# Testcase Example:  '"1"\n"11"'
#
# 给你两个正整数 low 和 high ，都用字符串表示，请你统计闭区间 [low, high] 内的 步进数字 数目。
# 
# 如果一个整数相邻数位之间差的绝对值都 恰好 是 1 ，那么这个数字被称为 步进数字 。
# 
# 请你返回一个整数，表示闭区间 [low, high] 之间步进数字的数目。
# 
# 由于答案可能很大，请你将它对 10^9 + 7 取余 后返回。
# 
# 注意：步进数字不能有前导 0 。
# 
# 
# 
# 示例 1：
# 
# 输入：low = "1", high = "11"
# 输出：10
# 解释：区间 [1,11] 内的步进数字为 1 ，2 ，3 ，4 ，5 ，6 ，7 ，8 ，9 和 10 。总共有 10 个步进数字。所以输出为 10 。
# 
# 示例 2：
# 
# 输入：low = "90", high = "101"
# 输出：2
# 解释：区间 [90,101] 内的步进数字为 98 和 101 。总共有 2 个步进数字。所以输出为 2 。
# 
# 
# 
# 提示：
# 
# 
# 1 <= int(low) <= int(high) < 10^100
# 1 <= low.length, high.length <= 100
# low 和 high 只包含数字。
# low 和 high 都不含前导 0 。
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
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10 ** 9 + 7 
        def clac(s: str) -> int :
            @cache
            def f(i: int, pre: int, is_limit: bool, is_num: bool) -> int:
                if i == len(s):
                    return int(is_num)
                res = 0 if is_num else f(i + 1, pre, False, False)
                low = 0 if is_num else 1
                up = int(s[i]) if is_limit else 9
                for d in range(low, up + 1):
                    if not is_num or abs(d - pre) == 1:
                        res += f(i + 1, d, is_limit and d == up, True)
                return res % MOD
            return f(0, 0, True, False)
        return (clac(high) - clac(str(int(low) - 1))) % MOD 
                    
# @lc code=end



#
# @lcpr case=start
# "1"\n"11"\n
# @lcpr case=end

# @lcpr case=start
# "90"\n"101"\n
# @lcpr case=end

#

