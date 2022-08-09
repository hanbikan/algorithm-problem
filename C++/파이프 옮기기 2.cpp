#include <bits/stdc++.h>
#define ROW 0
#define DIAGONAL 1
#define COLUMN 2
using namespace std;

int N;
int matrix[32][32];
vector<int> availableDir[3];
int dx[3] = { 0,1,1 };
int dy[3] = { 1,1,0 };
long long dp[32][32][3];

long long getCount(int x, int y, int dir) {
	if (dp[x][y][dir] != -1) return dp[x][y][dir];

	dp[x][y][dir] = 0;
	int k;

	for (k = 0; k < 3; k++) {
		int nDir = dir - 1 + k;

		if (0 <= nDir && nDir <= 2) {
			int nx = x + dx[nDir];
			int ny = y + dy[nDir];

			// 범위 초과
			if (!(0 <= nx && nx <= N - 1 && 0 <= ny && ny <= N - 1)) continue;

			// 방향에 따라 빈칸(0) 체크
			if (nDir == 1) {
				if (!(matrix[nx][ny] == 0 &&
					matrix[x + dx[0]][y + dy[0]] == 0 &&
					matrix[x + dx[2]][y + dy[2]] == 0)) continue;
			}
			else {
				if (!(matrix[nx][ny] == 0)) continue;
			}

			dp[x][y][dir] += getCount(nx, ny, nDir);
		}
	}

	return dp[x][y][dir];
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	// Input
	cin >> N;

	int i, j, k;
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			cin >> matrix[i][j];
		}
	}

	// Initialize availableDir
	availableDir[ROW].push_back(ROW);
	availableDir[ROW].push_back(DIAGONAL);
	availableDir[DIAGONAL].push_back(ROW);
	availableDir[DIAGONAL].push_back(DIAGONAL);
	availableDir[DIAGONAL].push_back(COLUMN);
	availableDir[COLUMN].push_back(DIAGONAL);
	availableDir[COLUMN].push_back(COLUMN);

	// Initialize dp
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			for (k = 0; k < 3; k++) {
				dp[i][j][k] = -1;
			}
		}
	}
	for (k = 0; k < 3; k++) {
		dp[N - 1][N - 1][k] = 1;
	}

	// Solution
	cout << getCount(0, 1, ROW);

	return 0;
}
