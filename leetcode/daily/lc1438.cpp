/*
 * @lc app=leetcode.cn id=1438 lang=cpp
 * @lcpr version=21907
 *
 * [1438] 绝对差不超过限制的最长连续子数组
 *
 * https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
 *
 * algorithms
 * Medium (49.49%)
 * Likes:    310
 * Dislikes: 0
 * Total Accepted:    44.6K
 * Total Submissions: 90.2K
 * Testcase Example:  '[8,2,4,7]\n4'
 *
 * 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于
 * limit 。
 * 
 * 如果不存在满足条件的子数组，则返回 0 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：nums = [8,2,4,7], limit = 4
 * 输出：2 
 * 解释：所有子数组如下：
 * [8] 最大绝对差 |8-8| = 0 <= 4.
 * [8,2] 最大绝对差 |8-2| = 6 > 4. 
 * [8,2,4] 最大绝对差 |8-2| = 6 > 4.
 * [8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
 * [2] 最大绝对差 |2-2| = 0 <= 4.
 * [2,4] 最大绝对差 |2-4| = 2 <= 4.
 * [2,4,7] 最大绝对差 |2-7| = 5 > 4.
 * [4] 最大绝对差 |4-4| = 0 <= 4.
 * [4,7] 最大绝对差 |4-7| = 3 <= 4.
 * [7] 最大绝对差 |7-7| = 0 <= 4. 
 * 因此，满足题意的最长子数组的长度为 2 。
 * 
 * 
 * 示例 2：
 * 
 * 输入：nums = [10,1,2,4,7,2], limit = 5
 * 输出：4 
 * 解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。
 * 
 * 
 * 示例 3：
 * 
 * 输入：nums = [4,2,2,2,4,4,2,2], limit = 0
 * 输出：3
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^9
 * 0 <= limit <= 10^9
 * 思路：单调队列+滑动窗口
 * 
 */
#include<bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    // long long s[100005]; // sum ==> [l, r] = s[r + 1] - s[l]
    int longestSubarray(vector<int>& nums, int limit) {
        // for(int i = 0 ; i < nums.size() ; i ++){
        //     s[i + 1] = s[i] + nums[i];
        // }
        int res = INT_MIN;
        deque<int> mx, mn;
        int l = 0;
        
        for(int i = 0 ; i < nums.size() ; i ++){
            while(!mx.empty() && nums[i] >= nums[mx.back()])
                mx.pop_back();
            mx.push_back(i);
        
            while(!mn.empty() && nums[i] <= nums[mn.back()])
                mn.pop_back();
            mn.push_back(i);
            while(nums[mx.front()] - nums[mn.front()] > limit){
                if (mx.front() == l){
                    mx.pop_front();
                }if(mn.front() == l)
                    mn.pop_front();
                l ++;
            }
            res = max(res, i - l + 1);
        }
        return res;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [8,2,4,7]\n4\n
// @lcpr case=end

// @lcpr case=start
// [10,1,2,4,7,2]\n5\n
// @lcpr case=end

// @lcpr case=start
// [4,2,2,2,4,4,2,2]\n0\n
// @lcpr case=end

 */

