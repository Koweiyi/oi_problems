#
# @lc app=leetcode.cn id=1345 lang=python3
# @lcpr version=21913
#
# [1345] 跳跃游戏 IV
#
# https://leetcode.cn/problems/jump-game-iv/description/
#
# algorithms
# Hard (45.61%)
# Likes:    236
# Dislikes: 0
# Total Accepted:    29.6K
# Total Submissions: 64.8K
# Testcase Example:  '[100,-23,-23,404,100,23,23,23,3,404]'
#
# 给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。
# 
# 每一步，你可以从下标 i 跳到下标 i + 1 、i - 1 或者 j ：
# 
# 
# i + 1 需满足：i + 1 < arr.length
# i - 1 需满足：i - 1 >= 0
# j 需满足：arr[i] == arr[j] 且 i != j
# 
# 
# 请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。
# 
# 注意：任何时候你都不能跳到数组外面。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [100,-23,-23,404,100,23,23,23,3,404]
# 输出：3
# 解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。
# 
# 
# 示例 2：
# 
# 输入：arr = [7]
# 输出：0
# 解释：一开始就在最后一个元素处，所以你不需要跳跃。
# 
# 
# 示例 3：
# 
# 输入：arr = [7,6,9,6,9,6,9,7]
# 输出：1
# 解释：你可以直接从下标 0 处跳到下标 7 处，也就是数组的最后一个元素处。
# 
# 
# 
# 
# 提示：
# 
# 
# 
# 1 <= arr.length <= 5 * 10^4
# -10^8 <= arr[i] <= 10^8
# 
# 
#
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter, defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # BFS 
        if len(arr) == 1:
            return 0 
        n = len(arr)
        vis = [False] * n           # vis表示某个下标是否被访问过
        vis[0] = True 
        mp = defaultdict(list)      # mp 存储相同的元素的下标集合
        for i, x in enumerate(arr):
            mp[x].append(i)
        res = 0                     # 跳跃次数
        q = [0]
        while q:
            tmp, q = q, []
            for x in tmp:
                if x == n - 1:  return res    # 访问到了最后节点 返回rank 
                if x + 1 < n and not vis[x + 1]:
                    q.append(x + 1)
                    vis[x + 1] = True 
                if x - 1 >= 0 and not vis[x - 1]:
                    q.append(x - 1)
                    vis[x - 1] = True 
                for id in mp[arr[x]]:
                    if not vis[id]:
                        vis[id] = True 
                        q.append(id)
                # 删除mp中的这个所有被访问过的节点，这个很重要， 
                # 因为不删除的话，后续还会重复对同一个数字进行判断，可能超时
                del mp[arr[x]]     
            res += 1 
        return -1 
# @lc code=end 



#
# @lcpr case=start
# [100,-23,-23,404,100,23,23,23,3,404]\n
# @lcpr case=end

# @lcpr case=start
# [7]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,9,6,9,6,9,7]\n
# @lcpr case=end

#

