#
# @lc app=leetcode.cn id=1147 lang=python3
# @lcpr version=21913
#
# [1147] 段式回文
#
# https://leetcode.cn/problems/longest-chunked-palindrome-decomposition/description/
#
# algorithms
# Hard (58.83%)
# Likes:    153
# Dislikes: 0
# Total Accepted:    23.5K
# Total Submissions: 39.9K
# Testcase Example:  '"ghiabcdefhelloadamhelloabcdefghi"'
#
# 你会得到一个字符串 text 。你应该把它分成 k 个子字符串 (subtext1, subtext2，…， subtextk) ，要求满足:
# 
# 
# subtexti 是 非空 字符串
# 所有子字符串的连接等于 text ( 即subtext1 + subtext2 + ... + subtextk == text )
# 对于所有 i 的有效值( 即 1 <= i <= k ) ，subtexti == subtextk - i + 1 均成立
# 
# 
# 返回k可能最大值。
# 
# 
# 
# 示例 1：
# 
# 输入：text = "ghiabcdefhelloadamhelloabcdefghi"
# 输出：7
# 解释：我们可以把字符串拆分成 "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)"。
# 
# 
# 示例 2：
# 
# 输入：text = "merchant"
# 输出：1
# 解释：我们可以把字符串拆分成 "(merchant)"。
# 
# 
# 示例 3：
# 
# 输入：text = "antaprezatepzapreanta"
# 输出：11
# 解释：我们可以把字符串拆分成 "(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)"。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= text.length <= 1000
# text 仅由小写英文字符组成
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
    def longestDecomposition(self, text: str) -> int:
        # 好像很难O(n), dp O(n^2)
        def z_function(s):
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r and z[i - l] < r - i + 1:
                    z[i] = z[i - l]
                else:
                    z[i] = max(0, r - i + 1)
                    while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                        z[i] += 1
                if i + z[i] - 1 > r:
                    l = i
                    r = i + z[i] - 1
            return z
        z = z_function(text)
        print(z)
        n = len(text)
        st = (n + 1) // 2 
        res = 0
        while st < n:
            if st + z[st] >= n:
                res += 1 
            st += 1 
        return res


# @lc code=end



#
# @lcpr case=start
# "ghiabcdefhelloadamhelloabcdefghi"\n
# @lcpr case=end

# @lcpr case=start
# "merchant"\n
# @lcpr case=end

# @lcpr case=start
# "antaprezatepzapreanta"\n
# @lcpr case=end

#

