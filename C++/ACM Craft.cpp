#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int D[1001];
int res[1001];
int depths[1001];
vector<int> nexts[1001];

void doTopologicalSort(int N) {
	queue<int> q;
	int i;

	for (i = 1; i < N + 1; i++) {
		if (depths[i] == 0) {
			q.push(i);
			res[i] = D[i];
		}
	}

	while (!q.empty()) {
		int cur = q.front();
		q.pop();

		for (i = 0; i < nexts[cur].size(); i++) {
			int next = nexts[cur][i];
			depths[next]--;
			res[next] = max(res[next], D[next] + res[cur]);

			if (depths[next] == 0) q.push(next);
		}
	}
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N, K;
		cin >> N >> K;

		int j;
		for (j = 1; j < N+1; j++) {
			res[j] = 0;
			depths[j] = 0;
			nexts[j].clear();
		}

		for (j = 1; j < N+1; j++) cin >> D[j];

		for (j = 0; j < K; j++) {
			int a, b;
			cin >> a >> b;
			nexts[a].push_back(b);
			depths[b] += 1;
		}

		doTopologicalSort(N);

		int W;
		cin >> W;
		cout << res[W] << "\n";
	}


	return 0;
}
