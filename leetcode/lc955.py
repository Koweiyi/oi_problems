#
# @lc app=leetcode.cn id=955 lang=python3
# @lcpr version=21913
#
# [955] 删列造序 II
#
# https://leetcode.cn/problems/delete-columns-to-make-sorted-ii/description/
#
# algorithms
# Medium (35.64%)
# Likes:    84
# Dislikes: 0
# Total Accepted:    5.7K
# Total Submissions: 15.9K
# Testcase Example:  '["ca","bb","ac"]'
#
# 给定由 n 个字符串组成的数组 strs，其中每个字符串长度相等。
# 
# 选取一个删除索引序列，对于 strs 中的每个字符串，删除对应每个索引处的字符。
# 
# 比如，有 strs = ["abcdef", "uvwxyz"]，删除索引序列 {0, 2, 3}，删除后 strs 为["bef", "vyz"]。
# 
# 假设，我们选择了一组删除索引 answer，那么在执行删除操作之后，最终得到的数组的元素是按 字典序（strs[0] <= strs[1] <=
# strs[2] ... <= strs[n - 1]）排列的，然后请你返回 answer.length 的最小可能值。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：strs = ["ca","bb","ac"]
# 输出：1
# 解释： 
# 删除第一列后，strs = ["a", "b", "c"]。
# 现在 strs 中元素是按字典排列的 (即，strs[0] <= strs[1] <= strs[2])。
# 我们至少需要进行 1 次删除，因为最初 strs 不是按字典序排列的，所以答案是 1。
# 
# 
# 示例 2：
# 
# 输入：strs = ["xc","yb","za"]
# 输出：0
# 解释：
# strs 的列已经是按字典序排列了，所以我们不需要删除任何东西。
# 注意 strs 的行不需要按字典序排列。
# 也就是说，strs[0][0] <= strs[0][1] <= ... 不一定成立。
# 
# 
# 示例 3：
# 
# 输入：strs = ["zyx","wvu","tsr"]
# 输出：3
# 解释：
# 我们必须删掉每一列。
# 
# 
# 
# 
# 提示：
# 
# 
# n == strs.length
# 1 <= n <= 100
# 1 <= strs[i].length <= 100
# strs[i] 由小写英文字母组成
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
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0 
        # 检测每一组是否有序 
        # 如果已经有严格降序，就不用都有序

        #g[i][j] 为True表示strs[i] 严格大于 strs[j]
        g = [[False] * 105 for _ in range(105) ]

        n = len(strs)
        for j in range(len(strs[0])):
            chs = []
            for s in strs:
                chs.append(s[j])
            flag = False 
            for i in range(1, len(chs)):
                for k in range(i):
                    if g[k][i]:continue
                    if chs[k] > chs[i]:
                        # 需要删除
                        flag = True
            if flag:
                # g 关系不需要更新 
                res += 1
            else:
                # 不需要删除，将严格大于的关系更新
                for i in range(len(chs)):
                    for k in range(i + 1, len(chs)):
                        if chs[i] < chs[k]:
                            g[i][k] = True 
        return res 

# @lc code=end



#
# @lcpr case=start
# ["ca","bb","ac"]\n
# @lcpr case=end

# @lcpr case=start
# ["xc","yb","za"]\n
# @lcpr case=end

# @lcpr case=start
# ["zyx","wvu","tsr"]\n
# @lcpr case=end

#

