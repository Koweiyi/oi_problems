//https://www.luogu.com.cn/problem/P1996
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

const int maxn = 100005;
struct node{
    int id, next;
}nodes[maxn];


int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),cin.tie(0);
    int n, m;
    n = read(), m = read();
    nodes[0].next = 1;
    repp(i,1,n) {
        nodes[i].id = i;
        nodes[i].next = i + 1;
    }
    nodes[n].next = 1;
    int now = 1, pre = 1;
    while((n--) > 1){
        repp(i,1,m - 1){
            pre = now;
            now = nodes[now].next;
        }
        out(nodes[now].id);
        out(' ');
        nodes[pre].next = nodes[now].next;
        now = nodes[pre].next;
    }
    out(nodes[now].id);
    return 0;
}