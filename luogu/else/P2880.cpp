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

int n, q, h[maxn],st_max[maxn][20], st_min[maxn][20];

void init(){
    repp(i, 1, n){
        st_max[i][0] = h[i];
        st_min[i][0] = h[i];
    }
    repp(i, 1, log2(n)){
        for(int s = 1 ; s + (1 << i) - 1 <= n; s ++){
            st_max[s][i] = max(st_max[s][i - 1], st_max[s + (1 << (i - 1))][i - 1]);
            st_min[s][i] = min(st_min[s][i - 1], st_min[s + (1 << (i - 1))][i - 1]);
        }
    }
}

int solve(int L, int R){
    int k = log2(R - L + 1);
    int x = max(st_max[L][k], st_max[R - (1 << k) + 1][k]);
    int y = min(st_min[L][k], st_min[R - (1 << k) + 1][k]);
    return x - y;
}

int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),cin.tie(0);
    cin >> n >> q;
    repp(i, 1, n) cin >> h[i];
    init();
    repp(i, 1, q){
        int a, b;
        cin >> a >> b;
        cout << solve(a, b) << endl;
    }
    
    return 0;
}
