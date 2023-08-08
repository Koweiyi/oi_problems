/*
 * @lc app=leetcode.cn id=1015 lang=cpp
 * @lcpr version=21907
 *
 * [1015] 可被 K 整除的最小整数
 *
 * https://leetcode.cn/problems/smallest-integer-divisible-by-k/description/
 *
 * algorithms
 * Medium (45.34%)
 * Likes:    145
 * Dislikes: 0
 * Total Accepted:    21.1K
 * Total Submissions: 46.6K
 * Testcase Example:  '1'
 *
 * 给定正整数 k ，你需要找出可以被 k 整除的、仅包含数字 1 的最 小 正整数 n 的长度。
 * 
 * 返回 n 的长度。如果不存在这样的 n ，就返回-1。
 * 
 * 注意： n 不符合 64 位带符号整数。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：k = 1
 * 输出：1
 * 解释：最小的答案是 n = 1，其长度为 1。
 * 
 * 示例 2：
 * 
 * 输入：k = 2
 * 输出：-1
 * 解释：不存在可被 2 整除的正整数 n 。
 * 
 * 示例 3：
 * 
 * 输入：k = 3
 * 输出：3
 * 解释：最小的答案是 n = 111，其长度为 3。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= k <= 10^5
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
#define ll long long
class Solution {
public:
    bool check(ll num){
        string s = to_string(num);
        for (char c : s){
            if (c != '1') return false;
        }
        return true;
    }
    int smallestRepunitDivByK(int k) {
        ll i = 1;
        int n = 1;
        while(i < LONG_LONG_MAX){
            if (i % k == 0) return n;
            else{
                
            } 
        }
    }
};
// @lc code=end



/*
// @lcpr case=start
// 1\n
// @lcpr case=end

// @lcpr case=start
// 2\n
// @lcpr case=end

// @lcpr case=start
// 3\n
// @lcpr case=end

 */

