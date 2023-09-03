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
const int maxn = 400005;

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

struct warrior{
    int id, L, R;
    bool operator < (const warrior b){return L < b.L;}
}w[maxn * 2];


int n, m, n2, st[maxn][20], res[maxn];
void init(){
    int nxt = 1;
    repp(i, 1, n2){
        while(nxt <= n2 && w[nxt].L <= w[i].R) nxt ++;
        st[i][0] = nxt - 1;
    }
    repp(i, 1, log2(n)) repp(s, 1, n2)
        st[s][i] = st[st[s][i - 1]][i - 1];
        
}

void solve(int x){
    int len = w[x].L + m, cur = x, ans = 2;
    pre(i, log2(maxn), 0){
        int pos = st[cur][i];
        if(pos && w[pos].R < len){
            ans += 1 << i;
            cur = pos;
        }
    }
    res[w[x].id] = ans;
}

int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),cin.tie(0);
    cin >> n >> m;
    repp(i, 1, n){
        w[i].id = i;
        cin >> w[i].L >> w[i].R;
        if(w[i].R < w[i].L) w[i].R += m;
    }
    sort(w + 1, w + n + 1);
    n2 = n;
    repp(i,1,n){
        w[++n2] = w[i];
        w[n2].L += m;
        w[n2].R += m;
    }
    init();
    repp(i, 1, n) solve(i);
    repp(i, 1, n) cout << res[i] << " ";
    return 0;
}
