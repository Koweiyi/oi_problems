#include <iostream>
#include <vector>
using namespace std;

const int mod = 1e9 + 7;

int dfs(int i, int left, vector<vector<int>>& memo, vector<int>& a, int n) {
    if (i == n) {
        if (left == 0) {
            return 1;
        }
        return 0;
    }
    if (memo[i][left] != -1) {
        return memo[i][left];
    }
    int res = 0;
    for (int j = 1; j < a[i]; j++) {
        if (left >= j) {
            res = (res + dfs(i + 1, left - j, memo, a, n)) % mod;
        }
    }
    for (int j = a[i] + 1; left - j >= n - (i + 1) && j <= left; j++) {
        res = (res + dfs(i + 1, left - j, memo, a, n)) % mod;
    }
    memo[i][left] = res;
    return res;
}

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    int s = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        s += a[i];
    }

    vector<vector<int>> memo(n + 1, vector<int>(505, -1));
    int res = dfs(0, s, memo, a, n);
    cout << res << endl;

    return 0;
}