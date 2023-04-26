#include<bits/stdc++.h>
#define ll long long int
#define F(i,n,m) for(int i=n;i<=m;i++)
#define r(i,n) for(int i=0;i<n;i++)
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
int n;
int a[maxn];
// 快读优化 66ms 

// cin cout 274 ms

int main(int argc, char const *argv[])
{
    cin >> n;
    F(i, 1, n)
        cin >> a[i];
    ll p = 0, q = 0;
    F(i, 2, n){
        ll d = a[i] - a[i - 1];
        if (d > 0)
            p += d;
        else
            q -= d;
    }
    cout << max(p, q) << endl;
    cout << abs(p - q) + 1;
    return 0;
}
