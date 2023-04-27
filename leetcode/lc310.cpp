/*
 * @Author: Koweiyi 1423376854@qq.com
 * @Date: 2023-04-27 15:04:42
 * @LastEditors: Koweiyi 1423376854@qq.com
 * @LastEditTime: 2023-04-27 16:41:14
 * @FilePath: \oi_problems\leetcode\lc310.cpp
 * @Description:
 *
 * Copyright (c) 2023 by ${git_name_email}, All Rights Reserved.
 */
/*
 * @lc app=leetcode.cn id=310 lang=cpp
 * @lcpr version=21907
 *
 * [310] 最小高度树
 *
 * https://leetcode.cn/problems/minimum-height-trees/description/
 *
 * algorithms
 * Medium (42.72%)
 * Likes:    767
 * Dislikes: 0
 * Total Accepted:    58.8K
 * Total Submissions: 137.8K
 * Testcase Example:  '4\n[[1,0],[1,2],[1,3]]'
 *
 * 树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
 *
 * 给你一棵包含 n 个节点的树，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges
 * 列表（每一个边都是一对标签），其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。
 *
 * 可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。在所有可能的树中，具有最小高度的树（即，min(h)）被称为
 * 最小高度树 。
 *
 * 请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。
 * 树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。
 *
 *
 *
 * 示例 1：
 *
 * 输入：n = 4, edges = [[1,0],[1,2],[1,3]]
 * 输出：[1]
 * 解释：如图所示，当根是标签为 1 的节点时，树的高度是 1 ，这是唯一的最小高度树。
 *
 * 示例 2：
 *
 * 输入：n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
 * 输出：[3,4]
 *
 *
 *
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 2 * 10^4
 * edges.length == n - 1
 * 0 <= ai, bi < n
 * ai != bi
 * 所有 (ai, bi) 互不相同
 * 给定的输入 保证 是一棵树，并且 不会有重复的边
 *
 *
 */

/**
 * 思路：一眼树的直径,简单来说
 * 树的直径  最小数高
 *   1         1
 *   2         1
 *   3         2
 *   4         4
 * 也就是说最小树高 h = (d + 1) / 2 (d为树的直径)
 *
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
#define pii pair<int, int>
class Solution
{
public:
    vector<vector<int>> g;
    vector<int> p;
    int bfs(int x)
    {
        int n = g.size();
        queue<int> que;
        vector<bool> visited(n, false);
        que.push(x);
        visited[x] = true;
        int node = -1;

        while (!que.empty())
        {
            int cur = que.front();
            que.pop();
            node = cur;
            for (auto &y : g[cur])
            {
                if (!visited[y])
                {
                    visited[y] = true;
                    p[y] = cur;
                    que.push(y);
                }
            }
        }
        return node;
    }

    vector<int> findMinHeightTrees(int n, vector<vector<int>> &edges)
    {
        g.resize(n);
        p.resize(n, -1);
        for (auto &e : edges)
        {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        int x = bfs(0);
        int y = bfs(x);
        p[x] = -1;
        vector<int> v;
        int cur = y;
        while (cur != -1)
        {
            v.push_back(cur);
            cur = p[cur];
        }
        int m = v.size();
        if (m & 1)
            return {v[m / 2]};
        return {v[m / 2 - 1], v[m / 2]};
        
    }
};
// @lc code=end

/*
// @lcpr case=start
// 4\n[[1,0],[1,2],[1,3]]\n
// @lcpr case=end

// @lcpr case=start
// 6\n[[3,0],[3,1],[3,2],[3,4],[5,4]]\n
// @lcpr case=end

 */
