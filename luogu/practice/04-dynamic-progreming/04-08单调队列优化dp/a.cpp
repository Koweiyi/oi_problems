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
#define int long long
#define endl "\n"
#define pii pair<int,int>
using namespace std;

inline int read(void) {
    int s = 0, w = 1;
    char ch = getchar();
    for(; ch < '0' || ch > '9'; ch = getchar()) if(ch == '-') w = -1;
    for(; ch <= '9' && ch >= '0'; ch = getchar()) s= s * 10 + ch - '0';
    return s * w;
}

inline void out(int a){
    if (a >= 10) out(a / 10);
    putchar(a % 10 + '0');
}

const int maxn = 100005;

int s[maxn], dp[maxn];

signed main(){
    ios::sync_with_stdio(0),cin.tie(0);
    int n, k;
    cin >> n >> k;
    deque<int> q;
    repp(i, 1, n){
        int a; 
        cin >> a;
        s[i] = s[i - 1] + a;
    }
    q.push_back(0);
    repp(i, 1, n){
        while(!q.empty() && q.front() < i - k){
            q.pop_front();
        }
        while (!q.empty() && dp[i - 1] - s[i] > dp[q.back() - 1] - s[q.back()]){
            q.pop_back();
        }

        q.push_back(i);
        dp[i] = dp[q.front() - 1] - s[q.front()] + s[i];
    }
    cout << dp[n] << endl;

    return 0;
}

// dp[i]表示前i个奶牛的最大贡献值
/**
 * 
 * dp[i] = max(dp[j - 1] + s[i] - s[j])  i - k <= j <= i
 * dp[i] = max(dp[j - 1] - s[j]) + s[i] i - k <= j <= i
*/ 
