#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#define INF 4000001
using namespace std;

vector<pair<int, int>> w[401];

int djikstra(int start) {
	priority_queue<pair<int, int>> pq;
	int dp[401];
	for (int i = 0; i < 401; i++) dp[i] = INF;
	pq.push(make_pair(0, start));
	dp[start] = 0;

	int res = INF;
	while (!pq.empty()) {
		int weight = -pq.top().first;
		int node = pq.top().second;
		pq.pop();

		if (dp[node] < weight) continue;

		for (int i = 0; i < w[node].size(); i++) {
			int next_node = w[node][i].first;
			int next_weight = w[node][i].second;

			if (next_weight == 0) continue;

			if (weight + next_weight < dp[next_node]) {
				dp[next_node] = weight + next_weight;
				pq.push(make_pair(-dp[next_node], next_node));
			}else if (next_node == start) res = min(res, dp[node] + next_weight);
		}
	}

	return res;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int V, E;
	cin >> V >> E;
	int i;
	for (i = 0; i < E; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		w[a].push_back(make_pair(b, c));
	}

	int res = INF;
	for (i = 1; i < V+1; i++) res = min(res, djikstra(i));
	if (res == INF) cout << -1;
	else cout << res;

	return 0;
}