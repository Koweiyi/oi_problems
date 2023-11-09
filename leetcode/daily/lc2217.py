#
# @lc app=leetcode.cn id=2217 lang=python3
# @lcpr version=21913
#
# [2217] 找到指定长度的回文数
#
# https://leetcode.cn/problems/find-palindrome-with-fixed-length/description/
#
# algorithms
# Medium (33.86%)
# Likes:    30
# Dislikes: 0
# Total Accepted:    7.5K
# Total Submissions: 22K
# Testcase Example:  '[1,2,3,4,5,90]\n3'
#
# 给你一个整数数组 queries 和一个 正 整数 intLength ，请你返回一个数组 answer ，其中 answer[i] 是长度为
# intLength 的 正回文数 中第 queries[i] 小的数字，如果不存在这样的回文数，则为 -1 。
# 
# 回文数 指的是从前往后和从后往前读一模一样的数字。回文数不能有前导 0 。
# 
# 
# 
# 示例 1：
# 
# 输入：queries = [1,2,3,4,5,90], intLength = 3
# 输出：[101,111,121,131,141,999]
# 解释：
# 长度为 3 的最小回文数依次是：
# 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ...
# 第 90 个长度为 3 的回文数是 999 。
# 
# 
# 示例 2：
# 
# 输入：queries = [2,4,6], intLength = 4
# 输出：[1111,1331,1551]
# 解释：
# 长度为 4 的前 6 个回文数是：
# 1001, 1111, 1221, 1331, 1441 和 1551 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= queries.length <= 5 * 10^4
# 1 <= queries[i] <= 10^9
# 1 <= intLength <= 15
# 
# 
#
from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
from itertools import accumulate
from functools import cache
from typing import Optional
from typing import List
from cmath import inf
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        # 被灵神智商碾压了
        if intLength == 1:
            return  [q if q <= 9 else -1 for q in queries]
        path = [""] * intLength
        def dfs(i:int, left: int) -> int:
            if i == (intLength - 1) // 2  + 1 :
                return  int("".join(path))       
            cnt = pow(10, (intLength + 1) // 2 - i - 1)
            low = 1 if i == 0 else 0
            for x in range(low, 10):
                if left - cnt > 0:
                    left -= cnt
                else:
                    path[i] = path[len(path) - i - 1] = str(x)
                    return dfs(i + 1, left)
                
        mx = pow(10, (intLength + 1) // 2 - 1) * 9
        return [-1 if q > mx else dfs(0, q) for q in queries]

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,90]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,4,6]\n4\n
# @lcpr case=end

#

