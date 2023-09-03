#include <bits/stdc++.h>
#define mem(a, b) memset(a, b, sizeof a)
#define rep(i, n, m) for (int i = n; i < m; i++)
#define repp(i, n, m) for (int i = n; i <= m; i++)
#define pre(i, n, m) for (int i = n; i >= m; i--)
#define len(x) (int)(x).size()
#define all(x) (x).begin(), (x).end()
#define gcd(a, b) __gcd(a, b)
#define lcm(a, b) a / gcd(a, b) * b
#define ft first
#define sd second
#define PI acos(-1.0)
#define INF 0x3f3f3f3f
#define ll long long
#define endl "\n"
#define pii pair<int, int>
using namespace std;
const int maxn = 15;

inline ll read(void)
{
    int s = 0, w = 1;
    char ch = getchar();
    for (; ch < '0' || ch > '9'; ch = getchar())
        if (ch == '-')
            w = -1;
    for (; ch <= '9' && ch >= '0'; ch = getchar())
        s = s * 10 + ch - '0';
    return s * w;
}

inline void out(ll a)
{
    if (a >= 10)
        out(a / 10);
    putchar(a % 10 + '0');
}
const double eps = 1e-6;
double a[maxn];
int n;
double f(double x){
    double s = 0;
    pre(i, n, 0)
        s = s * x + a[i];
    return s;
}

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(0), cin.tie(0);
    double l, r;
    cin >> n >> l >> r;
    pre(i, n, 0) cin >> a[i];

    while (r - l > eps)
    {
        double k = (r - l) / 3.0;
        double m1 = l + k, m2 = r - k;
        if (f(m1) < f(m2))
            l = m1;
        else
            r = m2;
    }
    printf("%.5f\n", l);
    return 0;
}
