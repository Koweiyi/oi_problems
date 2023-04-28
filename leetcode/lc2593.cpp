/*
 * @Author: Koweiyi 1423376854@qq.com
 * @Date: 2023-04-28 21:03:06
 * @LastEditors: Koweiyi 1423376854@qq.com
 * @LastEditTime: 2023-04-28 21:41:34
 * @FilePath: \oi_problems\leetcode\lc2593.cpp
 * @Description:
 *
 * Copyright (c) 2023 by ${git_name_email}, All Rights Reserved.
 */
/*
 * @lc app=leetcode.cn id=2593 lang=cpp
 * @lcpr version=21907
 *
 * [2593] 标记所有元素后数组的分数
 *
 * https://leetcode.cn/problems/find-score-of-an-array-after-marking-all-elements/description/
 *
 * algorithms
 * Medium (51.64%)
 * Likes:    6
 * Dislikes: 0
 * Total Accepted:    3.9K
 * Total Submissions: 7.5K
 * Testcase Example:  '[2,1,3,4,5,2]'
 *
 * 给你一个数组 nums ，它包含若干正整数。
 *
 * 一开始分数 score = 0 ，请你按照下面算法求出最后分数：
 *
 *
 * 从数组中选择最小且没有被标记的整数。如果有相等元素，选择下标最小的一个。
 * 将选中的整数加到 score 中。
 * 标记 被选中元素，如果有相邻元素，则同时标记 与它相邻的两个元素 。
 * 重复此过程直到数组中所有元素都被标记。
 *
 *
 * 请你返回执行上述算法后最后的分数。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums = [2,1,3,4,5,2]
 * 输出：7
 * 解释：我们按照如下步骤标记元素：
 * - 1 是最小未标记元素，所以标记它和相邻两个元素：[2,1,3,4,5,2] 。
 * - 2 是最小未标记元素，所以标记它和左边相邻元素：[2,1,3,4,5,2] 。
 * - 4 是仅剩唯一未标记的元素，所以我们标记它：[2,1,3,4,5,2] 。
 * 总得分为 1 + 2 + 4 = 7 。
 *
 *
 * 示例 2：
 *
 * 输入：nums = [2,3,5,1,3,2]
 * 输出：5
 * 解释：我们按照如下步骤标记元素：
 * - 1 是最小未标记元素，所以标记它和相邻两个元素：[2,3,5,1,3,2] 。
 * - 2 是最小未标记元素，由于有两个 2 ，我们选择最左边的一个 2 ，也就是下标为 0 处的 2 ，以及它右边相邻的元素：[2,3,5,1,3,2]
 * 。
 * - 2 是仅剩唯一未标记的元素，所以我们标记它：[2,3,5,1,3,2] 。
 * 总得分为 1 + 2 + 2 = 5 。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^6
 *
 *
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
struct p
{
    int val;
    int idx;
    p(int val, int idx) : val(val), idx(idx) {}
    bool operator<(const p &a) const
    {
        if(val == a.val)return idx > a.idx;
        return val > a.val;
    }
};
class Solution
{
public:
    priority_queue<p> pq;
    long long findScore(vector<int> &nums)
    {
        long long ans = 0;
        for (int i = 0; i < nums.size(); i++)
            pq.push(p(nums[i], i));
            
        unordered_set<int> s;
        while (!pq.empty())
        {
            p x = pq.top();
            pq.pop();
            if (s.count(x.idx))
                continue;
            ans += x.val;
            s.insert(x.idx);
            s.insert(x.idx + 1);
            s.insert(x.idx - 1);
        }
        return ans;
    }
};
// @lc code=end

/*
// @lcpr case=start
// [2,1,3,4,5,2]\n
// @lcpr case=end

// @lcpr case=start
// [2,3,5,1,3,2]\n
// @lcpr case=end

 */
