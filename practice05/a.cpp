#include <bits/stdc++.h>
#define ll long long
using namespace std;


void solve() {
	int n;
	cin >> n;
	
	int mxn = n;
	
	map < int, vector <int>> mp;
	
	vector < int > ans;
	
	for (int i = 1; i <= n; i++) {
		int l = 1, r = mxn;
		
		int k = -1;
		
		while (l <= r) {
			int mid = (l + r) / 2;
			cout << "? " << i << ' ' << mid << endl;
			string z;
			cin >> z;
			
			if (z == "Yes") {
				r = mid - 1;
				k = mid;
			} else {
				l = mid + 1;
			}
		}
		
		if (mxn > k) {
			ans.clear();
			ans.pb(i)
		} else {
			ans.pb(i);
		}
		
		mxn = min(mxn, k);
		
	}
	
	cout << "! ";
	cout << ans.size() << " ";
	for (int x : ans) {
		cout << x << " ";
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	solve();
}