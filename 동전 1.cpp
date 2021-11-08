#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int n, k;
	cin >> n >> k;
	
	int i, j;
	int *coins = (int *)malloc(sizeof(int)*n);
	for (i = 0; i < n; i++) cin >> coins[i];

	// Solution
	int dp[10001] = {1};

	for (i = 0; i < n; i++) {
		int coin = coins[i];
		for (j = 1; j < k+1; j++) {
			if (j - coin >= 0) dp[j] += dp[j - coin];
		}
	}

	cout << dp[k];

	free(coins);

	return 0;
}