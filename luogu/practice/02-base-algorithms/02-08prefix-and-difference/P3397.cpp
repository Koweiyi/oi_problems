#include<bits/stdc++.h>
#define ll long long int
#define F(i,n,m) for(int i=n;i<=m;i++)
#define r(i,n) for(int i=0;i<n;i++)
using namespace std;
const int maxn = 1005;

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


int g[maxn][maxn], s[maxn][maxn];

int main(int argc, char const *argv[])
{
    int n, m;
    n = read();
    m = read();
    r(i, m){
        int x1, y1, x2, y2;
        x1 = read(), y1 = read(), x2 = read(), y2 = read();
        s[x1][y1] += 1;
        s[x1][y2 + 1] -= 1;
        s[x2 + 1][y1] -= 1;
        s[x2 + 1][y2 + 1] += 1;
    }

    F(i, 1, n){
        F(j, 1, n){
            g[i][j] = s[i][j] + g[i - 1][j] + g[i][j - 1] - g[i - 1][j - 1];
        }
    }
    F(i, 1, n){
        F(j, 1, n){
            out(g[i][j]);
            putchar(' ');
        }
        cout << "\n";
    }
    return 0;
}
