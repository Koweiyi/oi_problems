#
# @lc app=leetcode.cn id=LCP 01 lang=python3
# @lcpr version=21913
#
# [LCP 01] 猜数字
#
# https://leetcode.cn/problems/guess-numbers/description/
#
# algorithms
# Easy (84.64%)
# Likes:    153
# Dislikes: 0
# Total Accepted:    100.2K
# Total Submissions: 118.4K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# 小A 和 小B 在玩猜数字。小B 每次从 1, 2, 3 中随机选择一个，小A 每次也从 1, 2, 3 中选择一个猜。他们一共进行三次这个游戏，请返回
# 小A 猜对了几次？
# 
# 输入的guess数组为 小A 每次的猜测，answer数组为 小B 每次的选择。guess和answer的长度都等于3。
# 
# 
# 
# 示例 1：
# 
# 输入：guess = [1,2,3], answer = [1,2,3]
# 输出：3
# 解释：小A 每次都猜对了。
# 
# 示例 2：
# 
# 输入：guess = [2,2,3], answer = [3,2,1]
# 输出：1
# 解释：小A 只猜对了第二次。
# 
# 
# 
# 限制：
# 
# 
# guess 的长度 = 3
# answer 的长度 = 3
# guess 的元素取值为 {1, 2, 3} 之一。
# answer 的元素取值为 {1, 2, 3} 之一。
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
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum(guess[i] == answer[i] for i in range(3))
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n[1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,3]\n[3,2,1]\n
# @lcpr case=end

#

