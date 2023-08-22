#include<bits/stdc++.h>
using namespace std;

const int N = 100005;
int a[N];
long long s[N];
int main(int argc, char const *argv[])
{
    int n;
    cin >> n;

    long long res = 0;
    for (int i = 1 ; i <= n ; i ++){
        cin >> a[i];
        s[i] = s[i - 1] + a[i];
        res += a[i];
    }
    for (int i = 2; i <= n ; i ++ ){
        res = max(res, s[i - 2] + a[i] * a[i - 1] + s[n] - s[i]);
    }    
    cout << res << endl;
    return 0;
}
