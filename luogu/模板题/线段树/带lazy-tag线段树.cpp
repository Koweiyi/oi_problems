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

const int N = 100005;
ll a[N];
ll mx[N << 2];
ll mn[N << 2];
ll sum[N << 2];
ll tag[N << 2];

ll ls(ll p){return p << 1;}
ll rs(ll p){return p << 1|1;}
ll n;

void push_up(ll p){
    sum[p] = sum[ls(p)] + sum[rs(p)];
    mx[p] = max(mx[ls(p)], mx[rs(p)]);
    mn[p] = min(mn[ls(p)], mn[rs(p)]);
}

void build(ll p, ll pl, ll pr){
    tag[p] = 0;
    if(pl == pr){
        mx[p] = a[pl];
        mn[p] = a[pl];
        return;
    }
    ll mid = (pl + pr) >> 1;
    build(ls(p), pl, mid);
    build(rs(p), mid + 1, pr);
    push_up(p);
}

void addtag(ll p, ll pl, ll pr, ll d){
    tag[p] += d;
    mn[p] += d;
    mx[p] += d;
    sum[p] += d * (pr - pl + 1);
} 

void push_down(ll p, ll pl, ll pr){
    if (tag[p]) {
        ll mid = (pl + pr) / 2;
        addtag(ls(p), pl, mid, tag[p]);
        addtag(rs(p), mid + 1, pr, tag[p]);
        tag[p] = 0;
    }
}

void update(ll L, ll R, ll p, ll pl, ll pr, ll d){
    if (L <= pl && pr <= R){
        addtag(p, pl, pr, d);
        return;
    }
    push_down(p, pl, pr);
    ll mid = (pl + pr) / 2;
    if (L <= mid) update(L, R, ls(p), pl, mid, d);
    if (mid < R) update(L, R, rs(p), mid + 1, pr, d);
    push_up(p);
}

void update(ll L, ll R, ll d){
    update(L, R, 1, 1, n, d);
}

ll queryMin(ll L, ll R, ll p, ll pl, ll pr){
    if (L <= pl && pr <= R){
        return mn[p];
    }
    push_down(p, pl, pr);
    ll res = LONG_LONG_MAX;
    ll mid = (pl + pr) / 2;
    if (L <= mid) res = min(res, queryMin(L, R, ls(p), pl, mid));
    if (R > mid) res = min(res, queryMin(L, R, rs(p), mid + 1, pr));
    return res;
}
ll queryMin(ll L, ll R){
    return queryMin(L, R, 1, 1, n);
}

ll queryMax(ll L, ll R, ll p, ll pl, ll pr){
    if (L <= pl && pr <= R){
        return mx[p];
    }
    push_down(p, pl, pr);
    ll res = LONG_LONG_MIN;
    ll mid = (pl + pr) / 2;
    if (L <= mid) res = max(res, queryMin(L, R, ls(p), pl, mid));
    if (R > mid) res = max(res, queryMin(L, R, rs(p), mid + 1, pr));
    return res;
}
ll queryMax(ll L, ll R){
    return queryMax(L, R, 1, 1, n);
}

ll querySum(ll L, ll R, ll p, ll pl, ll pr){
    if (L <= pl && pr <= R){
        return sum[p];
    }
    push_down(p, pl, pr);
    ll res = 0;
    ll mid = (pl + pr) / 2;
    if (L <= mid) res += queryMin(L, R, ls(p), pl, mid);
    if (R > mid) res += queryMin(L, R, rs(p), mid + 1, pr);
    return res;
}
ll querySum(ll L, ll R){
    return querySum(L, R, 1, 1, n);
}

int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),std::cin.tie(0);
    int M,N,Q;
    cin >> M >> N >> Q;
    for(int i = 1 ; i <= M - 1 ; i ++ ){
        a[i] = N;
    }
    map<pii, int> mp;
    n = M - 1;
    build(1, 1, n);
    for(int i = 0 ; i < Q ; i ++ ){
        char op;
        cin >> op; 
        if(op == 'Q'){
            int x, y;
            cin >> x >> y ;
            cout << queryMin(x + 1, y) << endl;
        }else if (op == 'B'){
            int x, y, c;
            cin >> x >> y >> c; 
            if (c <= queryMin(x + 1, y)){
                cout << "OK!" << endl;
                update(x + 1, y, -c);
                mp[{x,y}] += c;
            }else{
                cout << "Fail!" << endl;
            }
        }else if (op == 'R'){
            int x, y, c;
            cin >> x >> y >> c; 
            if (mp[{x,y}] >= c){
                cout << "OK!" << endl;
                update(x + 1, y, c);
                mp[{x,y}] -= c;
            }else{
                cout << "Fail!" << endl;
            }
        }
    }
    
    return 0;
}
