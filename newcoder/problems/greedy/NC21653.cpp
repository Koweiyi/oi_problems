#include <bits/stdc++.h>
#define mem(a, b) memset(a, b, sizeof a)
#define rep(i, n, m) for (int i = n; i < m; i++)
#define repp(i, n, m) for (int i = n; i <= m; i++)
#define pre(i, n, m) for (int i = n; i >= m; i--)
#define len(x) (int)(x).size()
#define all(x) (x).begin(), (x).end()
#define gcd(a, b) __gcd(a, b)
#define lcm(a, b) a / gcd(a, b) * b
#define ft first
#define sd second
#define PI acos(-1.0)
#define INF 0x3f3f3f3f
#define ll long long
#define endl "\n"
#define pii pair<int, int>
using namespace std;
const int maxn = 100005;

inline ll read(void)
{
    int s = 0, w = 1;
    char ch = getchar();
    for (; ch < '0' || ch > '9'; ch = getchar())
        if (ch == '-')
            w = -1;
    for (; ch <= '9' && ch >= '0'; ch = getchar())
        s = s * 10 + ch - '0';
    return s * w;
}

inline void out(ll a)
{
    if (a >= 10)
        out(a / 10);
    putchar(a % 10 + '0');
}

/**
// 链接：https://ac.nowcoder.com/acm/problem/21653
// 来源：牛客网
// 题目描述
// 有一个n行数字迷宫，每行都有无穷多个数，问你从起点走到终点经过的数字和的最小
// 值，包括起点终点上面的数字。
// 每一次可以走上下左右相邻的任意一个格子
// 这个数字迷宫比较特殊，每一列都是一模一样的。
// 现在给你一个数组a,a[i] 表示第i行的数字是什么
// 再给你sx,sy, ex,sy分别表示起点与终点

// 输入描述:
// 第一行输入一个整数n,sx,sy,ex,ey表示行数与起点终点
// 第二行输入n个数表示每一行的数字
// 1<=n<=50, 1<=a[i]<=1000
// 0<=sx,ex<=n-1, 0<=sy,ey<=109

// 输出描述:
// 输出一个整数

// 示例1
// 输入
// 3 2 0 2 2
// 5 3 10
// 输出
// 29
*/

/**
 * 思路：最终一定横向都是在某一行中行进，因为只有50行，模拟就行了，
 * 教训：wa一次，不开long long见祖宗，列数最大1e9,所以答案可能超int 范围;
 */

ll c[55];
ll sum[55];
int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(0), cin.tie(0);
    int n, sx, sy, ex, ey;
    cin >> n >> sx >> sy >> ex >> ey;
    sx++;
    sy++;
    ex++;
    ey++;
    repp(i, 1, n)
    {
        cin >> c[i];
        sum[i] = c[i] + sum[i - 1];
    }
    if (sx > ex)
        swap(sx, ex);
    if (sy > ey)
        swap(sy, ey);
    if (sy == ey)
    {
        cout << sum[ex] - sum[sx - 1] << endl;
        return 0;
    }
    ll res = LONG_LONG_MAX;
    repp(i, 1, n)
    {
        if (i < sx)
        {
            res = min(res, sum[sx] - sum[i - 1] + sum[ex] - sum[i - 1] + c[i] * (ey - sy - 1));
        }
        else if (i > ex)
        {
            res = min(res, 2 * sum[i] - sum[ex - 1] - sum[sx - 1] + c[i] * (ey - sy - 1));
        }
        else
        {
            res = min(res, sum[ex] - sum[sx - 1] + c[i] * (ey - sy));
        }
    }
    cout << res << endl;
    return 0;
}
