/*
 * @lc app=leetcode.cn id=974 lang=cpp
 * @lcpr version=21907
 *
 * [974] 和可被 K 整除的子数组
 *
 * https://leetcode.cn/problems/subarray-sums-divisible-by-k/description/
 *
 * algorithms
 * Medium (47.85%)
 * Likes:    438
 * Dislikes: 0
 * Total Accepted:    57.5K
 * Total Submissions: 120.1K
 * Testcase Example:  '[4,5,0,-2,-3,1]\n5'
 *
 * 给定一个整数数组 nums 和一个整数 k ，返回其中元素之和可被 k 整除的（连续、非空） 子数组 的数目。
 * 
 * 子数组 是数组的 连续 部分。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：nums = [4,5,0,-2,-3,1], k = 5
 * 输出：7
 * 解释：
 * 有 7 个子数组满足其元素之和可被 k = 5 整除：
 * [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
 * -3]
 * 
 * 
 * 示例 2:
 * 
 * 输入: nums = [5], k = 9
 * 输出: 0
 * 
 * 
 * 
 * 
 * 提示:
 * 
 * 
 * 1 <= nums.length <= 3 * 10^4
 * -10^4 <= nums[i] <= 10^4
 * 2 <= k <= 10^4
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
    int subarraysDivByK(vector<int>& nums, int k) {
        unordered_map<int, int> up;
        up[0] ++;
        int s = 0;
        int res = 0;
        for(int num : nums){
            s += num;
            res += up[(s % k + k) % k];
            up[(s % k + k) % k] ++;
        }
        return res;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [4,5,0,-2,-3,1]\n5\n
// @lcpr case=end

// @lcpr case=start
// [5]\n9\n
// @lcpr case=end

 */

