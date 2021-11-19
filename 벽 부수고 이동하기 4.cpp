#include <iostream>
#include <vector>
#include <set>
using namespace std;

int N, M;
int info[1000][1000];
int isVisited[1000][1000];
int parents[1000000];
int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1 };

int findParent(int x) {
	if (x == parents[x]) return x;

	return findParent(parents[x]);
}

void unionParents(int x, int y) {
	int xParent = findParent(x);
	int yParent = findParent(y);

	if (xParent < yParent) parents[yParent] = xParent;
	else parents[xParent] = yParent;
}

int getMoveCount(int x, int y) {
	int res = 1;

	int k;
	for (k = 0; k < 4; k++) {
		int nx = x + dx[k];
		int ny = y + dy[k];
		if (!(0 <= nx && nx <= N - 1 && 0 <= ny && ny <= M - 1)) continue;
		if (!(isVisited[nx][ny] == 0 && info[nx][ny] == 0)) continue;

		unionParents(x * M + y, nx * M + ny);
		isVisited[nx][ny] = 1;
		res = (res + getMoveCount(nx, ny)) % 10;
	}

	return res % 10;
}

void setInfo(int x, int y, int val) {
	int k;
	for (k = 0; k < 4; k++) {
		int nx = x + dx[k];
		int ny = y + dy[k];
		if (!(0 <= nx && nx <= N - 1 && 0 <= ny && ny <= M - 1)) continue;
		if (!(isVisited[nx][ny] == 1 && info[nx][ny] == 0)) continue;

		isVisited[nx][ny] = 2;
		info[nx][ny] = -val;
		setInfo(nx, ny, val);
	}
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int i, j, k;

	// Input
	cin >> N >> M;
	vector<pair<int, int>> walls;
	for (i = 0; i < N; i++) {
		for (j = 0; j < M; j++) {
			char c;
			cin >> c;
			info[i][j] = c - '0';

			if (info[i][j] == 1) walls.push_back({ i, j });
		}
	}

	for (i = 0; i < N; i++) {
		for (j = 0; j < M; j++) parents[i * M + j] = i * M + j;
	}

	// 빈 곳에 대해, 얼마나 이어져있는지 info에 음수로 저장
	for (i = 0; i < N; i++) {
		for (j = 0; j < M; j++) {
			if (!(!isVisited[i][j] && info[i][j] == 0)) continue;

			isVisited[i][j] = 1;
			int res = getMoveCount(i, j);

			isVisited[i][j] = 2;
			info[i][j] = -res;
			setInfo(i, j, res);
		}
	}

	// walls를 따라서, 상하좌우를 참조하여 음수값들을 합쳐서 저장
	for (i = 0; i < walls.size(); i++) {
		int x = walls[i].first;
		int y = walls[i].second;
		int count = 1;

		set<int> done;
		for (k = 0; k < 4; k++) {
			int nx = x + dx[k];
			int ny = y + dy[k];
			if (!(0 <= nx && nx <= N - 1 && 0 <= ny && ny <= M - 1)) continue;
			if (info[nx][ny] >= 0) continue;
			if (done.find(findParent(nx * M + ny)) != done.end()) continue;

			done.insert(parents[nx * M + ny]);
			count = (count - info[nx][ny]) % 10;
		}

		info[x][y] = count;
	}

	// Output
	for (i = 0; i < N; i++) {
		for (j = 0; j < M; j++) {
			if (info[i][j] > 0) cout << info[i][j];
			else cout << 0;
		}
		cout << "\n";
	}
}
