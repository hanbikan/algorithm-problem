#include <iostream>
#include <vector>
#define INF 5000001
using namespace std;

vector<pair<int, int>> weights[501];
long long dp[501];

bool doBellmanFord(int length) {
	bool res = true;

	for (int i = 1; i < length + 1; i++) {
		for (int j = 1; j < length + 1; j++) {
			for (int k = 0; k < weights[j].size(); k++) {
				if (dp[j] != INF && dp[weights[j][k].first] > weights[j][k].second + dp[j]) {
					dp[weights[j][k].first] = weights[j][k].second + dp[j];

					if (i == length) res = false;
				}
			}
		}
	}

	return res;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int N, M;
	cin >> N >> M;

	for (int i = 0; i < 501; i++) dp[i] = INF;
	dp[1] = 0;

	for (int i = 0; i < M; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		weights[a].push_back(make_pair(b, c));
	}

	bool res = doBellmanFord(N);
	if (res == false) cout << "-1";
	else {
		for (int i = 2; i < N + 1; i++) {
			if (dp[i] == INF) cout << "-1\n";
			else cout << dp[i] << "\n";
		}
	}
}
