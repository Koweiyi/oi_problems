#include<bits/stdc++.h>
#define ll long long int
#define F(i,n,m) for(int i=n;i<=m;i++)
#define r(i,n) for(int i=0;i<n;i++)
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

int L, N, M; 
int g[maxn];

bool judge(int x){
    int cur = 0;
    int s = 0;
    r(i, N + 1){
        if (g[i] - cur < x){
            s += 1;
        }else{
            cur = g[i];
        }
    }
    return s <= M;
}

int main(int argc, char const *argv[])
{
    cin >> L >> N >> M;
    F(i, 1, N)
        cin >> g[i - 1];
    g[N] = L;
    int l = 0, r = L + 1;
    while(l + 1 < r){
        int mid = l + (r - l) / 2;
        if(judge(mid)){
            l = mid;
        }else{
            r = mid;
        }
    }
    cout << l;
    return 0;
}
