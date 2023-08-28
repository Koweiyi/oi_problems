#
# @lc app=leetcode.cn id=842 lang=python3
# @lcpr version=21913
#
# [842] 将数组拆分成斐波那契序列
#
# https://leetcode.cn/problems/split-array-into-fibonacci-sequence/description/
#
# algorithms
# Medium (48.31%)
# Likes:    290
# Dislikes: 0
# Total Accepted:    34.2K
# Total Submissions: 70.8K
# Testcase Example:  '"1101111"'
#
# 给定一个数字字符串 num，比如 "123456579"，我们可以将它分成「斐波那契式」的序列 [123, 456, 579]。
# 
# 形式上，斐波那契式 序列是一个非负整数列表 f，且满足：
# 
# 
# 0 <= f[i] < 2^31 ，（也就是说，每个整数都符合 32 位 有符号整数类型）
# f.length >= 3
# 对于所有的0 <= i < f.length - 2，都有 f[i] + f[i + 1] = f[i + 2]
# 
# 
# 另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。
# 
# 返回从 num 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 []。
# 
# 
# 
# 示例 1：
# 
# 输入：num = "1101111"
# 输出：[11,0,11,11]
# 解释：输出[110,1,111]也可以。
# 
# 示例 2：
# 
# 输入: num = "112358130"
# 输出: []
# 解释: 无法拆分。
# 
# 
# 示例 3：
# 
# 输入："0123"
# 输出：[]
# 解释：每个块的数字不能以零开头，因此 "01"，"2"，"3" 不是有效答案。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= num.length <= 200
# num 中只含有数字
# 
# 
#
from typing import List
from typing import Optional
from cmath import inf
from collections import Counter
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:

        def check(n:str) -> bool:
            return n == "0" or n[0] != '0'     
        n = len(num)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                res = []
                n0, n1 = num[:i + 1], num[i + 1:j + 1]
                if not check(n0) or not check(n1):
                    continue
                res.append(n0)
                res.append(n1)
                cur = j + 1
                flag = True
                while cur != n:
                    s = str(int(n0) + int(n1))
                    if cur + len(s) > n or num[cur:cur+len(s)] != s:
                        flag = False
                        break
                    res.append(s)
                    cur += len(s)
                    n0, n1 =  n1, int(s)
                if flag:
                    res =  list(map(int, res))
                    if max(res) < (1 << 31):
                        return res
        return []
                    

            
                

# @lc code=end



#
# @lcpr case=start
# "1101111"\n
# @lcpr case=end

# @lcpr case=start
# "112358130"\n
# @lcpr case=end

# @lcpr case=start
# "0123"\n
# @lcpr case=end

#

