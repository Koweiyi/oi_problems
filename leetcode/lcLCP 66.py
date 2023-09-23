#
# @lc app=leetcode.cn id=LCP 66 lang=python3
# @lcpr version=21913
#
# [LCP 66] 最小展台数量
#
# https://leetcode.cn/problems/600YaG/description/
#
# algorithms
# Easy (77.41%)
# Likes:    8
# Dislikes: 0
# Total Accepted:    5.7K
# Total Submissions: 7.4K
# Testcase Example:  '["acd","bed","accd"]'
#
# 力扣嘉年华将举办一系列展览活动，后勤部将负责为每场展览提供所需要的展台。
# 已知后勤部得到了一份需求清单，记录了近期展览所需要的展台类型， `demand[i][j]` 表示第 `i` 天展览时第 `j` 个展台的类型。
# 在满足每一天展台需求的基础上，请返回后勤部需要准备的 **最小** 展台数量。
# 
# **注意：**
# - 同一展台在不同天中可以重复使用。
# 
# **示例 1：**
# >输入：`demand = ["acd","bed","accd"]`
# >
# >输出：`6`
# >
# >解释：
# >第 `0` 天需要展台 `a、c、d`；
# >第 `1` 天需要展台 `b、e、d`；
# >第 `2` 天需要展台 `a、c、c、d`；
# >因此，后勤部准备 `abccde` 的展台，可以满足每天的展览需求;
# 
# **示例 2：**
# >输入：`demand = ["abc","ab","ac","b"]`
# >
# >输出：`3`
# 
# 
# **提示：**
# - `1 <= demand.length,demand[i].length <= 100`
# - `demand[i][j]` 仅为小写字母
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
    def minNumBooths(self, demand: List[str]) -> int:
        c = Counter()
        for s in demand:
            c |= Counter(s)
        return sum(c.values())
# @lc code=end



#
# @lcpr case=start
# ["acd","bed","accd"]\n
# @lcpr case=end

# @lcpr case=start
# ["abc","ab","ac","b"]`>\n
# @lcpr case=end

#

