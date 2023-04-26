#include<bits/stdc++.h>
#define ll long long int
#define F(i,n,m) for(int i=n;i<=m;i++)
#define r(i,n) for(int i=0;i<n;i++)
using namespace std;
const int maxn = 105;

inline int read(void) {
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

int g[maxn][maxn];
int s[maxn][maxn];
int main(int argc, char const *argv[])
{
    int n, m;
    cin >> n >> m;
    F(i, 1, n) F(j, 1, m) g[i][j] = read();
    F(i, 1, n) F(j, 1, m) s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + g[i][j];
    for(int len = n; len >= 1; len --){
        for (int i = 0; i + len - 1 < n ; i ++){
            for(int j = 0 ; j + len - 1 < m ; j ++){
                int sum = s[i + len][j + len] + s[i][j] - s[i + len][j] - s[i][j + len];
                if (sum == len * len){
                    cout << len << endl;
                    return 0;
                }
            }
        }
    }
    
    cout << 0 << endl;
    return 0;
}
