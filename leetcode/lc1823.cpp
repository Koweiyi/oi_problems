/*
 * @lc app=leetcode.cn id=1823 lang=cpp
 * @lcpr version=21907
 *
 * [1823] 找出游戏的获胜者
 *
 * https://leetcode.cn/problems/find-the-winner-of-the-circular-game/description/
 *
 * algorithms
 * Medium (78.62%)
 * Likes:    185
 * Dislikes: 0
 * Total Accepted:    53.3K
 * Total Submissions: 67.8K
 * Testcase Example:  '5\n2'
 *
 * 共有 n 名小伙伴一起做游戏。小伙伴们围成一圈，按 顺时针顺序 从 1 到 n
 * 编号。确切地说，从第 i 名小伙伴顺时针移动一位会到达第 (i+1)
 * 名小伙伴的位置，其中 1 <= i < n ，从第 n 名小伙伴顺时针移动一位会回到第 1
 * 名小伙伴的位置。
 *
 * 游戏遵循如下规则：
 *
 *
 * 从第 1 名小伙伴所在位置 开始 。
 * 沿着顺时针方向数 k 名小伙伴，计数时需要 包含
 * 起始时的那位小伙伴。逐个绕圈进行计数，一些小伙伴可能会被数过不止一次。
 * 你数到的最后一名小伙伴需要离开圈子，并视作输掉游戏。
 * 如果圈子中仍然有不止一名小伙伴，从刚刚输掉的小伙伴的 顺时针下一位 小伙伴
 * 开始，回到步骤 2 继续执行。 否则，圈子中最后一名小伙伴赢得游戏。
 *
 *
 * 给你参与游戏的小伙伴总数 n ，和一个整数 k ，返回游戏的获胜者。
 *
 *
 *
 * 示例 1：
 *
 * 输入：n = 5, k = 2
 * 输出：3
 * 解释：游戏运行步骤如下：
 * 1) 从小伙伴 1 开始。
 * 2) 顺时针数 2 名小伙伴，也就是小伙伴 1 和 2 。
 * 3) 小伙伴 2 离开圈子。下一次从小伙伴 3 开始。
 * 4) 顺时针数 2 名小伙伴，也就是小伙伴 3 和 4 。
 * 5) 小伙伴 4 离开圈子。下一次从小伙伴 5 开始。
 * 6) 顺时针数 2 名小伙伴，也就是小伙伴 5 和 1 。
 * 7) 小伙伴 1 离开圈子。下一次从小伙伴 3 开始。
 * 8) 顺时针数 2 名小伙伴，也就是小伙伴 3 和 5 。
 * 9) 小伙伴 5 离开圈子。只剩下小伙伴 3 。所以小伙伴 3 是游戏的获胜者。
 *
 * 示例 2：
 *
 * 输入：n = 6, k = 5
 * 输出：1
 * 解释：小伙伴离开圈子的顺序：5、4、6、2、3 。小伙伴 1 是游戏的获胜者。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= k <= n <= 500
 *
 *
 *
 *
 * 进阶：你能否使用线性时间复杂度和常数空间复杂度解决此问题？
 *
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start

// 使用链表模拟 时间(nk) 空间O(n)
class Solution1 {
  public:
    int findTheWinner(int n, int k) {
        list<int> node;
        for (int i = 0; i < n; i++)
            node.push_back(i + 1);
        auto it = node.begin();
        while (node.size() > 1) {
            for (int i = 0; i < k - 1; i++) {
                it++;
                if (it == node.end())
                    it = node.begin();
            }
            auto nxt = ++it;
            if (nxt == node.end())
                nxt = node.begin();
            node.erase(--it);
            it = nxt;
        }
        return *it;
    }
};

// 使用队列模拟 时间 O(nk) 空间O(n)
class Solution2 {
  public:
    int findTheWinner(int n, int k) {
        queue<int> q;
        for (int i = 1; i <= n; i++)
            q.push(i);
        while (q.size() > 1) {
            for (int i = 0; i < k - 1; i++) {
                q.push(q.front());
                q.pop();
            }
            q.pop();
        }
        return q.front();
    }
};

// 使用递归 时间O(n), 空间O(n)
// f(n, k) = (f(n - 1, k) + k - 1) % n + 1
class Solution3 {
  public:
    int findTheWinner(int n, int k) {
        if (n == 1)
            return 1;
        return (findTheWinner(n - 1, k) + k - 1) % n + 1;
    }
};

// 将递归转化为递推 O(n)时间, O(1)空间解法
class Solution4 {
  public:
    int findTheWinner(int n, int k) {
        int res = 1;
        for (int i = 2; i <= n; i++) {
            res = (res + k - 1) % i + 1;
        }
        return res;
    }
};
// @lc code=end

/*
// @lcpr case=start
// 5\n2\n
// @lcpr case=end

// @lcpr case=start
// 6\n5\n
// @lcpr case=end

 */

int main() {
    auto res = Solution4().findTheWinner(5, 2);
    cout << res;

    return 0;
}
