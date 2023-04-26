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

int a[105];
int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),cin.tie(0);
    int n;
    cin >> n;
    bool flag = false;
    pre(i, n, 0) cin >> a[i];
    pre(i, n, 1){
        if(a[i] != 0){
            flag = true;
            if(a[i] == 1){
                if(i != n) 
                    cout << "+";
            }
            else if(a[i] > 1){
                if(i != n) cout << "+";
                cout << a[i];
            }
            else if(a[i] == -1)
                cout << "-";
            else if(a[i] < -1)
                cout << a[i];
            cout << "x";
            if (i != 1){
                cout << "^" << i;
            }
        }
    }
    if (a[0] != 0){
        if (a[0] > 0 && flag) cout << "+";
        cout << a[0];
    }
    return 0;
}
