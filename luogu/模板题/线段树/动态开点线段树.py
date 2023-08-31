from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        n = 100000001
        A = SegTree(n)
        root = A.root
        ans = []
        height = 0
        max_num = 0
        for pos, h in positions:
            height = A.query(root, 0, n - 1, pos, pos + h - 1)
            max_num = max(max_num, height + h)
            A.update(root, 0, n - 1, pos, pos + h - 1, height + h)
            ans.append(max_num)
        return ans


class Node:

    def __init__(self) -> None:
        self.val = 0
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

    def __push_down(self, node):
        node.left.val = node.val
        node.right.val = node.val
        node.left.lazy = 1
        node.right.lazy = 1
        node.lazy = 0

    def update(self, node, lo, hi, left, right, tar):
        if left <= lo and right >= hi:
            node.val = tar
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

    def query(self, node, lo, hi, left, right):
        if left <= lo and right >= hi:
            return node.val
        self.__addnode(node)
        mid = lo + hi >> 1
        if node.lazy != 0:
            self.__push_down(node)
        a = b = 0
        if mid >= left:
            a = self.query(node.left, lo, mid, left, right)
        if mid < right:
            b = self.query(node.right, mid+1, hi, left, right)
        return max(a, b)
