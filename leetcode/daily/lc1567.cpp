/*
 * @lc app=leetcode.cn id=1567 lang=cpp
 * @lcpr version=21907
 *
 * [1567] 乘积为正数的最长子数组长度
 *
 * https://leetcode.cn/problems/maximum-length-of-subarray-with-positive-product/description/
 *
 * algorithms
 * Medium (42.61%)
 * Likes:    211
 * Dislikes: 0
 * Total Accepted:    33.8K
 * Total Submissions: 79.4K
 * Testcase Example:  '[1,-2,-3,4]'
 *
 * 给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。
 * 
 * 一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。
 * 
 * 请你返回乘积为正数的最长子数组长度。
 * 
 * 
 * 
 * 示例  1：
 * 
 * 输入：nums = [1,-2,-3,4]
 * 输出：4
 * 解释：数组本身乘积就是正数，值为 24 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：nums = [0,1,-2,-3,-4]
 * 输出：3
 * 解释：最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
 * 注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。
 * 
 * 示例 3：
 * 
 * 输入：nums = [-1,-2,-3,0,1]
 * 输出：2
 * 解释：乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 * 
 * 
 * 
 * 
 */
#include<bits/stdc++.h>
#define ll long long int
#define F(i,n,m) for(int i=n;i<=m;i++)
#define r(i,n) for(int i=0;i<n;i++)
using namespace std;
const int maxn = 100005;
// @lc code=start

class Solution {
public: 
    int getMaxLen(vector<int>& nums) {
        int n = nums.size();
        int res = nums[0] > 0, f0 = nums[0] > 0, f1 = nums[0] < 0; 
        for(int i = 1; i < n ; i ++){
            if (nums[i] > 0){
                f0 ++;
                if(f1) f1++;
            }else if(nums[i] < 0){
                int tmp = f0;
                f0 = f1 ? f1 + 1 : 0;
                f1 = tmp + 1;
            }else{
                f0 = 0;
                f1 = 0;
            }
            res = max(res, f0);
        }   
        return res;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,-2,-3,4]\n
// @lcpr case=end

// @lcpr case=start
// [0,1,-2,-3,-4]\n
// @lcpr case=end

// @lcpr case=start
// [-1,-2,-3,0,1]\n
// @lcpr case=end

 */

