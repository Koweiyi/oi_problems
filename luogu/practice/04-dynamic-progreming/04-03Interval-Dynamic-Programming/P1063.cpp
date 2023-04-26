#include<bits/stdc++.h>
#define ll long long int

using namespace std;
const int maxn = 300;

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

ll n;
ll mars[maxn];
ll f[maxn][maxn];

int main(int argc, char const *argv[]){
    n = read();
    for (register int i = 1; i <= n ; i ++){
        mars[i] = read();
        mars[i + n] = mars[i];
    }
    for(int i = 1; i <= 2 * n - 1; i ++)
        f[i][i] = 0;
    for(register int len = 2; len <= n ; len ++){
        for(register int l = 1 ; l + len - 1 <= 2 * n; l ++){
            int r = l + len - 1;
            for(int k = l; k < r; k ++)
                f[l][r] = max(f[l][r], f[l][k] + f[k + 1][r] + mars[l] * mars[k + 1] * (r + 1 <= 2 * n ? mars[r + 1] : mars[1]));
        }
    }   
    ll res = 0;
    for(int i = 1 ; i <= n; i ++)
        res = max(res, f[i][i + n - 1]);
    out(res); 

    return 0;
}
