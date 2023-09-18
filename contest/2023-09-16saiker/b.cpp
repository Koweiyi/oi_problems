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

const int N = 100005;

int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),std::cin.tie(0);
    int v;
    cin >> v;
    string s;
    cin >> s;
    int cnt1 = 0, cnt2 = 0; 
    ll res = 0;
    for (char ch : s){
        if(ch == '1'){
            cnt1 ++;
        }else{
            cnt2 ++;
        }
        if(cnt1 < v){
            res += cnt1;
            if (cnt1 + 2 * cnt2 <= v){
                res += cnt2;
            }else{
                res += (v - cnt1) / 2;
            }
        }else{
            res += v;
        }
    }
    cout << res << endl;
    return 0;
}