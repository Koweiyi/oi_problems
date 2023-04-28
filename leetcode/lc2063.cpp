/*
 * @lc app=leetcode.cn id=2063 lang=cpp
 * @lcpr version=21907
 *
 * [2063] 所有子字符串中的元音
 *
 * https://leetcode.cn/problems/vowels-of-all-substrings/description/
 *
 * algorithms
 * Medium (51.25%)
 * Likes:    28
 * Dislikes: 0
 * Total Accepted:    6.6K
 * Total Submissions: 12.9K
 * Testcase Example:  '"aba"'
 *
 * 给你一个字符串 word ，返回 word 的所有子字符串中 元音的总数 ，元音是指 'a'、'e'、'i'、'o' 和 'u' 。
 * 
 * 子字符串 是字符串中一个连续（非空）的字符序列。
 * 
 * 注意：由于对 word 长度的限制比较宽松，答案可能超过有符号 32 位整数的范围。计算时需当心。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：word = "aba"
 * 输出：6
 * 解释：
 * 所有子字符串是："a"、"ab"、"aba"、"b"、"ba" 和 "a" 。
 * - "b" 中有 0 个元音
 * - "a"、"ab"、"ba" 和 "a" 每个都有 1 个元音
 * - "aba" 中有 2 个元音
 * 因此，元音总数 = 0 + 1 + 1 + 1 + 1 + 2 = 6 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：word = "abc"
 * 输出：3
 * 解释：
 * 所有子字符串是："a"、"ab"、"abc"、"b"、"bc" 和 "c" 。
 * - "a"、"ab" 和 "abc" 每个都有 1 个元音
 * - "b"、"bc" 和 "c" 每个都有 0 个元音
 * 因此，元音总数 = 1 + 1 + 1 + 0 + 0 + 0 = 3 。
 * 
 * 示例 3：
 * 
 * 输入：word = "ltcd"
 * 输出：0
 * 解释："ltcd" 的子字符串均不含元音。
 * 
 * 示例 4：
 * 
 * 输入：word = "noosabasboosa"
 * 输出：237
 * 解释：所有子字符串中共有 237 个元音。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= word.length <= 10^5
 * word 由小写英文字母组成
 * 
 * 
 */
#include<bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    bool check(char c){
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
    long long countVowels(string word) {

        long long res = 0;
        for(int i = 0 ; i < word.size() ; i ++){
            if(check(word[i])){
                res += (i + 1) * (word.size() - i);
            }
        }
        return res;
        
    }
};
// @lc code=end



/*
// @lcpr case=start
// "aba"\n
// @lcpr case=end

// @lcpr case=start
// "abc"\n
// @lcpr case=end

// @lcpr case=start
// "ltcd"\n
// @lcpr case=end

// @lcpr case=start
// "noosabasboosa"\n
// @lcpr case=end

 */

