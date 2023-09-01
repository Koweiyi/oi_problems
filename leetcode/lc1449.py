#
# @lc app=leetcode.cn id=1449 lang=python3
# @lcpr version=21913
#
# [1449] 数位成本和为目标值的最大数字
#
# https://leetcode.cn/problems/form-largest-integer-with-digits-that-add-up-to-target/description/
#
# algorithms
# Hard (62.30%)
# Likes:    168
# Dislikes: 0
# Total Accepted:    19.5K
# Total Submissions: 31.3K
# Testcase Example:  '[4,3,2,5,6,7,2,5,5]\n9'
#
# 给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：
# 
# 
# 给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
# 总成本必须恰好等于 target 。
# 添加的数位中没有数字 0 。
# 
# 
# 由于答案可能会很大，请你以字符串形式返回。
# 
# 如果按照上述要求无法得到任何整数，请你返回 "0" 。
# 
# 
# 
# 示例 1：
# 
# 输入：cost = [4,3,2,5,6,7,2,5,5], target = 9
# 输出："7772"
# 解释：添加数位 '7' 的成本为 2 ，添加数位 '2' 的成本为 3 。所以 "7772" 的代价为 2*3+ 3*1 = 9 。 "977"
# 也是满足要求的数字，但 "7772" 是较大的数字。
# ⁠数字     成本
# ⁠ 1  ->   4
# ⁠ 2  ->   3
# ⁠ 3  ->   2
# ⁠ 4  ->   5
# ⁠ 5  ->   6
# ⁠ 6  ->   7
# ⁠ 7  ->   2
# ⁠ 8  ->   5
# ⁠ 9  ->   5
# 
# 
# 示例 2：
# 
# 输入：cost = [7,6,5,5,5,6,8,7,8], target = 12
# 输出："85"
# 解释：添加数位 '8' 的成本是 7 ，添加数位 '5' 的成本是 5 。"85" 的成本为 7 + 5 = 12 。
# 
# 
# 示例 3：
# 
# 输入：cost = [2,4,6,2,4,6,4,4,4], target = 5
# 输出："0"
# 解释：总成本是 target 的条件下，无法生成任何整数。
# 
# 
# 示例 4：
# 
# 输入：cost = [6,10,15,40,40,40,40,40,40], target = 47
# 输出："32211"
# 
# 
# 
# 
# 提示：
# 
# 
# cost.length == 9
# 1 <= cost[i] <= 5000
# 1 <= target <= 5000
# 
# 
#
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter, defaultdict
from functools import cache
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        res = "0"
        mx_len = 0 
        n_cost =  []
        num = []
        for i in range(len(cost)):
            s = 0 
            k = 0
            while s < target:
                s += cost[i] * (1 << k)
                n_cost.append(cost[i ] * (1 << k)) 
                num.append(i + 1)
                k += 1
        use = [False] * 10 
        cnt = [0] * 10 

        @cache
        def dfs(i: int, target: int) -> bool:
            nonlocal mx_len
            if i == -1:
                if target == 0:
                    print(target, use, cnt, mx_len)
                if target == 0:
                    if sum(cnt) > mx_len:
                        mx_len = sum(cnt)
                        res = "".join(str(x)*cnt[x]  for x in range(9, 0, -1) if use[x])
                        print(res)
                    elif sum(cnt) == mx_len:
                        res = max(res, "".join(str(x)*cnt[x]  for x in range(9, 0, -1) if use[x]))
                    return True 
                return False 
            res = False
            # 选或者不选 
            if target < n_cost[i]:
                res = res or dfs(i - 1, target)


            use[num[i]] = True
            cnt[num[i]] += n_cost[i] // cost[num[i] - 1]
            res = res or dfs(i - 1,target - n_cost[i])
            use[num[i]] = False
            cnt[num[i]] -= n_cost[i] // cost[num[i] - 1]
        dfs(len(n_cost) - 1, target)
        return res 


        # 选出长度最长
        # 如果长度相同 选组合中最大值最大的
        # 
# @lc code=end



#
# @lcpr case=start
# [4,3,2,5,6,7,2,5,5]\n9\n
# @lcpr case=end

# @lcpr case=start
# [7,6,5,5,5,6,8,7,8]\n12\n
# @lcpr case=end

# @lcpr case=start
# [2,4,6,2,4,6,4,4,4]\n5\n
# @lcpr case=end

# @lcpr case=start
# [6,10,15,40,40,40,40,40,40]\n47\n
# @lcpr case=end

#

