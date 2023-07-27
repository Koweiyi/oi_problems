#include<bits/stdc++.h>
using namespace std;


vector<int> z_function(string s) {
    int n = s.length();
    vector<int> z(n);
    for (int i = 1, l = 0,r = 0; i < n; ++i) {
        if (i <= r && z[i - l] < r - i + 1) {
            z[i] = z[i - l];
        }
        else {
            z[i] = max(0,r - i + 1);
            while (i + z[i] < n && s[z[i]] == s[i + z[i]]) ++z[i];
        }
        if (i + z[i] - 1 > r) l = i,r = i + z[i] - 1;
    }
    return z;
}
int main(){
    string s;cin >> s;
    vector<int> z = z_function(s);
    long long res =(long long)s.size();
    for(int v: z)
        res += v;
    cout << res << endl;
    return 0;
}