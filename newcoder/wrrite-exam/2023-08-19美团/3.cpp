#include <bits/stdc++.h>
using namespace std;

const int N = 2005;
long long dp[N][2];
int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),std::cin.tie(0);

    string s;
    cin >> s;
    if(s[0] == s[1]){
        dp[1][0] = 1;
        dp[1][1] = 1;
    }else{
        dp[1][0] = 0;
        dp[1][1] = 2;
    }
    for (int i = 1 ; i < s.size() ; i ++){
        if(s[i] == s[i - 1]){
            dp[i][0] = dp[i - 1][1] ;
            dp[i][1] = dp[i - 1][0] + 1;
        }else{
            dp[i][0] = dp[i - 1][0];
            dp[i][1] = dp[i - 1][1] + 1;
        }
    }
    long long res = 0;
    for (int i = 0 ; i < s.size() ; i ++){
        res += min(dp[i][0], dp[i][1]);
    }
    cout << res << endl;
    return 0; 
}
