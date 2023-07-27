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

const int maxn = 100005;

int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),std::cin.tie(0);

    priority_queue<int, vector<int>, greater<int>> q;
    string s;
    while(getline(std::cin, s) && s != "END"){
        sort(s.begin(), s.end());
        int num = 1;
        repp(i, 1, s.size()){
            if(s[i] != s[i - 1]) q.push(num), num = 1;
            else num ++;
        }
        int ans = 0;
        if(q.size() == 1) ans = s.length();
        while(q.size() > 1){
            int a = q.top(); q.pop();
            int b = q.top(); q.pop();
            q.push(a + b);
            ans += a + b;
        }
        q.pop();
        printf("%d %d %.1f", s.length() * 8, ans, (double)s.length() * 8 / (double)ans);
    } 
    return 0;
}
