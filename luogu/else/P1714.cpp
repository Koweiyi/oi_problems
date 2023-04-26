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
const int maxn = 1000005;

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
int s[maxn];

int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),cin.tie(0);
    int n, m;
    cin >> n >> m;
    repp(i, 1, n) {
        cin >> s[i];
        s[i] += s[i - 1];
    }
    deque<int> q;
    int res = INT_MIN;
    q.push_back(0);
    repp(i, 1, n){
        while(!q.empty() && q.front() < i - m)q.pop_front();
        if(q.empty()) res = max(res, s[i]);
        else res = max(res, s[i] - s[q.front()]);
        while(!q.empty() && s[i] <= s[q.back()]) q.pop_back();
        q.push_back(i);
     }
     cout << res;
    
    return 0;
}
