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

const int N = 55;

int g[N][N];
bool vis[N];
int n, d;
int md = INT_MIN;

void dfs(int x, int fa){
    repp(y, 1, n){
        if (y != fa && ! vis[y] && g[x][y]){
            vis[y] = true;
            dfs(y, x);
        }
    }
}
void dfs2(int x, int fa, int deep){
    queue<int> q;
    q.push(x);
    int step = 0;
    while(!q.empty()){
        int s = q.size();
        for(int j = 0 ; j < s ; j ++){
            int z = q.front();
            q.pop();
            repp(mm, 1, n){
                if( g[z][mm] && !vis[mm]){
                    vis[mm] = true;
                    q.push(mm);
                }
            }
        }
        step += 1;
    }
    md = max(md, step - 1);
}
int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),std::cin.tie(0);

    cin >> n >> d;
    repp(i, 1, n) repp(j, 1, n){
        cin >> g[i][j];
    }
    vis[1] = true;
    dfs(1, 0);
    repp(i, 1, n) if (!vis[i]){
        cout << -1;
        return 0;
    }
    repp(k, 1, n){
        repp(i, 1, n) vis[i] = false;
        vis[k] = true;
        dfs2(k, 0, 0);
    }
    cout << md * d << endl;
    return 0;
}
