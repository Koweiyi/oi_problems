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

const int N = 100005;

int a[N], h[N];

int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),std::cin.tie(0);

    int n, m, k;
    cin >> n >> m >> k;
    map<pair<int, int>, int> w; 
    vector<vector<int>> g = vector<vector<int>>(n + 1, vector<int>()); 
    repp(i, 1, n) cin >> a[i];
    repp(i, 1, n) cin >> h[i];

    repp(i, 1, m) {
        int u, v, x;
        cin >> u >> v >> x;
        w[{u,v}] = x;
        w[{v,u}] = x;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    int res = INT_MIN;
    for(int i = 1 ; i < n ; i ++){
        // 枚举能到达的点
     
        // 
        for(int x : g[i]){
            for (int y : g[i]){
                if(x != y && h[i] + h[x] + h[y] + w[{i,x}] + w[{i,y}] <= k){
                    res = max(res, a[i] + a[x] + a[y]);
                }
            }
        }
    }
    cout << res << endl;
    return 0;
}
