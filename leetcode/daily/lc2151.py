#
# @lc app=leetcode.cn id=2151 lang=python3
# @lcpr version=21917
#
# [2151] 基于陈述统计最多好人数
#
# https://leetcode.cn/problems/maximum-good-people-based-on-statements/description/
#
# algorithms
# Hard (50.64%)
# Likes:    39
# Dislikes: 0
# Total Accepted:    5.5K
# Total Submissions: 10.8K
# Testcase Example:  '[[2,1,2],[1,2,2],[2,0,2]]'
#
# 游戏中存在两种角色：
# 
# 
# 好人：该角色只说真话。
# 坏人：该角色可能说真话，也可能说假话。
# 
# 
# 给你一个下标从 0 开始的二维整数数组 statements ，大小为 n x n ，表示 n
# 个玩家对彼此角色的陈述。具体来说，statements[i][j] 可以是下述值之一：
# 
# 
# 0 表示 i 的陈述认为 j 是 坏人 。
# 1 表示 i 的陈述认为 j 是 好人 。
# 2 表示 i 没有对 j 作出陈述。
# 
# 
# 另外，玩家不会对自己进行陈述。形式上，对所有 0 <= i < n ，都有 statements[i][i] = 2 。
# 
# 根据这 n 个玩家的陈述，返回可以认为是 好人 的 最大 数目。
# 
# 
# 
# 示例 1：
# 
# 输入：statements = [[2,1,2],[1,2,2],[2,0,2]]
# 输出：2
# 解释：每个人都做一条陈述。
# - 0 认为 1 是好人。
# - 1 认为 0 是好人。
# - 2 认为 1 是坏人。
# 以 2 为突破点。
# - 假设 2 是一个好人：
# ⁠   - 基于 2 的陈述，1 是坏人。
# ⁠   - 那么可以确认 1 是坏人，2 是好人。
# ⁠   - 基于 1 的陈述，由于 1 是坏人，那么他在陈述时可能：
# ⁠       - 说真话。在这种情况下会出现矛盾，所以假设无效。
# ⁠       - 说假话。在这种情况下，0 也是坏人并且在陈述时说假话。
# ⁠   - 在认为 2 是好人的情况下，这组玩家中只有一个好人。
# - 假设 2 是一个坏人：
# ⁠   - 基于 2 的陈述，由于 2 是坏人，那么他在陈述时可能：
# ⁠       - 说真话。在这种情况下，0 和 1 都是坏人。
# ⁠           - 在认为 2 是坏人但说真话的情况下，这组玩家中没有一个好人。
# ⁠       - 说假话。在这种情况下，1 是好人。
# ⁠           - 由于 1 是好人，0 也是好人。
# ⁠           - 在认为 2 是坏人且说假话的情况下，这组玩家中有两个好人。
# 在最佳情况下，至多有两个好人，所以返回 2 。
# 注意，能得到此结论的方法不止一种。
# 
# 
# 示例 2：
# 
# 输入：statements = [[2,0],[0,2]]
# 输出：1
# 解释：每个人都做一条陈述。
# - 0 认为 1 是坏人。
# - 1 认为 0 是坏人。
# 以 0 为突破点。
# - 假设 0 是一个好人：
# ⁠   - 基于与 0 的陈述，1 是坏人并说假话。
# ⁠   - 在认为 0 是好人的情况下，这组玩家中只有一个好人。
# - 假设 0 是一个坏人：
# ⁠   - 基于 0 的陈述，由于 0 是坏人，那么他在陈述时可能：
# ⁠       - 说真话。在这种情况下，0 和 1 都是坏人。
# ⁠           - 在认为 0 是坏人但说真话的情况下，这组玩家中没有一个好人。
# ⁠       - 说假话。在这种情况下，1 是好人。
# ⁠           - 在认为 0 是坏人且说假话的情况下，这组玩家中只有一个好人。
# 在最佳情况下，至多有一个好人，所以返回 1 。 
# 注意，能得到此结论的方法不止一种。
# 
# 
# 
# 
# 提示：
# 
# 
# n == statements.length == statements[i].length
# 2 <= n <= 15
# statements[i][j] 的值为 0、1 或 2
# statements[i][i] == 2
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
    def maximumGood(self, statements: List[List[int]]) -> int:
        res = 0 
        n = len(statements)
        good = set()
        def check():
            for x in good:
                for j in range(n):
                    if statements[x][j] == 0 and j  in good or statements[x][j] == 1 and j not in good:
                        return False
            return True 
        def dfs(i):
            nonlocal res 
            # 加入剪枝
            if (n - i) + len(good) < res:
                return
            if i == n:
                if check():
                    res = max(res, len(good))
                return
            dfs(i + 1)
            good.add(i)
            dfs(i + 1)
            good.remove(i)
        dfs(0)
        return res 
# @lc code=end



#
# @lcpr case=start
# [[2,1,2],[1,2,2],[2,0,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,0],[0,2]]\n
# @lcpr case=end

#

