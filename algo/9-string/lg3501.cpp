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
#define ull unsigned long long 
const int N = 500005;
ll res = 0;
ull P[N], f[N],g[N];
int n, PP = 131;
char s[N], t[N];

void bin_search(int x){
    int l = 0, r = min(x, n - x) + 1;
    while(l + 1 < r){
        int mid = (l + r) >> 1;
        if((ull)(f[x] - f[x - mid] *P[mid]) == (ull)(g[x + 1] - g[x + 1 + mid] * P[mid]))
            l = mid;
        else r = mid;
    } 
    res += l;
}

int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),std::cin.tie(0);
    std::cin >> n;
    std::cin >> s + 1;
    P[0] = 1;
    repp(i, 1, n) P[i] = P[i - 1] * PP;
    repp(i, 1, n) t[i] = s[i] == '1' ? '0' : '1';
    repp(i, 1, n) f[i] = f[i - 1] * PP + s[i];
    pre(i, n, 1) g[i] = g[i + 1] * PP + t[i];
    repp(i, 1, n) bin_search(i);
    std::cout << res;
    return 0; 
}
