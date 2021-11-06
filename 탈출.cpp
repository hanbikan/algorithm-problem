#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;

char map[50][50];
int isVisited[50][50];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

vector<pair<int, int>> waters;
int R, C;

int bfs(int startX, int startY);
void moveWaters();
bool isPositionInRange(int x, int y);

int bfs(int startX, int startY) {
	int res = 0;
	queue<pair<int, int>> q;
	q.push(make_pair(startX, startY));

	while (!q.empty()) {
		res++;
		queue<pair<int, int>> nextQ;
		moveWaters();

		while (!q.empty()) {
			int x = q.front().first;
			int y = q.front().second;
			q.pop();

			isVisited[x][y] = 1;
			
			for (int i = 0; i < 4; i++) {
				int nextX = x + dx[i];
				int nextY = y + dy[i];

				if (isPositionInRange(nextX, nextY) && isVisited[nextX][nextY] == 0) {
					if (map[nextX][nextY] == '.') {
						nextQ.push(make_pair(nextX, nextY));
						isVisited[nextX][nextY] = 1;
					}
					else if (map[nextX][nextY] == 'D') return res;
				}
			}
		}
		q = nextQ;
	}

	return 0;
}

void moveWaters() {
	vector<pair<int, int>> nextWaters;

	for (int i = 0; i < waters.size(); i++) {
		int x = waters[i].first;
		int y = waters[i].second;
		for (int j = 0; j < 4; j++) {
			int nextX = x + dx[j];
			int nextY = y + dy[j];

			if (isPositionInRange(nextX, nextY) && map[nextX][nextY] == '.') {
				map[nextX][nextY] = '*';
				nextWaters.push_back(make_pair(nextX, nextY));
											  			}
		}
	}

	waters = nextWaters;
}

bool isPositionInRange(int x, int y) {
	if (0 <= x && x <= R - 1 && 0 <= y && y <= C - 1) return true;
	else return false;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	cin >> R >> C;
	
	int startX, startY;
	int i, j;
	for (i = 0; i < R; i++) {
		for (j = 0; j < C; j++) {
			cin >> map[i][j];
			if (map[i][j] == '*') waters.push_back(make_pair(i, j));
			else if (map[i][j] == 'S') {
				startX = i;
				startY = j;
				map[i][j] = '.';
			}
		}
	}

	int res = bfs(startX, startY);
	if (res == 0) cout << "KAKTUS";
	else cout << res;

	return 0;
}
