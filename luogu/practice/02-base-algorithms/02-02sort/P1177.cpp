#include<bits/stdc++.h>
#define ll long long int
#define F(i,n,m) for(int i=n;i<=m;i++)
#define r(i,n) for(int i=0;i<n;i++)
using namespace std;
const int maxn = 100005;


void quickSort(vector<int> &nums, int l, int r){
    if (l >= r) return;
    int mid = nums[l + (r - l) / 2];
    int i = l, j = r;
    do{
        while(nums[i] < mid) i ++;
        while(nums[j] > mid) j --;
        if(i <= j)
            swap(nums[i ++], nums[j --]);
    }while(i <= j);

    quickSort(nums, l, j);
    quickSort(nums, i, r);
}


int main()
{
    int n;
    cin >> n;
    vector<int> nums(n);
    r(i, n) cin >> nums[i];
    quickSort(nums, 0, nums.size() - 1);
    int i = 1;
    for(int j = 1; j < n ; j ++){
        if(nums[j] != nums[j - 1]){
            nums[i] = nums[j];
            i ++;
        }
    }
    cout << i << endl;
    r(x, i) cout << nums[x] << " "; 
    return 0;
}
