/*
 * @lc app=leetcode.cn id=2416 lang=cpp
 * @lcpr version=21913
 *
 * [2416] 字符串的前缀分数和
 *
 * https://leetcode.cn/problems/sum-of-prefix-scores-of-strings/description/
 *
 * algorithms
 * Hard (40.74%)
 * Likes:    39
 * Dislikes: 0
 * Total Accepted:    9.1K
 * Total Submissions: 22.4K
 * Testcase Example:  '["abc","ab","bc","b"]'
 *
 * 给你一个长度为 n 的数组 words ，该数组由 非空 字符串组成。
 * 
 * 定义字符串 word 的 分数 等于以 word 作为 前缀 的 words[i] 的数目。
 * 
 * 
 * 例如，如果 words = ["a", "ab", "abc", "cab"] ，那么 "ab" 的分数是 2 ，因为 "ab" 是 "ab" 和
 * "abc" 的一个前缀。
 * 
 * 
 * 返回一个长度为 n 的数组 answer ，其中 answer[i] 是 words[i] 的每个非空前缀的分数 总和 。
 * 
 * 注意：字符串视作它自身的一个前缀。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：words = ["abc","ab","bc","b"]
 * 输出：[5,4,3,2]
 * 解释：对应每个字符串的答案如下：
 * - "abc" 有 3 个前缀："a"、"ab" 和 "abc" 。
 * - 2 个字符串的前缀为 "a" ，2 个字符串的前缀为 "ab" ，1 个字符串的前缀为 "abc" 。
 * 总计 answer[0] = 2 + 2 + 1 = 5 。
 * - "ab" 有 2 个前缀："a" 和 "ab" 。
 * - 2 个字符串的前缀为 "a" ，2 个字符串的前缀为 "ab" 。
 * 总计 answer[1] = 2 + 2 = 4 。
 * - "bc" 有 2 个前缀："b" 和 "bc" 。
 * - 2 个字符串的前缀为 "b" ，1 个字符串的前缀为 "bc" 。 
 * 总计 answer[2] = 2 + 1 = 3 。
 * - "b" 有 1 个前缀："b"。
 * - 2 个字符串的前缀为 "b" 。
 * 总计 answer[3] = 2 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：words = ["abcd"]
 * 输出：[4]
 * 解释：
 * "abcd" 有 4 个前缀 "a"、"ab"、"abc" 和 "abcd"。
 * 每个前缀的分数都是 1 ，总计 answer[0] = 1 + 1 + 1 + 1 = 4 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= words.length <= 1000
 * 1 <= words[i].length <= 1000
 * words[i] 由小写英文字母组成
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
struct TrieNode {
    unordered_map<char, TrieNode*> children;
    int score;
    bool  isEndOfWord;

    TrieNode() {
        score = 0;
        isEndOfWord = false;
    }
};
class Trie {
private:
    TrieNode* root;

public:
    Trie() {
        root = new TrieNode();
    }

    // 向Trie中插入一个单词
    void insert(string word) {
        TrieNode* curr = root;
        for (char c : word) {
            if (curr->children.find(c) == curr->children.end()) {
                curr->children[c] = new TrieNode();
            }
            curr = curr->children[c];
            curr->score ++;
        }
        curr->isEndOfWord = true;
    }

    // 搜索一个单词是否在Trie中
    int search(string word) {
        TrieNode* curr = root;
        int res = 0;
        for (char c : word) {
            if (curr->children.find(c) == curr->children.end()) {
                return false;
            }
            curr = curr->children[c];
            res += curr->score;
        }
        return res;
    }

    // 判断一个前缀是否存在于Trie中
    bool startsWith(string prefix) {
        TrieNode* curr = root;
        for (char c : prefix) {
            if (curr->children.find(c) == curr->children.end()) {
                return false;
            }
            curr = curr->children[c];
        }
        return true;
    }
};


class Solution {
public:

    vector<int> sumPrefixScores(vector<string>& words) {
        Trie t = Trie();
        for (auto& s : words){
            t.insert(s);
        }
        vector<int> res;
        for (auto& s : words){
            res.push_back(t.search(s));
        }
        return res;
    }
};
// @lc code=end



/*
// @lcpr case=start
// ["abc","ab","bc","b"]\n
// @lcpr case=end

// @lcpr case=start
// ["abcd"]\n
// @lcpr case=end

 */

