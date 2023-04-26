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

double a, b, c, d;


double f(double x){
    return a * x * x * x + b * x * x + c * x + d;
}


int main(int argc, char const *argv[])
{
    vector<double> res;
    //a = read(), b = read(), c = read(), d = read();
    cin >> a >> b >> c >> d;
    double pre = -110;
    F(i, -100, 99){
        double l = i, r = i + 1;

        if (f(l) * f(r) > 0)
            continue;
        r(x, 12){
            double mid = (l + r) / 2;
            if (f(mid) * f(l) <= 0)
                r = mid;
            else
                l = mid; 
        }
        if(l - pre >= 0.0005){
            res.push_back(l);
            pre = l;
            if (res.size() == 3) break;
        }
    }
    for (double x : res)
        printf("%.2f ", x);
    return 0;
}
