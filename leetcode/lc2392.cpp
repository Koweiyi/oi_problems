/*
 * @lc app=leetcode.cn id=2392 lang=cpp
 * @lcpr version=21914
 *
 * [2392] 给定条件下构造矩阵
 *
 * https://leetcode.cn/problems/build-a-matrix-with-conditions/description/
 *
 * algorithms
 * Hard (55.99%)
 * Likes:    34
 * Dislikes: 0
 * Total Accepted:    5.7K
 * Total Submissions: 10.2K
 * Testcase Example:  '3\n[[1,2],[3,2]]\n[[2,1],[3,2]]'
 *
 * 给你一个 正 整数 k ，同时给你：
 * 
 * 
 * 一个大小为 n 的二维整数数组 rowConditions ，其中 rowConditions[i] = [abovei, belowi] 和
 * 一个大小为 m 的二维整数数组 colConditions ，其中 colConditions[i] = [lefti, righti] 。
 * 
 * 
 * 两个数组里的整数都是 1 到 k 之间的数字。
 * 
 * 你需要构造一个 k x k 的矩阵，1 到 k 每个数字需要 恰好出现一次 。剩余的数字都是 0 。
 * 
 * 矩阵还需要满足以下条件：
 * 
 * 
 * 对于所有 0 到 n - 1 之间的下标 i ，数字 abovei 所在的 行 必须在数字 belowi 所在行的上面。
 * 对于所有 0 到 m - 1 之间的下标 i ，数字 lefti 所在的 列 必须在数字 righti 所在列的左边。
 * 
 * 
 * 返回满足上述要求的 任意 矩阵。如果不存在答案，返回一个空的矩阵。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 输入：k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
 * 输出：[[3,0,0],[0,0,1],[0,2,0]]
 * 解释：上图为一个符合所有条件的矩阵。
 * 行要求如下：
 * - 数字 1 在第 1 行，数字 2 在第 2 行，1 在 2 的上面。
 * - 数字 3 在第 0 行，数字 2 在第 2 行，3 在 2 的上面。
 * 列要求如下：
 * - 数字 2 在第 1 列，数字 1 在第 2 列，2 在 1 的左边。
 * - 数字 3 在第 0 列，数字 2 在第 1 列，3 在 2 的左边。
 * 注意，可能有多种正确的答案。
 * 
 * 
 * 示例 2：
 * 
 * 输入：k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
 * 输出：[]
 * 解释：由前两个条件可以得到 3 在 1 的下面，但第三个条件是 3 在 1 的上面。
 * 没有符合条件的矩阵存在，所以我们返回空矩阵。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 2 <= k <= 400
 * 1 <= rowConditions.length, colConditions.length <= 10^4
 * rowConditions[i].length == colConditions[i].length == 2
 * 1 <= abovei, belowi, lefti, righti <= k
 * abovei != belowi
 * lefti != righti
 * 
 * 
 */
#include<bits/stdc++.h>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
// @lc code=start
class Solution {
private:
    vector<vector<int>> res;
    vector<vector<int>> g;
public:
    vector<vector<int>> buildMatrix(int k, vector<vector<int>>& rowConditions, vector<vector<int>>& colConditions) {
        res = vector<vector<int>>(k, vector<int>(k, 0));
        g = vector<vector<int>>(k + 1);
        
        vector<int> indeg(k + 1, 0);
        for (int i = 0 ; i < rowConditions.size(); i ++ ){
            int x = rowConditions[i][0], y = rowConditions[i][1];
            indeg[y] ++;
            g[x].push_back(y);
            g[y].push_back(x);
        }
       // 拓扑排序 
        unordered_map<int, int> row, col;
        queue<int> q;
        for(int i = 1 ;i <= k ; i ++ ){
            if (indeg[i] == 0){
                q.push(i);
            }
        }
        int idx = 0;
        while(!q.empty()){
            int x = q.front();q.pop();
            row[x] = idx++;
            for(int y : g[x]){
                indeg[y] -= 1;
                if (indeg[y] == 0){
                    q.push(y);
                }
            }
        } 
        for(int i = 1; i <= k ; i ++ ){
            if (row.find(i) == row.end()){
                return {};
            }
        }
        g = vector<vector<int>>(k + 1);
        indeg = vector<int>(k + 1, 0);
        
        for (int i = 0 ; i < colConditions.size(); i ++ ){
            int x = colConditions[i][0], y = colConditions[i][1];
            indeg[y] ++;
            g[x].push_back(y);
            g[y].push_back(x);
        }
       // 拓扑排序 
        for(int i = 0 ;i < k ; i ++ ){
            if (indeg[i + 1] == 0){
                q.push(i + 1);
            }
        }
        idx = 0;
        while(!q.empty()){
            int x = q.front();q.pop();
            col[x] = idx++;
            for(int y : g[x]){
                indeg[y] -= 1;
                if (indeg[y] == 0){
                    q.push(y);
                }
            }
        } 
        if (idx != k){
            return {}; 
        }

        for(int i = 1 ; i <= k; i ++){
            res[row[i]][col[i]] = i;
        }
        return res;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 3\n[[1,2],[3,2]]\n[[2,1],[3,2]]\n
// @lcpr case=end

// @lcpr case=start
// 3\n[[1,2],[2,3],[3,1],[2,3]]\n[[2,1]]\n
// @lcpr case=end

 */

