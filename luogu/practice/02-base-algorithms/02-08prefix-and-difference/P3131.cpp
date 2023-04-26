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


int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    vector<int> a(n);
    r(i,n) cin >> a[i];

    unordered_map<int, int> record;
    record[0] = -1;
    ll s = 0;
    int res = 0;
    r(i, n){
        s += a[i];
        if(record.find(s % 7) != record.end()){
            res = max(res, i - record[s % 7]);
        }
        else{
            record[s % 7] = i;
        }
    }
    cout << res << endl;
    return 0;
}
