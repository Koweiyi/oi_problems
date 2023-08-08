#
# @lc app=leetcode.cn id=1031 lang=python3
# @lcpr version=21907
#
# [1031] 两个非重叠子数组的最大和 
#
from itertools import accumulate
from typing import List
# @lc code=start
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        s = list(accumulate(nums, initial=0))  # nums 的前缀和
        ans = 0
        def f(firstLen: int, secondLen: int) -> None:
            nonlocal ans
            maxSumA = 0
            for i in range(firstLen + secondLen, len(s)):
                maxSumA = max(maxSumA, s[i - secondLen] - s[i - secondLen - firstLen])
                ans = max(ans, maxSumA + s[i] - s[i - secondLen])
        f(firstLen, secondLen)  # 左 a 右 b
        f(secondLen, firstLen)  # 左 b 右 a
        return ans

# @lc code=end



#
# @lcpr case=start
# [0,6,5,2,2,5,1,9,4]\n1\n2\n
# @lcpr case=end

# @lcpr case=start
# [3,8,1,3,2,1,8,9,0]\n3\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,1,5,6,0,9,5,0,3,8]\n4\n3\n
# @lcpr case=end

#

