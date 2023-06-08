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
const int maxn = 10005;
string s;
ull BKDRHash(string s){
    ull P = 131, H = 0;
    rep(i,0,s.size()){
        H = H * P + (s[i] - 'a');
    }
    return H;
}
ull a[maxn];
int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),std::cin.tie(0);
    int n;std::cin >> n;
    repp(i, 1, n){
        std::cin >> s;
        a[i] = BKDRHash(s);
    }
    int res = 0;
    sort(a + 1, a + n + 1);
    repp(i, 1, n){
        if (a[i] != a[i + 1]) res ++;
    }
    std::cout << res;
    return 0;
}
