#
# @lc app=leetcode.cn id=2034 lang=python3
# @lcpr version=21913
#
# [2034] 股票价格波动
#
# https://leetcode.cn/problems/stock-price-fluctuation/description/
#
# algorithms
# Medium (45.75%)
# Likes:    138
# Dislikes: 0
# Total Accepted:    24.4K
# Total Submissions: 53.4K
# Testcase Example:  '["StockPrice","update","update","current","maximum","update","maximum","update","minimum"]\n' +
# '[[],[1,10],[2,5],[],[],[1,3],[],[4,2],[]]'
#
# 给你一支股票价格的数据流。数据流中每一条记录包含一个 时间戳 和该时间点股票对应的 价格 。
# 
# 
# 不巧的是，由于股票市场内在的波动性，股票价格记录可能不是按时间顺序到来的。某些情况下，有的记录可能是错的。如果两个有相同时间戳的记录出现在数据流中，前一条记录视为错误记录，后出现的记录
# 更正 前一条错误的记录。
# 
# 请你设计一个算法，实现：
# 
# 
# 更新 股票在某一时间戳的股票价格，如果有之前同一时间戳的价格，这一操作将 更正 之前的错误价格。
# 找到当前记录里 最新股票价格 。最新股票价格 定义为时间戳最晚的股票价格。
# 找到当前记录里股票的 最高价格 。
# 找到当前记录里股票的 最低价格 。
# 
# 
# 请你实现 StockPrice 类：
# 
# 
# StockPrice() 初始化对象，当前无股票价格记录。
# void update(int timestamp, int price) 在时间点 timestamp 更新股票价格为 price 。
# int current() 返回股票 最新价格 。
# int maximum() 返回股票 最高价格 。
# int minimum() 返回股票 最低价格 。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：
# ["StockPrice", "update", "update", "current", "maximum", "update", "maximum",
# "update", "minimum"]
# [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
# 输出：
# [null, null, null, 5, 10, null, 5, null, 2]
# 
# 解释：
# StockPrice stockPrice = new StockPrice();
# stockPrice.update(1, 10); // 时间戳为 [1] ，对应的股票价格为 [10] 。
# stockPrice.update(2, 5);  // 时间戳为 [1,2] ，对应的股票价格为 [10,5] 。
# stockPrice.current();     // 返回 5 ，最新时间戳为 2 ，对应价格为 5 。
# stockPrice.maximum();     // 返回 10 ，最高价格的时间戳为 1 ，价格为 10 。
# stockPrice.update(1, 3);  // 之前时间戳为 1 的价格错误，价格更新为 3 。
# ⁠                         // 时间戳为 [1,2] ，对应股票价格为 [3,5] 。
# stockPrice.maximum();     // 返回 5 ，更正后最高价格为 5 。
# stockPrice.update(4, 2);  // 时间戳为 [1,2,4] ，对应价格为 [3,5,2] 。
# stockPrice.minimum();     // 返回 2 ，最低价格时间戳为 4 ，价格为 2 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= timestamp, price <= 10^9
# update，current，maximum 和 minimum 总 调用次数不超过 10^5 。
# current，maximum 和 minimum 被调用时，update 操作 至少 已经被调用过 一次 。
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
# 像是动态开点？？？

class Node:

    def __init__(self) -> None:
        self.val = 0
        self.mn = 1000000009
        self.lazy = 0
        self.left = None
        self.right = None


class SegTree:

    def __init__(self, n) -> None:
        self.n = n
        self.root = Node()

    def __addnode(self, node):
        if node.left == None:
            node.left = Node()
        if node.right == None:
            node.right = Node()

    def __push_up(self, node):
        node.val = max(node.left.val, node.right.val)
        node.mn = min(node.left.mn, node.right.mn)

    def __push_down(self, node):
        node.left.val = node.val
        node.right.val = node.val
        node.left.mn = node.mn
        node.right.mn = node.mn
        node.left.lazy = 1
        node.right.lazy = 1
        node.lazy = 0

    def update(self, node, lo, hi, left, right, tar):
        if left <= lo and right >= hi:
            node.val = tar
            node.mn = tar 
            node.lazy = 1
            return
        self.__addnode(node)
        mid = lo + hi >> 1
        if node.lazy != 0:
            self.__push_down(node)
        if mid >= left:
            self.update(node.left, lo, mid, left, right, tar)
        if mid < right:
            self.update(node.right, mid+1, hi, left, right, tar)
        self.__push_up(node)

    def queryMax(self, node, lo, hi, left, right):
        if left <= lo and right >= hi:
            return node.val
        self.__addnode(node)
        mid = lo + hi >> 1
        if node.lazy != 0:
            self.__push_down(node)
        a = b = 0
        if mid >= left:
            a = self.queryMax(node.left, lo, mid, left, right)
        if mid < right:
            b = self.queryMax(node.right, mid+1, hi, left, right)
        return max(a, b)

    def queryMin(self, node, lo, hi, left, right):
        if left <= lo and right >= hi:
            return node.mn
        self.__addnode(node)
        mid = lo + hi >> 1
        if node.lazy != 0:
            self.__push_down(node)
        a = b = 1000000009
        if mid >= left:
            a = self.queryMin(node.left, lo, mid, left, right)
        if mid < right:
            b = self.queryMin(node.right, mid+1, hi, left, right)
        return min(a, b)
class StockPrice:

    def __init__(self):
        self.n = 1000000009
        self.A = SegTree(self.n)
        self.root = self.A.root
        self.cur = 0 


    def update(self, timestamp: int, price: int) -> None:
        self.cur = max(self.cur, timestamp)
        self.A.update(self.root, 0, self.n - 1, timestamp, timestamp, price)
        
        

    def current(self) -> int:
        return self.A.queryMax(self.root, 0, self.n - 1, self.cur, self.cur)

    def maximum(self) -> int:
        return self.A.queryMax(self.root, 0, self.n - 1, 1, self.n - 1)


    def minimum(self) -> int:
        return self.A.queryMin(self.root, 0, self.n - 1, 1, self.n - 1)


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
# @lc code=end



#
# @lcpr case=start
# ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"][[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]\n
# @lcpr case=end

#

