#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 线段树节点
struct Node {
    int start, end; // 节点表示的区间的起始和结束位置
    int maxVal; 
    int minVal;    // 当前区间的最大值
    int lazy;       // 延迟标记，用于懒惰更新

    Node(int s, int e) : start(s), end(e), maxVal(0), minVal(0),lazy(0) {}
};

// 更新节点信息
void updateNode(Node& node, int val) {
    node.minVal += val;
    node.maxVal += val;
    node.lazy += val;
}

// 下传延迟标记
void propagateLazyTag(Node& node, vector<Node>& tree) {
    if (node.lazy != 0) {
        if (node.start != node.end) {
            // 将延迟标记下传给左右孩子节点
            tree[node.start * 2].lazy += node.lazy;
            tree[node.start * 2 + 1].lazy += node.lazy;
        }
        node.maxVal += node.lazy; // 更新当前节点的最大值
        node.minVal += node.lazy;
        node.lazy = 0; // 清空当前节点的延迟标记
    }
}

// 构建线段树
void buildSegmentTree(vector<int>& arr, vector<Node>& tree, int nodeIdx, int start, int end) {
    if (start == end) {
        tree[nodeIdx].maxVal = arr[start];
        return;
    }

    int mid = (start + end) / 2;
    buildSegmentTree(arr, tree, nodeIdx * 2, start, mid);
    buildSegmentTree(arr, tree, nodeIdx * 2 + 1, mid + 1, end);

    tree[nodeIdx].maxVal = max(tree[nodeIdx * 2].maxVal, tree[nodeIdx * 2 + 1].maxVal);
    tree[nodeIdx].minVal = min(tree[nodeIdx * 2].minVal, tree[nodeIdx * 2 + 1].minVal);
}

// 更新区间
void updateSegmentTree(vector<Node>& tree, int nodeIdx, int start, int end, int val) {
    propagateLazyTag(tree[nodeIdx], tree); // 下传延迟标记

    if (tree[nodeIdx].start == start && tree[nodeIdx].end == end) {
        updateNode(tree[nodeIdx], val);
        return;
    }

    int mid = (tree[nodeIdx].start + tree[nodeIdx].end) / 2;
    if (end <= mid) {
        updateSegmentTree(tree, nodeIdx * 2, start, end, val);
    } else if (start > mid) {
        updateSegmentTree(tree, nodeIdx * 2 + 1, start, end, val);
    } else {
        updateSegmentTree(tree, nodeIdx * 2, start, mid, val);
        updateSegmentTree(tree, nodeIdx * 2 + 1, mid + 1, end, val);
    }

    tree[nodeIdx].maxVal = max(tree[nodeIdx * 2].maxVal, tree[nodeIdx * 2 + 1].maxVal);
    tree[nodeIdx].minVal = min(tree[nodeIdx * 2].minVal, tree[nodeIdx * 2 + 1].minVal);

}

// 查询区间最值
int queryMaxSegmentTree(vector<Node>& tree, int nodeIdx, int start, int end) {
    propagateLazyTag(tree[nodeIdx], tree); // 下传延迟标记

    if (tree[nodeIdx].start == start && tree[nodeIdx].end == end) {
        return tree[nodeIdx].maxVal;
    }

    int mid = (tree[nodeIdx].start + tree[nodeIdx].end) / 2;
    if (end <= mid) {
        return queryMaxSegmentTree(tree, nodeIdx * 2, start, end);
    } else if (start > mid) {
        return queryMaxSegmentTree(tree, nodeIdx * 2 + 1, start, end);
    } else {
        int leftMax = queryMaxSegmentTree(tree, nodeIdx * 2, start, mid);
        int rightMax = queryMaxSegmentTree(tree, nodeIdx * 2 + 1, mid + 1, end);
        return max(leftMax, rightMax);
    }
}

int main() {
    vector<int> arr = {1, 3, 2, -5, 6, 4};
    int n = arr.size();

    // 构建线段树
    vector<Node> tree(4 * n);
    buildSegmentTree(arr, tree, 1, 0, n - 1);

    // 查询区间最值
    int maxVal = queryMaxSegmentTree(tree, 1, 0, n - 1);
    cout << "Max value in the range [0, " << n - 1 << "] is: " << maxVal << endl;

    // 更新区间
    updateSegmentTree(tree, 1, 2, 4, 1); // 将arr[2], arr[3], arr[4]增加1

    // 再次查询区间最值
    maxVal = queryMaxSegmentTree(tree, 1, 0, n - 1);
    cout << "Max value in the range [0, " << n - 1 << "] after update is: " << maxVal << endl;

    return 0;
}