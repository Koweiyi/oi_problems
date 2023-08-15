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

const int maxn = 100005;
int sum[maxn], dp[maxn][2];
deque<int> q;

signed main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),cin.tie(0);
    int N, K; 
    cin >> N >> K;
    repp(i, 1, N){
        int a;
        cin >> a;
        sum[i] = sum[i - 1] + a;
    }  
    q.push_back(0);
    repp(i, 1, N){
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]);
        while(!q.empty() && q.front() < i - K){
            q.pop_front();
        }
        dp[i][1] = dp[q.front()][0] + sum[i] - sum[q.front()];
        while(!q.empty() && dp[q.back()][0] - sum[q.back()] < dp[i][0] - sum[i]){
            q.pop_back();
        }
        q.push_back(i);
    }
    cout << max(dp[N][0], dp[N][1]) << endl;
    return 0;
}
