/*
 * @lc app=leetcode.cn id=31 lang=cpp
 * @lcpr version=21913
 *
 * [31] 下一个排列
 *
 * https://leetcode.cn/problems/next-permutation/description/
 *
 * algorithms
 * Medium (38.42%)
 * Likes:    2290
 * Dislikes: 0
 * Total Accepted:    449K
 * Total Submissions: 1.2M
 * Testcase Example:  '[1,2,3]'
 *
 * 整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
 * 
 * 
 * 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
 * 
 * 
 * 整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列
 * 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
 * 
 * 
 * 例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
 * 类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
 * 而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
 * 
 * 
 * 给你一个整数数组 nums ，找出 nums 的下一个排列。
 * 
 * 必须 原地 修改，只允许使用额外常数空间。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：nums = [1,2,3]
 * 输出：[1,3,2]
 * 
 * 
 * 示例 2：
 * 
 * 输入：nums = [3,2,1]
 * 输出：[1,2,3]
 * 
 * 
 * 示例 3：
 * 
 * 输入：nums = [1,1,5]
 * 输出：[1,5,1]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length <= 100
 * 0 <= nums[i] <= 100
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
    void nextPermutation(vector<int>& nums) {
        // 库函数泰裤啦
        // next_permutation(nums.begin(), nums.end());
        // 思路是从后往前找(i, j) 要求满足nums[i] < nums[j] 则有[j, nums.end) 递减找到
        // 然后从后往前找 k .满足nums[k] > nums[i] swap(nums[i], nums[k])
        // 此时[j, nums.end) 依旧是逆序的， 将这一部分逆置就OK啦。
        int i = nums.size() - 2, j = nums.size() - 1;
        while(i >= 0  && nums[i] >= nums[j]){
            i --;
            j --;
        }
        if (i < 0){
            for (int k = 0 ; k < nums.size() / 2 ; k ++)
                swap(nums[k], nums[nums.size() - k - 1]);
        }else{
            // [j, end)一定严格递减
            for (int k = nums.size() - 1 ; k > i ; k -- ){
                if (nums[k] > nums[i]){
                    swap(nums[k], nums[i]);
                    // 逆置[j, end)
                    for(int k = j ; k < nums.size() - 1 + j - k ; k ++ ){
                        swap(nums[k], nums[nums.size() + j - 1 - k]);
                    }
                    break;
                }
            } 
        }
        return ;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,3,2]\n
// @lcpr case=end

// @lcpr case=start
// [3,2,1]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,5]\n
// @lcpr case=end

// @lcpr case=start
// [1,2]\n
// @lcpr case=end
 */

