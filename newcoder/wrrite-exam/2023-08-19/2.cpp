#include <bits/stdc++.h>
using namespace std;
const int N = 100005;

bool check(string &s, int i, int j){
    if (s[i] == s[j]){
        return true;
    } 
    if ((s[i] == 'b' || s[i] == 'd' || s[i] == 'p' || s[i] == 'q') && (s[j] == 'b' || s[j] == 'd' || s[j] == 'p' || s[j] == 'q')) 
        return true;
    if ((s[i] == 'n' || s[i] == 'u') && (s[j] == 'n' || s[j] == 'u'))
        return true;
    return false;
}
void solve(){
    string s;
    cin >> s;
    int l = 0, r = s.size() - 1;
    while(l < r){
        if (check(s, l, r)){
            l ++;
            r --;
        }else{
            if (s[l] == 'w' && s[r] == 'v'){
                s[l] = 'v';
                r --;
                continue;
            }
            if (s[l] =='v' && s[r] == 'w'){
                s[r] = 'v';
                l ++;
                continue;
            }
            if (s[l] == 'm' && s[r] == 'n' || s[r] == 'u'){
                s[l] = 'n';
                r --;
                continue;
            }
            if (s[l] == 'n' || s[l] == 'u' && s[r] == 'm'){
                l ++;
                s[r] = 'n';
                continue;
            }
            cout << "NO" << endl;
            return;
        }
    }
    cout << "YES" << endl;
    return;
}


int main(int argc, char const *argv[]){
    ios::sync_with_stdio(0),std::cin.tie(0);

    int N;
    cin >> N;
    while (N --) {solve();}
    return 0;
}

