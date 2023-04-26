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



int n, sum;
int pc[20], res[20];
int visited[20] = {0};

int dfs(int t, int num, int s){
    if(s > sum) return 0;
    if(t == n){
        if(s == sum){
            res[t] = num;
            return 1;
        }
        else
            return 0;
    }
    visited[num] = 1;
    repp(i, 1, n){
        if(!visited[i] && dfs(t + 1, i, s + pc[t] * i)){
            res[t] = num;
            return 1;
        }
    }
    visited[num] = 0;
    return 0;
    
}
int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),cin.tie(0);
    cin >> n >> sum;
    pc[0] = pc[n - 1] = 1;
    if(n > 1)repp(i, 1, n / 2)pc[i] = pc[n - i - 1] = (n - i) * pc[i - 1] / i;
    if(dfs(0, 0, 0)){
        repp(i, 1, n)cout << res[i] << " ";
    }
    return 0;
}
