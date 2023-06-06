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
ll a[maxn], s[maxn], l[maxn];
int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),std::cin.tie(0);
    int n;
    std::cin >> n;
    repp(i, 1, n) std::cin >> a[i], s[i] = s[i - 1] + a[i];
    stack<int> stk;
    ll res = 0;
    repp(i, 1, n + 1){ // n + 1 是因为要保证所有元素出栈
        while(!stk.empty() && a[i] < a[stk.top()]){
            res = max(res,(s[i - 1] - s[l[stk.top()]]) * a[stk.top()]);
            stk.pop();
        }
        l[i] = stk.empty() ? 0 :stk.top();
        stk.push(i);
    }
    std::cout << res << endl;
    return 0;
}
