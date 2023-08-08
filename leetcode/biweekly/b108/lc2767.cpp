/*
 * @lc app=leetcode.cn id=2767 lang=cpp
 * @lcpr version=21909
 *
 * [2767] 将字符串分割为最少的美丽子字符串
 *
 * https://leetcode.cn/problems/partition-string-into-minimum-beautiful-substrings/description/
 *
 * algorithms
 * Medium (54.35%)
 * Likes:    5
 * Dislikes: 0
 * Total Accepted:    2.2K
 * Total Submissions: 4K
 * Testcase Example:  '"1011"'
 *
 * 给你一个二进制字符串 s ，你需要将字符串分割成一个或者多个 子字符串  ，使每个子字符串都是 美丽 的。
 * 
 * 如果一个字符串满足以下条件，我们称它是 美丽 的：
 * 
 * 
 * 它不包含前导 0 。
 * 它是 5 的幂的 二进制 表示。
 * 
 * 
 * 请你返回分割后的子字符串的 最少 数目。如果无法将字符串 s 分割成美丽子字符串，请你返回 -1 。
 * 
 * 子字符串是一个字符串中一段连续的字符序列。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：s = "1011"
 * 输出：2
 * 解释：我们可以将输入字符串分成 ["101", "1"] 。
 * - 字符串 "101" 不包含前导 0 ，且它是整数 5^1 = 5 的二进制表示。
 * - 字符串 "1" 不包含前导 0 ，且它是整数 5^0 = 1 的二进制表示。
 * 最少可以将 s 分成 2 个美丽子字符串。
 * 
 * 
 * 示例 2：
 * 
 * 输入：s = "111"
 * 输出：3
 * 解释：我们可以将输入字符串分成 ["1", "1", "1"] 。
 * - 字符串 "1" 不包含前导 0 ，且它是整数 5^0 = 1 的二进制表示。
 * 最少可以将 s 分成 3 个美丽子字符串。
 * 
 * 
 * 示例 3：
 * 
 * 输入：s = "0"
 * 输出：-1
 * 解释：无法将给定字符串分成任何美丽子字符串。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <= 15
 * s[i] 要么是 '0' 要么是 '1' 。
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

const int INF = 1e9;

class Solution {
public:
    int minimumBeautifulSubstrings(string s) {
        int n = s.length();
        vector<string> pow5;
        for (int i = 0; i < 7 ; i ++){
            string str = bitset<32>(pow(5, i)).to_string();
            int pos = str.find_first_not_of('0');
            pow5.push_back(str.substr(pos));

            //cout << pow5.back() << endl;
        }
        function<int(int)> dfs = [&](int i) {
            if (i == n) {
                return 0;
            }
            if (s[i] != '1') {
                return INF;
            }
            int res = INF;
            for (string t : pow5) {
                if (i + t.length() > n) {
                    break;
                }
                if (s.substr(i, t.length()) == t) {
                    res = min(res, dfs(i + t.length()) + 1);
                }
            }
            return res;
        };
        int ans = dfs(0);
        return (ans == INF ? -1 : ans);
    }
};
// @lc code=end



/*
// @lcpr case=start
// "1011"\n
// @lcpr case=end

// @lcpr case=start
// "111"\n
// @lcpr case=end

// @lcpr case=start
// "0"\n
// @lcpr case=end

 */

