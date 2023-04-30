/*
 * @lc app=leetcode.cn id=2033 lang=cpp
 * @lcpr version=21907
 *
 * [2033] 获取单值网格的最小操作数
 *
 * https://leetcode.cn/problems/minimum-operations-to-make-a-uni-value-grid/description/
 *
 * algorithms
 * Medium (43.02%)
 * Likes:    33
 * Dislikes: 0
 * Total Accepted:    6.5K
 * Total Submissions: 15.1K
 * Testcase Example:  '[[2,4],[6,8]]\n2'
 *
 * 给你一个大小为 m x n 的二维整数网格 grid 和一个整数 x 。每一次操作，你可以对 grid 中的任一元素 加 x 或 减 x 。
 * 
 * 单值网格 是全部元素都相等的网格。
 * 
 * 返回使网格化为单值网格所需的 最小 操作数。如果不能，返回 -1 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 输入：grid = [[2,4],[6,8]], x = 2
 * 输出：4
 * 解释：可以执行下述操作使所有元素都等于 4 ： 
 * - 2 加 x 一次。
 * - 6 减 x 一次。
 * - 8 减 x 两次。
 * 共计 4 次操作。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 
 * 输入：grid = [[1,5],[2,3]], x = 1
 * 输出：5
 * 解释：可以使所有元素都等于 3 。
 * 
 * 
 * 示例 3：
 * 
 * 
 * 
 * 输入：grid = [[1,2],[3,4]], x = 2
 * 输出：-1
 * 解释：无法使所有元素相等。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 10^5
 * 1 <= m * n <= 10^5
 * 1 <= x, grid[i][j] <= 10^4
 * 
 * 
 * 
 */
#include<bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        vector<int> v;
        for(auto& g : grid){
            for(auto a: g){
                v.push_back(a);
            }
        }
        // sort(v.begin(), v.end());
        for(int i = 1; i < v.size() ; i ++){
            if((v[i] - v[i - 1]) % x != 0)  return -1;
        }
        int res = 0;
        nth_element(v.begin(), v.begin() + v.size() / 2, v.end());
        int num = v[v.size() / 2];
        for(auto a : v){
            res += abs(a - num) / x;
        }
        return res;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[2,4],[6,8]]\n2\n
// @lcpr case=end

// @lcpr case=start
// [[1,5],[2,3]]\n1\n
// @lcpr case=end

// @lcpr case=start
// [[1,2],[3,4]]\n2\n
// @lcpr case=end

 */

