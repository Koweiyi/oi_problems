/*
 * @lc app=leetcode.cn id=1033 lang=cpp
 * @lcpr version=21907
 *
 * [1033] 移动石子直到连续
 * 
 * 思路：
 * 最少: 如果一开始就全相邻就是0, 
 *      否则如果有相邻两格以内,那么只需要一次移动
 *      都超过两格就是2次了
 * 最多: 最大减去最小再 - 2
 */ 
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
  int solvemin(int a, int b, int c) {
    if (a == b - 1 && c == b + 1)
      return 0;
    if (b - a <= 2 or c - b <= 2)
      return 1;
    return 2;
  }

  vector<int> numMovesStones(int a, int b, int c) {
    int x, y, z;
    x = min(a, min(b, c));
    z = max(a, max(b, c));
    y = a + b + c - x - z;
    int mn = solvemin(x, y, z);
    int mx = z - x - 2;
    return {mn, mx};
  }
};
// @lc code=end

/*
// @lcpr case=start
// 1\n2\n5\n
// @lcpr case=end

// @lcpr case=start
// 4\n3\n2\n
// @lcpr case=end

// @lcpr case=start
// 7\n4\n1\n
// @lcpr case=end

 */

int main() {
  auto res = Solution().numMovesStones(1, 2, 3);
  for (auto &x : res) {
    cout << x << endl;
  }

  return 0;
}
