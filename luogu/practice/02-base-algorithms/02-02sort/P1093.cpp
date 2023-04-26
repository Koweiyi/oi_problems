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

struct stu{
    int id, c, sum;
    bool operator < (const stu b){
        if(sum > b.sum) return true;
        else if(sum < b.sum) return false;
        else{
            if (c > b.c)return true;
            else if(c < b.c) return false;
            return id < b.id;
        }
    }
}s[305];


int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),cin.tie(0);
    int n;
    cin >> n;
    repp(i, 1, n){
        int a,b,c;
        cin >> a >> b >> c;
        s[i].id = i;
        s[i].sum = a + b + c;
        s[i].c = a;
    }
    sort(s + 1, s + n + 1);
    repp(i, 1, 5){
        cout << s[i].id << " " << s[i].sum << endl;
    }
    return 0;
}
