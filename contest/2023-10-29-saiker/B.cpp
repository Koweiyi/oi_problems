#include <iostream>
#include <vector>
#include <set>
using namespace std;

vector<int> r1, r2, s;
vector<set<int>> g;

int find(int x, vector<int>& r) {
    if (x != r[x]) {
        r[x] = find(r[x], r);
    }
    return r[x];
}

void union_(int x, int y, vector<int>& r) {
    int rx = find(x, r);
    int ry = find(y, r);
    if (rx != ry) {
        r[rx] = ry;
    }
}

void union2(int x, int y) {
    int rx = find(x, r2);
    int ry = find(y, r2);
    if (rx != ry) {
        r2[rx] = ry;
        int tot = s[rx] + s[ry];
        s[rx] = s[ry] = tot;
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    
    r1.resize(n + 1);
    for (int i = 0; i <= n; i++) {
        r1[i] = i;
    }
    
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        union_(u, v, r1);
    }
    
    r2.resize(n + 1);
    s.resize(n + 1, 1);
    
    int k;
    cin >> k;
    
    g.resize(n + 1); // Resizing g to accommodate n + 1 elements
    
    for (int i = 0; i < k; i++) {
        int u, v;
        cin >> u >> v;
        if (find(u, r1) == find(v, r1)) {
            union2(u, v);
        } else {
            for (int w : g[u]) {
                if (find(u, r1) == find(w, r1)) {
                    union2(u, w);
                }
            }
            for (int w : g[v]) {
                if (find(v, r1) == find(w, r1)) {
                    union2(v, w);
                }
            }
            g[u].insert(v);
            g[v].insert(u);
        }
    }
    
    int mx = -1;
    int mn = 999999999;
    
    for (int i = 1; i <= n; i++) {
        int sz = s[find(i, r2)];
        mx = max(mx, sz);
        mn = min(mn, sz);
    }
    
    cout << mx << " " << mn << endl;
    
    return 0;
}
