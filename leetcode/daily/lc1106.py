#
# @lc app=leetcode.cn id=1106 lang=python3
# @lcpr version=21913
#
# [1106] 解析布尔表达式
#
# https://leetcode.cn/problems/parsing-a-boolean-expression/description/
#
# algorithms
# Hard (68.55%)
# Likes:    198
# Dislikes: 0
# Total Accepted:    27.1K
# Total Submissions: 39.5K
# Testcase Example:  '"&(|(f))"'
#
# 布尔表达式 是计算结果不是 true 就是 false 的表达式。有效的表达式需遵循以下约定：
# 
# 
# 't'，运算结果为 true
# 'f'，运算结果为 false
# '!(subExpr)'，运算过程为对内部表达式 subExpr 进行 逻辑非（NOT）运算
# '&(subExpr1, subExpr2, ..., subExprn)'，运算过程为对 2 个或以上内部表达式 subExpr1, subExpr2,
# ..., subExprn 进行 逻辑与（AND）运算
# '|(subExpr1, subExpr2, ..., subExprn)'，运算过程为对 2 个或以上内部表达式 subExpr1, subExpr2,
# ..., subExprn 进行 逻辑或（OR）运算
# 
# 
# 给你一个以字符串形式表述的 布尔表达式 expression，返回该式的运算结果。
# 
# 题目测试用例所给出的表达式均为有效的布尔表达式，遵循上述约定。
# 
# 
# 
# 示例 1：
# 
# 输入：expression = "&(|(f))"
# 输出：false
# 解释：
# 首先，计算 |(f) --> f ，表达式变为 "&(f)" 。
# 接着，计算 &(f) --> f ，表达式变为 "f" 。
# 最后，返回 false 。
# 
# 
# 示例 2：
# 
# 输入：expression = "|(f,f,f,t)"
# 输出：true
# 解释：计算 (false OR false OR false OR true) ，结果为 true 。
# 
# 
# 示例 3：
# 
# 输入：expression = "!(&(f,t))"
# 输出：true
# 解释：
# 首先，计算 &(f,t) --> (false AND true) --> false --> f ，表达式变为 "!(f)" 。
# 接着，计算 !(f) --> NOT false --> true ，返回 true 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= expression.length <= 2 * 10^4
# expression[i] 为 '('、')'、'&'、'|'、'!'、't'、'f' 和 ',' 之一
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
    def parseBoolExpr(self, s: str) -> bool:
        mp = defaultdict(int)
        st = []
        for i, x in  enumerate(s):
            if x == '(':
                st.append(i)
            if x == ')':
                mp[st[-1]] = i 
                st.pop()        
        # 递归细节真的太麻烦了
        def dfs(l, r) -> bool:
            if s[l] == '!':
                return not dfs(l + 2, r - 1)
            if l == r:
                return s[l] == "t"
            sub = []
            i = l + 2
            while i < r:
                if s[i] == '!':
                    # 去掉括号
                    sub.append(not dfs(i + 2, mp[i + 1] - 1))
                    i = mp[i + 1] + 2
                elif s[i] == '&' or s[i] == '|':
                    sub.append(dfs(i, mp[i + 1]))
                    i = mp[i + 1] + 2
                else:
                    sub.append(s[i] == 't')
                    i += 2 
            if s[l] == '&':
                return all(x for x in sub)
            return any(x for x in sub)
        return dfs(0, len(s) - 1)
                



            
# @lc code=end



#
# @lcpr case=start
# "&(|(f))"\n
# @lcpr case=end

# @lcpr case=start
# "|(f,f,f,t)"\n
# @lcpr case=end

# @lcpr case=start
# "!(&(f,t))"\n
# @lcpr case=end

#

