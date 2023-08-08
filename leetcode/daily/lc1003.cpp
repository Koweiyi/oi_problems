/*
 * @lc app=leetcode.cn id=1003 lang=cpp
 * @lcpr version=21907
 *
 * [1003] 检查替换后的词是否有效
 *
 * https://leetcode.cn/problems/check-if-word-is-valid-after-substitutions/description/
 *
 * algorithms
 * Medium (58.48%)
 * Likes:    79
 * Dislikes: 0
 * Total Accepted:    17.1K
 * Total Submissions: 28.9K
 * Testcase Example:  '"aabcbc"'
 *
 * 给你一个字符串 s ，请你判断它是否 有效 。
 * 字符串 s 有效 需要满足：假设开始有一个空字符串 t = "" ，你可以执行 任意次 下述操作将 t 转换为 s ：
 * 
 * 
 * 将字符串 "abc" 插入到 t 中的任意位置。形式上，t 变为 tleft + "abc" + tright，其中 t == tleft +
 * tright 。注意，tleft 和 tright 可能为 空 。
 * 
 * 
 * 如果字符串 s 有效，则返回 true；否则，返回 false。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：s = "aabcbc"
 * 输出：true
 * 解释：
 * "" -> "abc" -> "aabcbc"
 * 因此，"aabcbc" 有效。
 * 
 * 示例 2：
 * 
 * 输入：s = "abcabcababcc"
 * 输出：true
 * 解释：
 * "" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
 * 因此，"abcabcababcc" 有效。
 * 
 * 示例 3：
 * 
 * 输入：s = "abccba"
 * 输出：false
 * 解释：执行操作无法得到 "abccba" 。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <= 2 * 10^4
 * s 由字母 'a'、'b' 和 'c' 组成
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
public:
    bool isValid(string s) {
        stack<int> stk;
        for(int i = 0 ; i < s.size() ; i ++){
            char x = s[i];
            if(x == 'c'){
                if(stk.size() < 2)
                    return false;
                if(stk.top() != 'b')
                    return false;
                stk.pop();
                if(stk.top() != 'a')
                    return false;
                stk.pop();
            }
            else
                stk.push(x);
        
        }
        return stk.empty();
    }
};
// @lc code=end



/*
// @lcpr case=start
// "aabcbc"\n
// @lcpr case=end

// @lcpr case=start
// "abcabcababcc"\n
// @lcpr case=end

// @lcpr case=start
// "abccba"\n
// @lcpr case=end

 */

