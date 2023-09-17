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

int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),std::cin.tie(0);

    int n;
    cin >> n;
    repp(k,1,4){
        string s;
        cin >> s; 
        double res = 0;
        int ht = 0;
        int i = 0;
        while (i < s.size()){
            char ch = s[i];
            if(ch == '>'){
                res += 0.5;
                ht = 9;
                i ++;
            }else if (ch == '.'){
                if(ht){
                    res += 0.5;
                    ht -= 1;
                }else{
                    res += 1.0;
                }
                i ++;
            }
            else if (ch == 'w'){
                if (ht >= 2){
                    res += 1.0;
                    ht -= 2;
                }
                else if(ht == 1){
                    res += 1.5;
                    ht = 0;
                }else{
                    res += 2.0;
                }
                i ++;
            }else if (ch == 's'){
                res += 1.0;
                ht -= 2;
                ht = max(ht, 0);
                s[i] = '.';
            }else if(ch == 'm'){
                res += 2.0;
                ht -= 4;
                ht = max(ht, 0);
                s[i] = '.';
            }
        }

        cout << fixed << setprecision(1) << res << " ";
    }
    return 0;
}
