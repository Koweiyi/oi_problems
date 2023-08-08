/*
 * @lc app=leetcode.cn id=1738 lang=cpp
 * @lcpr version=21907
 *
 * [1738] 找出第 K 大的异或坐标值
 *
 * https://leetcode.cn/problems/find-kth-largest-xor-coordinate-value/description/
 *
 * algorithms
 * Medium (65.13%)
 * Likes:    99
 * Dislikes: 0
 * Total Accepted:    31.5K
 * Total Submissions: 48.4K
 * Testcase Example:  '[[5,2],[1,6]]\n1'
 *
 * 给你一个二维矩阵 matrix 和一个整数 k ，矩阵大小为 m x n 由非负整数组成。
 * 
 * 矩阵中坐标 (a, b) 的 值 可由对所有满足 0 <= i <= a < m 且 0 <= j <= b < n 的元素
 * matrix[i][j]（下标从 0 开始计数）执行异或运算得到。
 * 
 * 请你找出 matrix 的所有坐标中第 k 大的值（k 的值从 1 开始计数）。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：matrix = [[5,2],[1,6]], k = 1
 * 输出：7
 * 解释：坐标 (0,1) 的值是 5 XOR 2 = 7 ，为最大的值。
 * 
 * 示例 2：
 * 
 * 输入：matrix = [[5,2],[1,6]], k = 2
 * 输出：5
 * 解释：坐标 (0,0) 的值是 5 = 5 ，为第 2 大的值。
 * 
 * 示例 3：
 * 
 * 输入：matrix = [[5,2],[1,6]], k = 3
 * 输出：4
 * 解释：坐标 (1,0) 的值是 5 XOR 1 = 4 ，为第 3 大的值。
 * 
 * 示例 4：
 * 
 * 输入：matrix = [[5,2],[1,6]], k = 4
 * 输出：0
 * 解释：坐标 (1,1) 的值是 5 XOR 2 XOR 1 XOR 6 = 0 ，为第 4 大的值。 * 
 * 提示：
 * 
 * 
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 1000
 * 0 <= matrix[i][j] <= 10^6
 * 1 <= k <= m * n
 * 
 *有点简单，就不写思路了，大该就是前缀异或和加优先队列，当然也可以都存起来，最后排序，
 *优先队列在k 比 m*n小很多的时候性能较优
 *本题有O(m*n)解法 
 */
#include<bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int m, n;
    long long s[1005][1005] = {0};
    vector<int> v;
    int kthLargestValue(vector<vector<int>>& matrix, int k) {
        m = matrix.size();
        n = matrix[0].size();
        for(int i = 0 ; i < m ; i ++){
            for(int j = 0 ; j < n ; j ++){
                s[i + 1][j + 1] = s[i][j + 1] ^ s[i + 1][j] ^ s[i][j] ^ matrix[i][j];
                v.push_back(s[i + 1][j + 1]);
            }
        }
        nth_element(v.begin(), v.begin() + m * n - k, v.end());
        return v[n * m - k];
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[8,10,5,8,5,7,6,0,1,4,10,6,4,3,6,8,7,9,4,2]]\n2\n
// @lcpr case=end

// @lcpr case=start
// [[5,2],[1,6]]\n2\n
// @lcpr case=end

// @lcpr case=start
// [[5,2],[1,6]]\n3\n
// @lcpr case=end

// @lcpr case=start
// [[5,2],[1,6]]\n4\n
// @lcpr case=end
// @lcpr case=start
// [[5,2],[1,6]]\n4\n
// @lcpr case=end

 */

