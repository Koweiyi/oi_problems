#include<bits/stdc++.h>
using namespace std;

const int maxn = 270000;

int n, val, ans;
int f[60][maxn];

inline int read(void) {
    int s = 0, w = 1;
    char ch = getchar();
    for(; ch < '0' || ch > '9'; ch = getchar()) if(ch == '-') w = -1;
    for(; ch <= '9' && ch >= '0'; ch = getchar()) s= s * 10 + ch - '0';
    return s * w;
}

int main(){

    n = read();
    for(register int i = 1; i <= n; i++) val = read(), f[val][i] = i + 1; 
    
    for(register int i = 2; i <= 58; i++) {
        for(register int j = 1 ; j <= n ; j ++){
            if (!f[i][j])
                f[i][j] = f[i - 1][f[i - 1][j]];
            if (f[i][j])
                ans = i;
        }
    }
        
    cout << ans << '\n';
    return 0;
}