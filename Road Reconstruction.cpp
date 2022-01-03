#include <bits/stdc++.h>
#define INF 2001
using namespace std;

int n, m;
int info[1000][1000];
int dist[1000][1000];
int dx[4] = { 1,-1,0,0 };
int dy[4] = { 0,0,1,-1 };

void djikstra() {
	if (info[0][0] == -1) {
		cout << -1;
		return;
	}

	int i, j, k;

	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			dist[i][j] = INF;
		}
	}
	dist[0][0] = info[0][0];

	priority_queue<tuple<int, int, int>> pq;
	pq.push({ -info[0][0],0,0 });

	while (!pq.empty()) {
		int cost = -get<0>(pq.top());
		int x = get<1>(pq.top());
		int y = get<2>(pq.top());
		pq.pop();

		for (k = 0; k < 4; k++) {
			int nx = x + dx[k];
			int ny = y + dy[k];

			if (!(0 <= nx && nx <= n - 1 && 0 <= ny && ny <= m - 1)) continue;
			if (info[nx][ny] == -1) continue;
			if (dist[nx][ny] <= cost + info[nx][ny]) continue;

			dist[nx][ny] = cost + info[nx][ny];
			pq.push({ -dist[nx][ny],nx,ny });

			if (nx == n - 1 && ny == m - 1) {
				cout << dist[nx][ny];
				return;
			}
		}
	}

	cout << -1;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	cin >> n >> m;
	
	int i, j;
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			cin >> info[i][j];
		}
	}

	djikstra();

	return 0;
}