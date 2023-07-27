#
# @lc app=leetcode.cn id=1461 lang=python3
# @lcpr version=21912
#
# [1461] 检查一个字符串是否包含所有长度为 K 的二进制子串
#
# https://leetcode.cn/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/
#
# algorithms
# Medium (52.47%)
# Likes:    58
# Dislikes: 0
# Total Accepted:    9.8K
# Total Submissions: 18.7K
# Testcase Example:  '"00110110"\n2'
#
# 给你一个二进制字符串 s 和一个整数 k 。如果所有长度为 k 的二进制字符串都是 s 的子串，请返回 true ，否则请返回 false 。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "00110110", k = 2
# 输出：true
# 解释：长度为 2 的二进制串包括 "00"，"01"，"10" 和 "11"。它们分别是 s 中下标为 0，1，3，2 开始的长度为 2 的子串。
# 
# 
# 示例 2：
# 
# 输入：s = "0110", k = 1
# 输出：true
# 解释：长度为 1 的二进制串包括 "0" 和 "1"，显然它们都是 s 的子串。
# 
# 
# 示例 3：
# 
# 输入：s = "0110", k = 2
# 输出：false
# 解释：长度为 2 的二进制串 "00" 没有出现在 s 中。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 5 * 10^5
# s[i] 不是'0' 就是 '1'
# 1 <= k <= 20
# 
# 
#

# @lc code=start
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        st = set()
        i = 0
        while i + k <= len(s):
            st.add(int(s[i: i + k]))
            i += 1
        return len(st) == 2 ** k
# @lc code=end



#
# @lcpr case=start
# "00110110"\n2\n
# @lcpr case=end

# @lcpr case=start
# "0110"\n1\n
# @lcpr case=end

# @lcpr case=start
# "0110"\n2\n
# @lcpr case=end

#

