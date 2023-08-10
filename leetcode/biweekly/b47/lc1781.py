#
# @lc app=leetcode.cn id=1781 lang=python3
# @lcpr version=21913
#
# [1781] 所有子字符串美丽值之和
#
# https://leetcode.cn/problems/sum-of-beauty-of-all-substrings/description/
#
# algorithms
# Medium (66.49%)
# Likes:    85
# Dislikes: 0
# Total Accepted:    24.9K
# Total Submissions: 37.4K
# Testcase Example:  '"aabcb"'
#
# 一个字符串的 美丽值 定义为：出现频率最高字符与出现频率最低字符的出现次数之差。
# 
# 
# 比方说，"abaacc" 的美丽值为 3 - 1 = 2 。
# 
# 
# 给你一个字符串 s ，请你返回它所有子字符串的 美丽值 之和。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "aabcb"
# 输出：5
# 解释：美丽值不为零的字符串包括 ["aab","aabc","aabcb","abcb","bcb"] ，每一个字符串的美丽值都为 1 。
# 
# 示例 2：
# 
# 输入：s = "aabcbaa"
# 输出：17
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <=^ 500
# s 只包含小写英文字母。
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
    def beautySum(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            cnt = Counter()
            for j in range(i, len(s)):
                cnt[s[j]] += 1
                res += max(cnt.values()) - min(cnt.values())
        return res 

# @lc code=end



#
# @lcpr case=start
# "aabcb"\n
# @lcpr case=end

# @lcpr case=start
# "aabcbaa"\n
# @lcpr case=end

#

