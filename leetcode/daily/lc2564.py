#
# @lc app=leetcode.cn id=2564 lang=python3
# @lcpr version=21914
#
# [2564] 子字符串异或查询
#
# https://leetcode.cn/problems/substring-xor-queries/description/
#
# algorithms
# Medium (36.62%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 13.4K
# Testcase Example:  '"101101"\n[[0,5],[1,2]]'
#
# 给你一个 二进制字符串 s 和一个整数数组 queries ，其中 queries[i] = [firsti, secondi] 。
# 
# 对于第 i 个查询，找到 s 的 最短子字符串 ，它对应的 十进制值 val 与 firsti 按位异或 得到 secondi ，换言之，val ^
# firsti == secondi 。
# 
# 第 i 个查询的答案是子字符串 [lefti, righti] 的两个端点（下标从 0 开始），如果不存在这样的子字符串，则答案为 [-1, -1]
# 。如果有多个答案，请你选择 lefti 最小的一个。
# 
# 请你返回一个数组 ans ，其中 ans[i] = [lefti, righti] 是第 i 个查询的答案。
# 
# 子字符串 是一个字符串中一段连续非空的字符序列。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "101101", queries = [[0,5],[1,2]]
# 输出：[[0,2],[2,3]]
# 解释：第一个查询，端点为 [0,2] 的子字符串为 "101" ，对应十进制数字 5 ，且 5 ^ 0 = 5 ，所以第一个查询的答案为
# [0,2]。第二个查询中，端点为 [2,3] 的子字符串为 "11" ，对应十进制数字 3 ，且 3 ^ 1 = 2 。所以第二个查询的答案为 [2,3]
# 。
# 
# 
# 示例 2：
# 
# 输入：s = "0101", queries = [[12,8]]
# 输出：[[-1,-1]]
# 解释：这个例子中，没有符合查询的答案，所以返回 [-1,-1] 。
# 
# 
# 示例 3：
# 
# 输入：s = "1", queries = [[4,5]]
# 输出：[[0,0]]
# 解释：这个例子中，端点为 [0,0] 的子字符串对应的十进制值为 1 ，且 1 ^ 4 = 5 。所以答案为 [0,0] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^4
# s[i] 要么是 '0' ，要么是 '1' 。
# 1 <= queries.length <= 10^5
# 0 <= firsti, secondi <= 10^9
# 
# 
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
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(s)
        # 预处理 s串 
        mp = {}
        for l in range(1, 32):
            for st in range(n):
                if st + l > n:
                    break
                num = int(s[st:st + l], 2)
                if num not in mp:
                    mp[num] = st 

        for x, y in queries:
            # t ^ x = y 
            t = x ^ y 
            # 每个询问 kmp 查询也是不可接受的 
            if t not in mp:
                res.append([-1, -1])
            else:
                res.append([mp[t], mp[t] + t.bit_length() - 1 if t else mp[t]])
        return res 
                
# @lc code=end



#
# @lcpr case=start
# "101101"\n[[0,5],[1,2]]\n
# @lcpr case=end

# @lcpr case=start
# "0101"\n[[12,8]]\n
# @lcpr case=end

# @lcpr case=start
# "1"\n[[4,5]]\n
# @lcpr case=end

# @lcpr case=start
# "111010110" \n [[4,2],[3,3],[6,4],[9,9],[10,28],[0,470],[5,83],[10,28],[8,15],[6,464],[0,3],[5,8],[7,7],[8,8],[6,208],[9,15],[2,2],[9,95]]\n
# @lcpr case=end

#

