#
# @lc app=leetcode.cn id=752 lang=python3
# @lcpr version=21913
#
# [752] 打开转盘锁
#
# https://leetcode.cn/problems/open-the-lock/description/
#
# algorithms
# Medium (52.70%)
# Likes:    627
# Dislikes: 0
# Total Accepted:    122.9K
# Total Submissions: 233.3K
# Testcase Example:  '["0201","0101","0102","1212","2002"]\n"0202"'
#
# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8',
# '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
# 
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
# 
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
# 
# 字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。
# 
# 
# 
# 示例 1:
# 
# 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# 输出：6
# 解释：
# 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
# 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
# 因为当拨动到 "0102" 时这个锁就会被锁定。
# 
# 
# 示例 2:
# 
# 输入: deadends = ["8888"], target = "0009"
# 输出：1
# 解释：把最后一位反向旋转一次即可 "0000" -> "0009"。
# 
# 
# 示例 3:
# 
# 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"],
# target = "8888"
# 输出：-1
# 解释：无法旋转到目标数字且不被锁定。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target 不在 deadends 之中
# target 和 deadends[i] 仅由若干位数字组成
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
    def openLock(self, deadends: List[str], target: str) -> int:
        # 搜索 
        s = set(deadends)
        if "0000" in s:
            return -1 
        s.add("0000")
        q = ["0000"]
        step = 0
        db1 = "1234567890" 
        db2 = "9012345678" 
        def change(x :str) -> List[str]:
            res = []
            ls = list(x)
            for i in range(4):
                pre = ls[i]
                ls[i] = db1[ord(pre) - ord('0')]
                res.append("".join(ls))
                ls[i] = db2[ord(pre) - ord('0')]
                res.append("".join(ls))
                ls[i] = pre 
            return res
        while q:
            tmp = q
            q = []
            for x in tmp:
                if x == target:
                    return step
                for y in change(x):
                    if y not in s:
                        s.add(y)
                        q.append(y)
            step += 1
        return -1 


# @lc code=end



#
# @lcpr case=start
# ["0201","0101","0102","1212","2002"]\n"0202"\n
# @lcpr case=end

# @lcpr case=start
# ["8888"]\n"0009"\n
# @lcpr case=end

# @lcpr case=start
# ["8887","8889","8878","8898","8788","8988","7888","9888"]\n"8888"\n
# @lcpr case=end

#

