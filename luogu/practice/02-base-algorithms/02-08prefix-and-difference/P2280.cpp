#include<bits/stdc++.h>
#define ll long long int
#define F(i,n,m) for(int i=n;i<=m;i++)
#define r(i,n) for(int i=0;i<n;i++)
using namespace std;
const int maxn = 5005;

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

int g[maxn][maxn];

int main(int argc, char const *argv[])
{
    int n, len;
    n = read();
    len = read();
    r(i, n){
        int x, y, v;
        x = read(), y = read(), v = read();
        g[x + 1][y + 1] = v;
    }   
    F(i, 1, maxn - 1) F(j, 1, maxn - 1)
        g[i][j] +=  g[i - 1][j] + g[i][j - 1] - g[i - 1][j - 1];

    ll res = -INT_MAX;
    for(int i = 0 ; i  + len - 1 < maxn - 1; i ++){
        for(int j = 0 ; j + len - 1 < maxn - 1; j ++ ){
            ll sum = g[i + len][j + len] + g[i][j] - g[i + len][j] - g[i][j + len];
            res = max(res, sum);
        }
    }
    out(res);
    return 0;
}
