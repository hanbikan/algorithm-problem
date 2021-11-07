#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#define INF 200001
#define MAX 20001
using namespace std;

int dp[MAX];
int w[MAX][MAX];

void djikstra(int start) {
	priority_queue<pair<int, int>> pq;
	for (int i = 0; i < MAX; i++) dp[i] = INF;
	pq.push(make_pair(0, start));
	dp[start] = 0;

	int res = INF;
	while (!pq.empty()) {
		int weight = -pq.top().first;
		int node = pq.top().second;
		pq.pop();

		if (dp[node] < weight) continue;

		for (int i = 0; i < MAX; i++) {
			int next_weight = w[node][i];

			if (next_weight == 0) continue;

			if (weight + next_weight < dp[i]) {
				dp[i] = weight + next_weight;
				pq.push(make_pair(-dp[i], i));
			}
		}
	}
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int V, E;
	cin >> V >> E;

	int K;
	cin >> K;

	int i;
	for (i = 0; i < E; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		if (w[a][b] == 0 || w[a][b] > c) w[a][b] = c;
	}

	djikstra(K);
	for (i = 1; i < V + 1; i++) {
		if (dp[i] == INF) cout << "INF\n";
		else cout << dp[i] << "\n";
	}

	return 0;
}