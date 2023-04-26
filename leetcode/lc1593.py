#
# @lc app=leetcode.cn id=1593 lang=python3
# @lcpr version=21907
#
# [1593] 拆分字符串使唯一子字符串的数目最大
#
from typing import List
# @lc code=start
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = 1
        record = set()
        def dfs(i, pre):
            nonlocal res
            if i == len(s):
                if pre == len(s):
                    res = max(res, len(record))
                return
            if s[pre: i + 1] not in record:
                record.add(s[pre:i + 1])
                dfs(i + 1, i + 1)
                record.remove(s[pre:i + 1])
            dfs(i + 1, pre)
        dfs(0, 0)
        return res
# @lc code=end



#
# @lcpr case=start
# "ababccc"\n
# @lcpr case=end

# @lcpr case=start
# "aba"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n
# @lcpr case=end

#

