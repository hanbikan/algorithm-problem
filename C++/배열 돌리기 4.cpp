#include <bits/stdc++.h>
#define INF 5001
using namespace std;

int N, M, K;
int matrix[50][50];
tuple<int, int, int> op[6];
bool isSelected[6];
int minMatrixValue = INF;

void rotateMatrixClockwise(int r, int c, int s) {
	if (s <= 0) return;

	int tmp = matrix[r - s][c - s];
	int i, j;

	// left
	j = c - s;
	for (i = r - s + 1; i < r + s + 1; i++) {
		matrix[i - 1][j] = matrix[i][j];
	}

	// bottom
	i = r + s;
	for (j = c - s + 1; j < c + s + 1; j++) {
		matrix[i][j - 1] = matrix[i][j];
	}

	// right
	j = c + s;
	for (i = r + s - 1; i > r - s - 1; i--) {
		matrix[i + 1][j] = matrix[i][j];
	}

	// top
	i = r - s;
	for (j = c + s - 1; j > c - s; j--) {
		matrix[i][j + 1] = matrix[i][j];
	}

	matrix[r-s][c-s+1] = tmp;
	rotateMatrixClockwise(r, c, s - 1);
}

void rotateMatrixCounterclockwise(int r, int c, int s) {
	if (s <= 0) return;

	int tmp = matrix[r - s][c - s];
	int i, j;

	// top
	i = r - s;
	for (j = c - s + 1; j < c + s + 1; j++) {
		matrix[i][j - 1] = matrix[i][j];
	}

	// right
	j = c + s;
	for (i = r - s + 1; i < r + s + 1; i++) {
		matrix[i - 1][j] = matrix[i][j];
	}

	// bottom
	i = r + s;
	for (j = c + s - 1; j > c - s - 1; j--) {
		matrix[i][j + 1] = matrix[i][j];
	}

	// left
	j = c - s;
	for (i = r + s - 1; i > r - s; i--) {
		matrix[i + 1][j] = matrix[i][j];
	}

	matrix[r - s + 1][c - s] = tmp;
	rotateMatrixCounterclockwise(r, c, s - 1);
}

int getMatrixValue() {
	int res = INF;

	int i, j;
	for (i = 0; i < N; i++) {
		int rowSum = 0;
		for (j = 0; j < M; j++) {
			rowSum += matrix[i][j];
		}
		res = min(res, rowSum);
	}

	return res;
}

void setMinMatrixValueRecursively(int left) {
	if (left == 0) {
		minMatrixValue = min(minMatrixValue, getMatrixValue());
		return;
	}

	int i;
	for (i = 0; i < K; i++) {
		if (isSelected[i]) continue;

		rotateMatrixClockwise(get<0>(op[i]), get<1>(op[i]), get<2>(op[i]));
		isSelected[i] = true;

		setMinMatrixValueRecursively(left - 1);

		rotateMatrixCounterclockwise(get<0>(op[i]), get<1>(op[i]), get<2>(op[i]));
		isSelected[i] = false;
	}
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int i, j;

	// 입력 1
	cin >> N >> M >> K;

	// Matrix 입력 2
	for (i = 0; i < N; i++) {
		for (j = 0; j < M; j++) {
			cin >> matrix[i][j];
		}
	}

	// 입력 3
	for (i = 0; i < K; i++) {
		int r, c, s;
		cin >> r >> c >> s;
		r--; c--;

		op[i] = make_tuple(r, c, s);
	}

	// Solution
	setMinMatrixValueRecursively(K);
	cout << minMatrixValue;

	return 0;
}
