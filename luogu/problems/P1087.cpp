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

char s[maxn];
string m = "BIF";
string res;
int dfs(int i, int j){
    if (i == j){
        res.push_back(m[s[i] - '0']);
        return s[i] - '0';
    }
    int mid =  (i + j) / 2;
    int l = dfs(i, mid);
    int r = dfs(mid + 1, j);
    if(l == 2 || r == 2 || l != r){
        res.push_back('F');
        return 2;
    }else{
        res.push_back(m[l]);
        return l;
    }

}

int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),cin.tie(0);
    int n;
    cin >> n;
    repp(i,1,(1 << n)){
        cin >> s[i];
    }
    dfs(1, (1 << n));
    cout << res;
    return 0;
}
