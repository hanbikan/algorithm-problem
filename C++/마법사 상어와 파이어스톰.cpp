#include <bits/stdc++.h>
using namespace std;

int N, Q;
int length;
int A[64][64];
int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };

// Rotate A[][] clockwise in 90 degree
void rotateMatrix(int startX, int startY, int len) {
	int i, j;

	// Set tmp
	int tmp[63];
	i = 0;
	for (j = len - 1; j > 0; j--) {
		tmp[i] = A[startX][startY + j];
		i++;
	}

	// Top
	i = 0;
	for (j = len - 1; j > 0; j--) {
		A[startX + i][startY + j] = A[startX + (len - 1) - j][startY];
	}

	// Left
	j = 0;
	for (i = 0; i < len - 1; i++) {
		A[startX + i][startY + j] = A[startX + len - 1][startY + i];
	}

	// Bottom
	i = len - 1;
	for (j = 0; j < len - 1; j++) {
		A[startX + i][startY + j] = A[startX + (len - 1) - j][startY + len - 1];
	}

	// Right using tmp
	j = len - 1;
	for (i = len - 1; i > 0; i--) {
		A[startX + i][startY + j] = tmp[(len - 1) - i];
	}


	// Recursion
	if (len > 2) {
		rotateMatrix(startX + 1, startY + 1, len - 2);
	}
}

void doFirestorm(int L) {
	int len = pow(2, L);

	// Rotate
	int i, j;
	for (i = 0; i < length; i += len) {
		for (j = 0; j < length; j += len) {
			rotateMatrix(i, j, len);
		}
	}

	// Set toDecrease
	int k;
	vector<pair<int, int>> toDecrease;
	for (i = 0; i < length; i++) {
		for (j = 0; j < length; j++) {
			// Set iceCount
			int iceCount = 0;
			for (k = 0; k < 4; k++) {
				int nx = i + dx[k];
				int ny = j + dy[k];
				if (0 <= nx && nx <= length - 1 &&
					0 <= ny && ny <= length - 1) {
					if (A[nx][ny] != 0) iceCount++;
				}
			}

			// Copy and decrease the ice
			if (iceCount <= 2) {
				toDecrease.push_back({ i, j });
			}
		}
	}

	// Decrease ices
	for (i = 0; i < toDecrease.size(); i++) {
		int x = toDecrease.at(i).first;
		int y = toDecrease.at(i).second;
		
		A[x][y] = max(0, A[x][y] - 1);
	}
}

int getIceArea(int x, int y) {
	if (A[x][y] <= 0) return 0;

	A[x][y] *= -1; // Visited 처리

	int res = 0;
	int k;
	for (k = 0; k < 4; k++) {
		int nx = x + dx[k];
		int ny = y + dy[k];
		if (0 <= nx && nx <= length - 1 &&
			0 <= ny && ny <= length - 1) {
			res += getIceArea(nx, ny);
		}
	}

	return res + 1;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	// Input
	cin >> N >> Q;
	length = pow(2, N);

	int i, j;
	for (i = 0; i < length; i++) {
		for (j = 0; j < length; j++) {
			cin >> A[i][j];
		}
	}

	// 명령 수행
	int L;
	for (i = 0; i < Q; i++) {
		cin >> L;
		doFirestorm(L);
	}

	// 1. 남아있는 얼음의 합
	// 2. 가장 큰 덩어리가 차지하는 칸의 개수
	int iceSum = 0;
	int maxIceArea = 0;
	for (i = 0; i < length; i++) {
		for (j = 0; j < length; j++) {
			iceSum += abs(A[i][j]);
			maxIceArea = max(maxIceArea, getIceArea(i, j));
		}
	}
	cout << iceSum << "\n" << maxIceArea << "\n";

	return 0;
}
