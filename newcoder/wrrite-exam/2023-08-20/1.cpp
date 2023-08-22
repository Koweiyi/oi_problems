#include <bits/stdc++.h>
using namespace std;
const int N = 100005;
int a[N];

long long solve(int l, int r){
    long long res = 0;
    int leng =  (r - l + 1) ;
    int mid = 0;
    if (leng & 1){
        mid = a[(l + r) / 2];
    }else{
        mid = (a[(l + r) / 2] + a[(l + r) / 2 + 1]) / 2;
    }
    for (int i = l ; i <= r ; i ++){
        res += abs(a[i] - mid);
    }
    return res;
}

int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),std::cin.tie(0);

    int n;
    cin >> n;
    long long s = 0;
    for(int i = 1 ; i <= n ; i ++) cin >> a[i];
    sort(a + 1, a + n + 1);
    if (a[1] == a[n]){
        cout << 1 << endl;
        return 0;
    }
    long long res = min(solve(1, n - 1), solve(2, n)); 
    cout << res << endl;
    return 0;
}
