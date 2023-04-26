#include <bits/stdc++.h>
#define mem(a,b) memset(a,b,sizeof a)
#define rep(i,n,m) for(int i=n;i<=m;i++)
#define repp(i,n,m) for(int i=n;i<m;i++)
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

int n, m, res, a[105], sum[(1 << 10)], dp[(1 << 10)][(1 << 10)][3];

int getSum(int x){
    int tot = 0;
    while(x){
        if (x & 1) tot ++;
        x >>= 1;
    }
    return tot;
}

int main(int argc, char const *argv[]){
    // ios::sync_with_stdio(0),cin.tie(0);
    cin >> n >> m;
    char x;
    repp(i, 0, n) repp(j, 0, m)
        cin >> x, a[i] <<= 1, a[i] += (x == 'H'? 1 : 0);
    repp(i, 0, (1 << m)){
        sum[i] = getSum(i);
    }

    repp(i, 0, 1 << m)
        if(!(i&a[0] || (i&(i<<1)) || (i&(i<<2))))
            dp[0][i][0] = sum[i];
    repp(i, 0, 1 << m)
        repp(j, 0, 1 << m)
            if (!(i&j || j&a[1] || i&a[0] || (i&(i<<1)) || (i&(i<<2)) || (j&(j<<1)) || (j&(j<<2))))
                dp[i][j][1] = sum[i] + sum[j];

    repp(i,2,n){
        repp(L,0,1 << m){
            if(L&a[i - 1] || (L&(L<<1)) || (L&(L<<2))) continue;
            repp(S, 0, 1 << m){
                if(S&L || S&a[i] || (S&(S<<1)) || (S&(S<<2))) continue;
                repp(FL, 0, 1 << m){
                    if(FL & S || FL & L || FL & a[i - 2] || (FL&(FL<<1)) || (FL&(FL<<2))) continue;
                    dp[L][S][i%3] = max(dp[FL][L][(i-1)%3] + sum[S], dp[L][S][i%3]);
                }
            }
        }
    }
    repp(L,0,1<<m)
        repp(S,0,1<<m)
            res = max(res, dp[L][S][(n - 1)%3]);
    cout << res;    
    return 0;
}
