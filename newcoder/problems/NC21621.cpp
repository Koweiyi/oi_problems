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
struct wupin
{   
    int t, v;
}a[55];

bool cmp(wupin a, wupin b){
    return a.v > b.v;
}
int  mem[105] = {0};
// int t[55], v[55];  
int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),cin.tie(0);
    int n;
    cin >> n;
    repp(i, 1, n) cin >> a[i].t;
    repp(i, 1, n) cin >> a[i].v;
    sort(a + 1, a + n + 1, cmp);
    int type = 0, s = 0;
    
    repp(i, 1, n){
        if (a[i].v >= 0){
            if(mem[a[i].t] == 0){
                type ++;
                mem[a[i].t] ++;
            }
            s += a[i].v;
        }else{
            if(mem[a[i].t]){
                continue;
            }
            if ((type + 1) * (s + a[i].v)  > type * s){
                mem[a[i].t] ++;
                type ++;
                s += a[i].v;
            }
        }
    }
    cout << type * s;
    return 0;
}

/*
链接：https://ac.nowcoder.com/acm/problem/21621
来源：牛客网

题目描述 
牛牛有最多50个物品，每个物品有一个type标号，并且有一个taste值，现在要求选择若干个物品放进背包使得x * y最大，x为选择的不同type的数量，y为总的taste值之和 
输入描述:
第一行输入一个整数n表示物品的数量(1 ≤ n ≤ 50)

第二行输入 n个整数typei表示每个物品的类型(1 ≤ typei ≤ 100)

第三行输入n个整数tastei(-100000 ≤ tastei ≤ 100000)
输出描述:
输出一个整数
示例1
输入
复制
2
1 2
4 7
输出
复制
22
*/