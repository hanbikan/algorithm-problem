#include <iostream>
#include <queue>
#include <tuple>
#define INF 140626
using namespace std;

int dx[] = { 1, -1, 0, 0 };
int dy[] = { 0, 0, 1, -1 };
int N;
int map[125][125];
int dist[125][125];

bool is_in_range(int x, int y) {
	return 0 <= x && x <= N - 1 && 0 <= y && y <= N - 1;
}

int djikstra() {
	priority_queue<tuple<int, int, int>> pq;
	pq.push(make_tuple(-map[0][0], 0, 0)); // weight, x, y

	// Initialize dist
	int i, j;
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) dist[i][j] = INF;
	}
	dist[0][0] = map[0][0];

	while (!pq.empty()) {
		int w = -get<0>(pq.top());
		int x = get<1>(pq.top());
		int y = get<2>(pq.top());
		pq.pop();

		if (w > dist[x][y]) continue;

		for (i = 0; i < 4; i++) {
			int nextX = x + dx[i];
			int nextY = y + dy[i];

			if (!is_in_range(nextX, nextY)) continue;

			int nextW = w + map[nextX][nextY];
			if (nextW < dist[nextX][nextY]) {
				pq.push(make_tuple(-nextW, nextX, nextY));
				dist[nextX][nextY] = nextW;
			}
		}
	}

	return dist[N - 1][N - 1];
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int cnt = 1;
	while (1) {
		cin >> N;
		if (N == 0) break;

		int i, j;
		for (i = 0; i < N; i++) {
			for (j = 0; j < N; j++) cin >> map[i][j];
		}

		cout << "Problem " << cnt << ": " << djikstra() << "\n";
		cnt++;
	}

	return 0;
}
