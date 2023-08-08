/*
 * @lc app=leetcode.cn id=1419 lang=cpp
 * @lcpr version=21907
 *
 * [1419] 数青蛙
 *
 * https://leetcode.cn/problems/minimum-number-of-frogs-croaking/description/
 *
 * algorithms
 * Medium (49.59%)
 * Likes:    175
 * Dislikes: 0
 * Total Accepted:    27.3K
 * Total Submissions: 55.1K
 * Testcase Example:  '"croakcroak"'
 *
 * 给你一个字符串 croakOfFrogs，它表示不同青蛙发出的蛙鸣声（字符串 "croak" ）的组合。由于同一时间可以有多只青蛙呱呱作响，所以
 * croakOfFrogs 中会混合多个 “croak” 。
 * 
 * 请你返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。
 * 
 * 要想发出蛙鸣 "croak"，青蛙必须 依序 输出 ‘c’, ’r’, ’o’, ’a’, ’k’ 这 5
 * 个字母。如果没有输出全部五个字母，那么它就不会发出声音。如果字符串 croakOfFrogs 不是由若干有效的 "croak" 字符混合而成，请返回
 * -1 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：croakOfFrogs = "croakcroak"
 * 输出：1 
 * 解释：一只青蛙 “呱呱” 两次
 * 
 * 
 * 示例 2：
 * 
 * 输入：croakOfFrogs = "crcoakroak"
 * 输出：2 
 * 解释：最少需要两只青蛙，“呱呱” 声用黑体标注
 * 第一只青蛙 "crcoakroak"
 * 第二只青蛙 "crcoakroak"
 * 
 * 
 * 示例 3：
 * 
 * 输入：croakOfFrogs = "croakcrook"
 * 输出：-1
 * 解释：给出的字符串不是 "croak" 的有效组合。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= croakOfFrogs.length <= 10^5
 * 字符串中的字符只有 'c', 'r', 'o', 'a' 或者 'k'
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
    int minNumberOfFrogs(string croakOfFrogs) {
        // 预处理每个字母在 "croak" 中的上一个字母
        char PREVIOUS['s']; // 's' 保证 "croak" 中的任意字符都不会越界
        const string croak = "croakc";
        for (int i = 1; i < croak.length(); i++)
            PREVIOUS[croak[i]] = croak[i - 1];

        int cnt['s']{};
        for (char ch: croakOfFrogs) {
            char pre = PREVIOUS[ch]; // pre 为 ch 在 "croak" 中的上一个字母
            if (cnt[pre]) // 如果有青蛙发出了 pre 的声音
                cnt[pre]--; // 复用一只
            else if (ch != 'c') // 否则青蛙必须从 'c' 开始蛙鸣
                return -1; // 不符合要求
            cnt[ch]++; // 发出了 ch 的声音
        }
        if (cnt['c'] || cnt['r'] || cnt['o'] || cnt['a'])
            return -1; // 有发出其它声音的青蛙，不符合要求
        return cnt['k']; // 最后青蛙们都发出了 'k' 的声音
    }
};
// @lc code=end



/*
// @lcpr case=start
// "croakcroak"\n
// @lcpr case=end

// @lcpr case=start
// "crcoakroak"\n
// @lcpr case=end

// @lcpr case=start
// "croakcrook"\n
// @lcpr case=end

 */

