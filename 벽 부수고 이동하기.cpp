#include <bits/stdc++.h>
#define INF 1000001
using namespace std;

int N, M;
int matrix[1000][1000];
int dp[1000][1000][2];
int dx[4] = { 1,-1,0,0 };
int dy[4] = { 0,0,1,-1 };

int bfs() {
	// dist, x, y, breakable
	queue<tuple<int, int, int, int>> pq;
	if (matrix[0][0] == 0) {
		pq.push({ 1,0,0,1 });
		dp[0][0][1] = 1;
	}
	else {
		pq.push({ 1,0,0,0 });
		dp[0][0][0] = 1;
	}

	while (!pq.empty()) {
		tuple<int, int, int, int> cur = pq.front(); pq.pop();
		int dist = get<0>(cur);
		int x = get<1>(cur);
		int y = get<2>(cur);
		int breakable = get<3>(cur);

		if (x == N - 1 && y == M - 1) {
			return dist;
		}

		int k;
		for (k = 0; k < 4; k++) {
			int nx = x + dx[k];
			int ny = y + dy[k];

			if (!(0 <= nx && nx <= N - 1 && 0 <= ny && ny <= M - 1)) continue;

			if (matrix[nx][ny] == 1) {
				if (breakable == 1 && dist + 1 < dp[nx][ny][0]) {
					pq.push({ dist + 1, nx, ny, 0 });
					dp[nx][ny][0] = dist + 1;
				}
			}
			else {
				if (dist + 1 < dp[nx][ny][breakable]) {
					pq.push({ dist + 1, nx, ny, breakable });
					dp[nx][ny][breakable] = dist + 1;
				}
			}
		}
	}

	return -1;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	cin >> N >> M;
	int i, j;
	string line;
	for (i = 0; i < N; i++) {
		cin >> line;
		for (j = 0; j < M; j++) {
			matrix[i][j] = line[j] - '0';
		}
	}

	for (i = 0; i < N; i++) {
		for (j = 0; j < M; j++) {
			dp[i][j][0] = INF;
			dp[i][j][1] = INF;
		}
	}

	cout << bfs();

	return 0;
}