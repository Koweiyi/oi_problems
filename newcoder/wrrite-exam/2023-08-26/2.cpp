#include <bits/stdc++.h>
using namespace std;


int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),std::cin.tie(0);
    string s;
    int n, k;
    cin >> n >> k;
    cin >> s;
    char flip = '0'; 
    reverse(s.begin(), s.end());
    while(s.size() > 1 && k > 0){
        for (int i = s.size() - 1; i > 0 ; i --){
            if(s[i] != flip){
                s.pop_back();
            }else{
                flip ^= 1;
                k -= 1;
                break;
            }
        } 
    }
    reverse(s.begin(), s.end());
    flip ^= (k & 1);
    if(flip == '1'){
        for(int i = 0 ; i < s.size() ; i ++ ){
            s[i] ^= 1;
        }
    }
    cout << s << endl;
    return 0;
}
