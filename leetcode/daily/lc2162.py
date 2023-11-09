#
# @lc app=leetcode.cn id=2162 lang=python3
# @lcpr version=21801
#
# [2162] 设置时间的最少代价
#
# https://leetcode.cn/problems/minimum-cost-to-set-cooking-time/description/
#
# algorithms
# Medium (34.59%)
# Likes:    5
# Dislikes: 0
# Total Accepted:    3.6K
# Total Submissions: 10.4K
# Testcase Example:  '1\n2\n1\n600'
#
# 常见的微波炉可以设置加热时间，且加热时间满足以下条件：
# 
# 
# 至少为 1 秒钟。
# 至多为 99 分 99 秒。
# 
# 
# 你可以 最多 输入 4 个数字 来设置加热时间。如果你输入的位数不足 4 位，微波炉会自动加 前缀 0 来补足 4 位。微波炉会将设置好的四位数中，前
# 两位当作分钟数，后 两位当作秒数。它们所表示的总时间就是加热时间。比方说：
# 
# 
# 你输入 9 5 4 （三个数字），被自动补足为 0954 ，并表示 9 分 54 秒。
# 你输入 0 0 0 8 （四个数字），表示 0 分 8 秒。
# 你输入 8 0 9 0 ，表示 80 分 90 秒。
# 你输入 8 1 3 0 ，表示 81 分 30 秒。
# 
# 
# 给你整数 startAt ，moveCost ，pushCost 和 targetSeconds 。一开始，你的手指在数字 startAt 处。将手指移到
# 任何其他数字 ，需要花费 moveCost 的单位代价。每 输入你手指所在位置的数字一次，需要花费 pushCost 的单位代价。
# 
# 要设置 targetSeconds 秒的加热时间，可能会有多种设置方法。你想要知道这些方法中，总代价最小为多少。
# 
# 请你能返回设置 targetSeconds 秒钟加热时间需要花费的最少代价。
# 
# 请记住，虽然微波炉的秒数最多可以设置到 99 秒，但一分钟等于 60 秒。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：startAt = 1, moveCost = 2, pushCost = 1, targetSeconds = 600
# 输出：6
# 解释：以下为设置加热时间的所有方法。
# - 1 0 0 0 ，表示 10 分 0 秒。
# 手指一开始就在数字 1 处，输入 1 （代价为 1），移到 0 处（代价为 2），输入 0（代价为 1），输入 0（代价为 1），输入 0（代价为
# 1）。
# 总代价为：1 + 2 + 1 + 1 + 1 = 6 。这是所有方案中的最小代价。
# - 0 9 6 0，表示 9 分 60 秒。它也表示 600 秒。
# 手指移到 0 处（代价为 2），输入 0 （代价为 1），移到 9 处（代价为 2），输入 9（代价为 1），移到 6 处（代价为 2），输入 6（代价为
# 1），移到 0 处（代价为 2），输入 0（代价为 1）。
# 总代价为：2 + 1 + 2 + 1 + 2 + 1 + 2 + 1 = 12 。
# - 9 6 0，微波炉自动补全为 0960 ，表示 9 分 60 秒。
# 手指移到 9 处（代价为 2），输入 9 （代价为 1），移到 6 处（代价为 2），输入 6（代价为 1），移到 0 处（代价为 2），输入 0（代价为
# 1）。
# 总代价为：2 + 1 + 2 + 1 + 2 + 1 = 9 。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：startAt = 0, moveCost = 1, pushCost = 2, targetSeconds = 76
# 输出：6
# 解释：最优方案为输入两个数字 7 6，表示 76 秒。
# 手指移到 7 处（代价为 1），输入 7 （代价为 2），移到 6 处（代价为 1），输入 6（代价为 2）。总代价为：1 + 2 + 1 + 2 = 6
# 其他可行方案为 0076 ，076 ，0116 和 116 ，但是它们的代价都比 6 大。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= startAt <= 9
# 1 <= moveCost, pushCost <= 10^5
# 1 <= targetSeconds <= 6039
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
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        mn = targetSeconds // 60 
        se = targetSeconds % 60 

        def calc(x, y) -> int:
            res = 0 
            if x < 0 or x > 99 or y > 99:
                return inf 
            cur = startAt
            is_num = False 
            num = x * 100 + y 
            p = 1000
            for i in range(4):
                n = (num // p) % 10
                p //= 10
                if n == 0 and not is_num:
                    continue
                if cur != n:
                    res += moveCost 
                res += pushCost
                cur = n 
                is_num = True 
            return res 
        return min(calc(mn, se), calc(mn - 1, se + 60))


# @lc code=end

# @lcpr-div-debug-arg-start
# funName=
# paramTypes= []
# returnType=
# @lcpr-div-debug-arg-end


#
# @lcpr case=start
# 1\n2\n1\n600\n
# @lcpr case=end

# @lcpr case=start
# 0\n1\n2\n76\n
# @lcpr case=end

# @lcpr case=start
# 0\n9\n18\n460\n
# @lcpr case=end
#


