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

const int maxn = 35;
int yc[maxn][maxn], n;
char c;
string words[maxn];
int visited[maxn];
int res = 0, l = 0;

int solve(int x, int y){
    pre(sx, words[x].size() - 1, 0){
        int i = sx;
        int j = 0;
        bool flag = true;
        while(i < words[x].size()){
            if(j >= words[y].size() or words[x][i] != words[y][j ++]){
                flag = false;
                break;
            }
            i ++;
        } 
        if(flag) return words[x].size() - sx;
    }
    return 0;
}

void dfs(int p){
    bool flag = false;
    repp(i, 1, n){
        if(visited[i] >= 2 or yc[p][i] == 0 or yc[p][i] == words[i].size() or yc[p][i] == words[p].size()) continue;
        l += words[i].size() - yc[p][i];
        visited[i] ++;
        flag = true;
        dfs(i);
        l -= words[i].size() - yc[p][i];
        visited[i] --;
    }
    if(!flag) res = max(res, l);
}

int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),cin.tie(0);
    cin >> n;
    repp(i, 1, n)cin >> words[i];
    cin >> c; 
    repp(i, 1, n) repp(j, 1, n){
        yc[i][j] = solve(i, j);
    }
    repp(i, 1, n){
        if (words[i][0] == c){
            visited[i] ++;
            l = words[i].size();
            dfs(i);
            visited[i] = 0;
        }
    }
    cout << res;
    return 0;
}

