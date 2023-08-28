#include <bits/stdc++.h>
using namespace std;


bool isyuanyin(char c){
    return c == 'a'|| c == 'e' || c == 'i' || c == 'o' || c == 'u'; 
}
int dp[5][26][5];

int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),std::cin.tie(0);
    string s;
    cin >> s;
    int n = s.size();
    const int mod = 1000000007;
    unordered_map<char, int> mp;
    mp['a'] = 0;
    mp['e'] = 1;
    mp['i'] = 2;
    mp['o'] = 3;
    mp['u'] = 4;
    if(isyuanyin(s[0]))
        for(int j = 0 ; j < 26 ; j ++)
            if (!isyuanyin('a' + j))
                dp[mp[s[0]]][j][1] = 1;
            
    for(int i = 1 ; i < n ; i ++){
        if (isyuanyin(s[i])){
            int d = mp[s[i]];
            for (int j = 0 ; j < 26 ; j ++ ){
                if(!isyuanyin('a' + j)){
                    dp[d][j][4] = (dp[d][j][3] + dp[d][j][4]) % mod;
                    dp[d][j][1] = (dp[d][j][1] + 1) % mod;
                }
            }
        }else{
            int j = s[i] - 'a';
            for (int d = 0 ; d < 5 ; d ++){
                dp[d][j][3] = (dp[d][j][2] + dp[d][j][3]) % mod;
                dp[d][j][2] = (dp[d][j][1] + dp[d][j][2]) % mod;
            }
        }
    }    
    int res = 0;
    for (int i = 0 ; i < 5 ; i ++){
        for(int j = 0 ; j < 26 ; j ++){
            if (!isyuanyin('a' + j)){
                res = (res + dp[i][j][4]) % mod;
            }
        }
    }
    cout << res << endl;
    return 0;
}
