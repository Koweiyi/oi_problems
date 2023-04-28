#include <bits/stdc++.h>
#define mem(a,b) memset(a,b,sizeof a)
#define rep(i,n,m) for(int i=n;i<m;i++)
#define repp(i,n,m) for(int i=n;i<=m;i++)
#define pre(i,n,m) for(int i=n;i>=m;i--)
#define len(x) (int) (x).size()
#define all(x) (x).begin(), (x).end()
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) a/gcd(a,b)*b
#define ft first
#define sd second
#define PI acos(-1.0)
#define INF 0x3f3f3f3f
#define ll long long
#define endl "\n"
#define pii pair<int,int>
using namespace std;
const int maxn = 100005;

inline ll read(void) {
    int s = 0, w = 1;
    char ch = getchar();
    for(; ch < '0' || ch > '9'; ch = getchar()) if(ch == '-') w = -1;
    for(; ch <= '9' && ch >= '0'; ch = getchar()) s= s * 10 + ch - '0';
    return s * w;
}

inline void out(ll a){
    if (a >= 10) out(a / 10);
    putchar(a % 10 + '0');
}


/**
 * 链接：https://ac.nowcoder.com/acm/problem/21669
来源：牛客网

题目描述 
给你一个网格，有些点被#覆盖了不能再走，其他点是空地，现在牛牛和牛妹轮流开始将空地变成#
如果当前轮到的人操作之后左上角到右下角不存在通路了，当前操作的人就输了
通路只能是从左上角到右下角往右或者往下走的路径
牛牛先开始操作，如果双方都是绝顶聪明，输出最后谁赢

保证一开始给你的网格是存在一条左上角到右下角的通路的，当然，左上角与右下角都是空地。
输入描述:
第一行输入两个整数n,m(2≤ n,m ≤ 20)

接下来n行每行输入m个字符用来描述网格
输出描述:
输出赢的人的名字，"niuniu" 或者 "niumei"
示例1
输入
复制
2 2
..
..
输出
复制
niuniu

思路：考虑只有一条必要通路的情况外，有多少额外'.',
额外空地数量为奇数，niuniu胜，否则niumei胜。
*/

int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),cin.tie(0);
    int n, m;
    cin >> n >> m;
    char c;
    int cnt = 0;
    repp(i, 1, m * n){
        cin >> c;
        if(c == '.')
            cnt ++;
    }
    cnt -= m + n - 1;
    if(cnt & 1)
        cout << "niuniu" << endl;
    else cout << "niumei" << endl;
    return 0;
}
