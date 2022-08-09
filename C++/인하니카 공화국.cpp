#include <bits/stdc++.h>
#define INF 20001
using namespace std;

int N, M;
vector<pair<int, int>> graph[1001];
int dp[1001];

int f(int node, int parent) {
	// DP가 초기값일 경우
	if (dp[node] == 0) {
		int res = INF;

		// node-childs 간의 다이너마이트 선택
		int sum = 0;
		int i;
		for (i = 0; i < graph[node].size(); i++) {
			int child = graph[node].at(i).first;
			int childWeight = graph[node].at(i).second;
			if (child == parent) {
				// parent-node 간의 다이너마이트 선택
				res = childWeight;
				continue;
			}

			if (graph[child].size() == 1) sum += childWeight;
			else sum += f(child, node);
		}
		res = min(res, sum);

		dp[node] = res;
	}

	return dp[node];
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int T;
	cin >> T;
	for (; T > 0;T--) {
		cin >> N >> M;

		// 초기화
		int i;
		for (i = 1; i < N + 1; i++) {
			graph[i].clear();
			dp[i] = 0;
		}

		// 입력
		int a, b, c;
		for (i = 0; i < M; i++) {
			cin >> a >> b >> c;
			graph[a].push_back({ b, c });
			graph[b].push_back({ a, c });
		}

		// 출력
		cout << f(1, 0) << "\n";
	}

	return 0;
}