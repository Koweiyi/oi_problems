///
///@file P1219.cpp
///@author Koweiyi (kkweiyi@gmail.com)
///@brief
///@version 0.1
///@date 2023-04-30 01:42:51
///
///@copyright Copyright (c) 2023 Koweiyi
///@deprecated 八皇后问题，输入的是一个整数n，代表n*n棋盘大小
///

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

inline ll read(void) {
    int s = 0, w = 1;
    char ch = getchar();
    for (; ch < '0' || ch > '9'; ch = getchar())
        if (ch == '-')
            w = -1;
    for (; ch <= '9' && ch >= '0'; ch = getchar())
        s = s * 10 + ch - '0';
    return s * w;
}

inline void out(ll a) {
    if (a >= 10)
        out(a / 10);
    putchar(a % 10 + '0');
}

const int maxn = 100005;

int col[15]; // 某列是否放过棋子
int sum[30]; // 某反对角线是否放过棋子
int diff[30]; // 某对角线是否放过棋子
int n, cnt = 0; //n: 棋盘大小, cnt: 总的摆放数量
vector<int> path;
void dfs(int c, vector<int> &path) {
    if (c == n + 1) {
        cnt++;
        if (cnt <= 3) {
            // 打印前三种摆放方式
            rep(i, 0, n) {
                cout << path[i] << " ";
                if (i == n - 1)
                    cout << endl;
            }
        }
        return;
    }
    repp(i, 1, n) {
        if (!col[i] && !sum[i + c] && !diff[i - c + n]) {
            path.push_back(i);
            col[i] = 1;
            sum[i + c] = 1;
            diff[i - c + n] = 1;
            dfs(c + 1, path);
            // 回溯
            col[i] = 0;
            sum[i + c] = 0;
            diff[i - c + n] = 0;
            path.pop_back();
        }
    }
}

int main(int argc, char const *argv[]) {
    ios::sync_with_stdio(0), cin.tie(0);
    cin >> n;
    dfs(1, path);
    cout << cnt << endl;
    return 0;
}
