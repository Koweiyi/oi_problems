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
#define ull unsigned long long
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

const int N = 1000005;
char s[N];
ull P = 131, p[N],  h[N];

ull get_hash(ull l, ull R){
    return h[R] - h[l - 1] * p[R - l + 1];
}

int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),std::cin.tie(0);
    int n;
    std::cin >> n >> s + 1;
    p[0] = 1;
    repp(i, 1, n) p[i] = p[i - 1] * P;
    repp(i, 1, n) h[i] = h[i - 1] * P + s[i];
    repp(i, 1, n){
        bool f = 1;
        ull a = get_hash(1, i);
        for(int j = 1 ; (j + 1) * i <= n ; j ++){
            if(get_hash(j * i + 1, (j + 1) * i) != a){
                f = 0;
                break;
            }
        }
        if(n % i != 0 and get_hash(1, n % i) != get_hash(n - n % i + 1, n)){
            f = 0;
        }
        if(f){
            std::cout << i << endl;
            break;
        }
    }
    return 0;
}
