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

const int maxn = 10005;
int A[maxn], B[maxn], C[maxn], F[maxn];

int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),std::cin.tie(0);
    int n, m;
    std::cin >> n >> m;
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> q;
    repp(i,1,n){
        std::cin >> A[i] >> B[i] >> C[i];
        F[i] = 1;
        q.push({A[i] + B[i] + C[i], i});
    }
    repp(x,1,m){
        auto p = q.top(); q.pop();
        std::cout << p.first << " ";
        int i = p.second;
        F[i] ++;
        q.push({A[i] * F[i] * F[i] + B[i] * F[i] + C[i], i});
    }
    return 0;
}
