#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
#include <bits/stdc++.h>

using namespace std;


void overturn(int l, int r){
    if(r == l) return ;
    int mid = (r + l - 1) / 2;
    cout<<l<<" "<<mid<<" "<<r<<endl;
    int left_number = r - mid;
    int right_number = mid - l + 1;
    overturn(l, l + left_number - 1);
    overturn(r - right_number + 1, r);
};

int main() {
    int n;
    cin >> n;
    cout<<n - 1<<endl;
    if(n == 1)
        return 0;
    int l = 1;
    int r = n;
    int mid = (l + r - 1) / 2;
    cout<<l<<" "<<mid<<" "<<r<<endl;
    int left_number = r - mid;
    int right_number = mid - l + 1;
    overturn(l, l + left_number - 1);
    overturn(r - right_number + 1, r);
    return 0;
}