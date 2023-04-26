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
const int maxn = 30005;

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

int p[205] = {0};
int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),cin.tie(0);

    int w, n;
    cin >> w >> n;
    int res = 0;
    repp(i, 1, n){
        int x;
        cin >> x;
        p[x] += 1;
    }
    pre(i, w, 1){
        while(p[i]){
            res += 1;
            p[i] -= 1;
            pre(j, w - i, 1){
                if(p[j] > 0){
                    p[j] -= 1;
                    break;
                }
            }
        }
    }
    cout << res;
    return 0;
}
