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


int n, c, x[maxn];

bool work(int mid){
    int cnt = 1, cur = 1;
    repp(i, 2, n){
        if (x[i] - x[cur]>= mid){
            cnt ++;
            cur = i;
        }
    }
    return cnt >= c;
}
int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),cin.tie(0);
    cin >> n >> c;
    repp(i, 1, n)cin >> x[i];
    sort(x + 1, x + n + 1);
    int l = 0, r = x[n] - x[1] + 1;
    while(l + 1 < r){
        int mid = l + (r - l) / 2;
        if(!work(mid))r = mid;
        else l = mid;
    }
    cout << l;
    return 0;
}
