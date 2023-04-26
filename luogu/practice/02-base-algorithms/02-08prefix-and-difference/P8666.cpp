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
const int maxn = 1000005;

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

int A, B, C, m, n;
int s[maxn], D[maxn], h[maxn];
int x2[maxn], y2[maxn], z2[maxn];
int x1[maxn], yy1[maxn], z1[maxn];

int num(int x, int y, int z){
    if(x > A || y > B || z > C) return 0;
    return ((x - 1) * B + (y - 1)) * C + (z - 1) + 1;
}

bool check(int x){
    mem(D, 0);
    repp(i, 1, x){
        D[num(x1[i], yy1[i], z1[i])] += h[i];
        D[num(x2[i] + 1, yy1[i], z1[i])] -= h[i];
        D[num(x1[i], y2[i] + 1, z1[i])] -= h[i];
        D[num(x1[i], yy1[i], z2[i] + 1)] -= h[i];
        D[num(x2[i] + 1, y2[i] + 1, z1[i])] += h[i];
        D[num(x2[i] + 1, yy1[i], z2[i] + 1)] += h[i];
        D[num(x1[i], y2[i] + 1, z2[i] + 1)] += h[i];
        D[num(x2[i] + 1, y2[i] + 1, z2[i] + 1)] -= h[i];
    }
    repp(i, 1, A) repp(j, 1, B) repp(k, 1, C)
        D[num(i, j, k + 1)] += D[num(i, j, k)];
    repp(j, 1, B) repp(k, 1, C) repp(i, 1, A) 
        D[num(i + 1, j, k)] += D[num(i, j, k)];
    repp(i, 1, A) repp(k, 1, C) repp(j, 1, B)
        D[num(i, j + 1, k)] += D[num(i, j, k)];
    
    
    repp(i, 1, n) if(D[i] > s[i]) return true;
    return false;
}


int main(int argc, char const *argv[]){
    // ios::sync_with_stdio(0),cin.tie(0);
    cin >> A >> B >> C >> m;
    n = A * B * C;
    repp(i, 1, n) 
        cin >> s[i];
    repp(j, 1, m) 
        scanf("%d%d%d%d%d%d%d", &x1[j], &x2[j], &yy1[j], &y2[j], &z1[j], &z2[j], &h[j]);
    int l = 0, r = m + 1;
    while(l + 1 < r){
        int mid = l + (r - l) / 2;
        if(check(mid)) r = mid;
        else l = mid;
    } 
    cout << r;
    return 0;
}
