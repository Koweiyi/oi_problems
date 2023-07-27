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

    priority_queue<int> q1;
    priority_queue<int, vector<int>, greater<int>> q2;
    int n;std::cin >> n;
    int x;std::cin >> x;q1.push(x);
    std::cout << x << endl;
    for(int i = 3; i <= n ; i += 2){
        int a, b;
        std::cin >> a >> b;
        q1.push(a);
        q1.push(b);
        q2.push(q1.top());
        q1.pop();
        while(q1.top() > q2.top()){
            int x = q1.top();q1.pop();
            q2.push(x);
            q1.push(q2.top());
            q2.pop();
        }
        std::cout<< q1.top() << endl;
    }
    return 0;
}
