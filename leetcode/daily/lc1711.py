#
# @lc app=leetcode.cn id=1711 lang=python3
# @lcpr version=21913
#
# [1711] 大餐计数
#
# https://leetcode.cn/problems/count-good-meals/description/
#
# algorithms
# Medium (35.97%)
# Likes:    142
# Dislikes: 0
# Total Accepted:    33.4K
# Total Submissions: 92.7K
# Testcase Example:  '[1,3,5,7,9]'
#
# 大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。
# 
# 你可以搭配 任意 两道餐品做一顿大餐。
# 
# 给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第 i^​​​​​​​​​​​​​​
# 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大餐 的数量。结果需要对 10^9 + 7 取余。
# 
# 注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。
# 
# 
# 
# 示例 1：
# 
# 输入：deliciousness = [1,3,5,7,9]
# 输出：4
# 解释：大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。
# 它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。
# 
# 
# 示例 2：
# 
# 输入：deliciousness = [1,1,1,3,3,3,7]
# 输出：15
# 解释：大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。
# 
# 
# 
# 提示：
# 
# 
# 1 <= deliciousness.length <= 10^5
# 0 <= deliciousness[i] <= 2^20
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
    def countPairs(self, deliciousness: List[int]) -> int:
        mod = 10 ** 9 + 7
        cnt = Counter()
        res = 0 
        for x in deliciousness:
            for j in range(41):
                if x <= (1 << j):
                    res = (res + cnt[(1 << j) - x]) % mod
            cnt[x] += 1
        return res 


# @lc code=end



#
# @lcpr case=start
# [1,3,5,7,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,3,3,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [149,107,1,63,0,1,6867,1325,5611,2581,39,89,46,18,12,20,22,234]\n
# @lcpr case=end
#

