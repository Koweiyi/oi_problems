/*
 * @lc app=leetcode.cn id=970 lang=cpp
 * @lcpr version=21907
 *
 * [970] 强整数
 *
 * https://leetcode.cn/problems/powerful-integers/description/
 *
 * algorithms
 * Medium (44.67%)
 * Likes:    79
 * Dislikes: 0
 * Total Accepted:    20.9K
 * Total Submissions: 46.8K
 * Testcase Example:  '2\n3\n10'
 *
 * 给定三个整数 x 、 y 和 bound ，返回
 * 值小于或等于 bound 的所有 强整数 组成的列表 。
 *
 * 如果某一整数可以表示为 x^i + y^j ，其中整数 i >= 0 且 j >=
 * 0，那么我们认为该整数是一个 强整数 。
 *
 * 你可以按 任何顺序 返回答案。在你的回答中，每个值 最多 出现一次。
 *
 *
 *
 * 示例 1：
 *
 * 输入：x = 2, y = 3, bound = 10
 * 输出：[2,3,4,5,7,9,10]
 * 解释：
 * 2 = 2^0 + 3^0
 * 3 = 2^1 + 3^0
 * 4 = 2^0 + 3^1
 * 5 = 2^1 + 3^1
 * 7 = 2^2 + 3^1
 * 9 = 2^3 + 3^0
 * 10 = 2^0 + 3^2
 *
 * 示例 2：
 *
 * 输入：x = 3, y = 5, bound = 15
 * 输出：[2,4,6,8,10,14]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= x, y <= 100
 * 0 <= bound <= 10^6
 *
 *
 */
#include <bits/stdc++.h>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right)
        : val(x), left(left), right(right) {}
};
// @lc code=start
class Solution {
  public:
    vector<int> powerfulIntegers(int x, int y, int bound) {

        vector<int> res;
        set<int> s;
        if (bound <= 1)
            return res;

        if (x == 1 && y == 1) {
            res.push_back(2);
            return res;
        }

        if (x == 1 or y == 1) {
            y = max(x, y);
            int i = 0;
            while ((int)pow(y, i) + 1 <= bound) {
                res.push_back((int)pow(y, i++) + 1);
            }
            return res;
        }

        int i = 0;
        while ((int)pow(x, i) + 1<= bound) {
            int pre = (int)pow(x, i);
           
            int j = 0;
            while ((int)pow(y, j) + pre <= bound) {
                int x = (int) pow(y, j ++) + pre;
                if(s.count(x)) continue;
                res.push_back(x);
                s.insert(x);

            }
            i ++;
        }
        return res;
    }
};
// @lc code=end

/*
// @lcpr case=start
// 2\n3\n10\n
// @lcpr case=end

// @lcpr case=start
// 3\n5\n15\n
// @lcpr case=end
 */

// @lcpr case=start
// 2\n1\n10\n
// @lcpr case=end