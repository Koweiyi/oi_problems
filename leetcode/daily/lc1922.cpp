/*
 * @lc app=leetcode.cn id=1922 lang=cpp
 * @lcpr version=21907
 *
 * [1922] 统计好数字的数目
 *
 * https://leetcode.cn/problems/count-good-numbers/description/
 *
 * algorithms
 * Medium (36.07%)
 * Likes:    25
 * Dislikes: 0
 * Total Accepted:    6.8K
 * Total Submissions: 18.8K
 * Testcase Example:  '1'
 *
 * 我们称一个数字字符串是 好数字 当它满足（下标从 0 开始）偶数 下标处的数字为 偶数 且 奇数 下标处的数字为 质数 （2，3，5 或
 * 7）。
 * 
 * 
 * 比方说，"2582" 是好数字，因为偶数下标处的数字（2 和 8）是偶数且奇数下标处的数字（5 和 2）为质数。但 "3245" 不是 好数字，因为 3
 * 在偶数下标处但不是偶数。
 * 
 * 
 * 给你一个整数 n ，请你返回长度为 n 且为好数字的数字字符串 总数 。由于答案可能会很大，请你将它对 10^9 + 7 取余后返回 。
 * 
 * 一个 数字字符串 是每一位都由 0 到 9 组成的字符串，且可能包含前导 0 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：n = 1
 * 输出：5
 * 解释：长度为 1 的好数字包括 "0"，"2"，"4"，"6"，"8" 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：n = 4
 * 输出：400
 * 
 * 
 * 示例 3：
 * 
 * 输入：n = 50
 * 输出：564908303
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= n <= 10^15
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
    int mod = 1000000007;
    int countGoodNumbers(long long n) {
        function<int(int, ll, int)> fastPow = [](int a, ll n, int mod) -> int{
            ll res = 1, mul = a;
            while(n){
                if(n & 1) res = res * mul % mod;
                mul = mul * mul % mod;
                n >>= 1;
            }
            return res;
        };
       return (ll)fastPow(5, (n + 1)/ 2, mod) * fastPow(4, n / 2, mod) % mod;
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
// 50\n
// @lcpr case=end

 */

