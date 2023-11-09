#
# @lc app=leetcode.cn id=1363 lang=python3
# @lcpr version=21913
#
# [1363] 形成三的最大倍数
#
# https://leetcode.cn/problems/largest-multiple-of-three/description/
#
# algorithms
# Hard (35.99%)
# Likes:    81
# Dislikes: 0
# Total Accepted:    8K
# Total Submissions: 22.2K
# Testcase Example:  '[8,1,9]'
#
# 给你一个整数数组 digits，你可以通过按 任意顺序 连接其中某些数字来形成 3 的倍数，请你返回所能得到的最大的 3 的倍数。
# 
# 由于答案可能不在整数数据类型范围内，请以字符串形式返回答案。如果无法得到答案，请返回一个空字符串。返回的结果不应包含不必要的前导零。
# 
# 
# 
# 示例 1：
# 
# 输入：digits = [8,1,9]
# 输出："981"
# 
# 
# 示例 2：
# 
# 输入：digits = [8,6,7,1,0]
# 输出："8760"
# 
# 
# 示例 3：
# 
# 输入：digits = [1]
# 输出：""
# 
# 
# 示例 4：
# 
# 输入：digits = [0,0,0,0,0,0]
# 输出："0"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= digits.length <= 10^4
# 0 <= digits[i] <= 9
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
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        # 贪心， 最多只有两个数不会被选

        # 按照 mod 3 进行分类 
        m0 = []
        m1 = []
        m2 = []
        for x in digits :
            if x % 3 == 0:
                m0.append(x)
            elif x % 3 == 1:
                m1.append(x)
            else:
                m2.append(x)
        m0.sort(reverse=True)
        m1.sort(reverse=True)
        m2.sort(reverse=True)

        s = sum(digits)
        if s % 3 == 0:
            # 如果全是零
            if s == 0:
                return "0"
            return "".join(list(map(str, sorted(digits, reverse=True))))
        if s % 3 == 1:
            # 去除一个最小的 mod 3 == 1 的数
            if len(m1):
                m1.pop()
            else :
                m2.pop()
                m2.pop()
        else:  
            # 去除一个最小的 mod 3 == 1 的数
            if len(m2):
                m2.pop()
            else:
                m1.pop()
                m1.pop()
        m = m0 + m1 + m2
        m.sort(reverse=True)
        if len(m) == 0:
            return ""
        if sum(m) == 0:
            return "0"
        return  "".join(list(map(str, m)))
# @lc code=end



#
# @lcpr case=start
# [8,1,9]\n
# @lcpr case=end

# @lcpr case=start
# [8,6,7,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0,0,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [5, 8]\n
# @lcpr case=end
#

