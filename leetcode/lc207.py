#
# @lc app=leetcode.cn id=207 lang=python3
# @lcpr version=21913
#
# [207] 课程表
#
# https://leetcode.cn/problems/course-schedule/description/
#
# algorithms
# Medium (53.59%)
# Likes:    1755
# Dislikes: 0
# Total Accepted:    332.1K
# Total Submissions: 617.5K
# Testcase Example:  '2\n[[1,0]]'
#
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
# 
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi]
# ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
# 
# 
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 
# 
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
# 
# 示例 2：
# 
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
# 
# 
# 
# 提示：
# 
# 
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# prerequisites[i] 中的所有课程对 互不相同
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
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        for x, y in prerequisites:
            g[y].append(x)
            degree[x] += 1 
        q = [x for x in range(numCourses) if degree[x] == 0]

        vis = [False] * numCourses
        for x in q:
            vis[x] = True
        while q:
            tmp = q 
            q = [] 
            for x in tmp:
                for y in g[x]:
                    if vis[y]:
                        return False 
                    degree[y] -= 1
                    if degree[y] == 0:
                        q.append(y)
                        vis[y] = True
        return sum(vis) == numCourses
# @lc code=end



#
# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,0],[0,1]]\n
# @lcpr case=end

#

