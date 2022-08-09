#include <bits/stdc++.h>
#define INF 10001
using namespace std;

int n, k;
vector<int> coins;
int dp[10001];


int getCoinCountUsingCoins(int sum) {
	int res = 0;

	int currentSum = sum;
	int i;
	for (i = n - 1; i >= 0; i--) {
		int coin = coins[i];
		if (currentSum >= coin) {
			res += currentSum / coin;
			currentSum %= coin;

			if (currentSum == 0) break;
		}
	}

	if (res == 0 || currentSum != 0) res = INF;
	return res;
}

int getCoinCountUsingDp(int sum) {
	int res = INF;

	int i, j;
	for (i = 1; i < sum / 2 + 1; i++) {
		j = sum - i;
		
		res = min(res, dp[i] + dp[j]);
	}
	return res;
}

int getCoinCount(int sum) {
	int i;
	for (i = 1; i < sum + 1; i++) {
		dp[i] = min(
			getCoinCountUsingCoins(i),
			getCoinCountUsingDp(i)
		);
	}

	return dp[sum];
}


int solution() {
	int res = getCoinCount(k);
	if (res == 0 || res == INF) res = -1;

	return res;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	cin >> n >> k;
	int i;
	for (i = 0; i < n; i++) {
		int tmp;
		cin >> tmp;
		coins.push_back(tmp);
	}
	sort(coins.begin(), coins.end());
	
	cout << solution();

	return 0;
}