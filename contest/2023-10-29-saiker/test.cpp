#include<bits/stdc++.h>

using namespace std;
const int maxn = 2e5 + 5;

int get_fa(vector<pair<int, int>> &fa, int x)
{
    return x == fa[x].first ? x : fa[x].first = get_fa(fa, fa[x].first);
}


void unionfa(vector<pair<int, int>> &fa, int x, int y)
{
    int fx = get_fa(fa, x);
    int fy = get_fa(fa, y);
    if ( fa[fx].second > fa[fy].second )  fa[fy].first = fx;
    else
    {
        fa[fx].first = fy;
        if ( fa[fx].second == fa[fy].second ) fa[fy].second += 1;
    }
}

map<int, vector<int>> get_set(vector<pair<int, int>> &fa, int n)
{
    map<int, vector<int>> mp;
    for (int i = 1; i <= n; i++)
    {
        int f = get_fa(fa, i);
        if (!mp.count(f)) mp[f] = vector<int>{i};
         else mp[f].push_back(i);
    }
    return mp;
}
pair<int, int> calc(vector<pair<int, int>> &fa, vector<int> ve)
{
    int maxs = -1, mins = maxn;
    map<int,int> count;
    for (auto x : ve)
    {
        int f=get_fa(fa, x);
        if( count.count(f) ) count[f]+=1;
        else count[f]=1;
    }
    for(auto it :count){
        maxs = max(maxs, it.second);
        mins = min(mins, it.second);
    }
    return pair<int, int>(maxs, mins);
}
int main()
{
    ios::sync_with_stdio(0);std::cin.tie(0);
    
	int n, m;
    cin>>n>>m;
    
    vector<pair<int, int>> fmap(n + 5);
    for (int i = 0; i <= n; i++)
        fmap[i] = pair<int, int>{i, 1};
        
    while( m-- ){
    	int a, b;
        cin>>a>>b;
        unionfa(fmap, a, b);
	}
    int k;
    cin >> k;
    vector<pair<int, int>> ft(n + 5);
    
    for (int i = 0; i <= n; i++)
        ft[i] = pair<int, int>{i, 1};
    
    while( k-- ){
    	int a, b;
        cin >> a >> b;
        unionfa(ft, a, b);
	}
    
    map<int, vector<int>> mp = get_set(ft, n);
    
    int maxs = 1, mins = 2e5;
    
    for (auto v : mp)
    {
        pair<int, int> p = calc(fmap, v.second);
        maxs = max(maxs, p.first);
        mins = min(mins, p.second);
    }
    cout << maxs << " " << mins << "\n";
}
