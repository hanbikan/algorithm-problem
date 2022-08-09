#include <iostream>
#include <map>
#define UP 0
#define LEFT 1
#define FRONT 2
#define RIGHT 3
#define BACK 4
#define DOWN 5	
#define UP_POS {{0,0},{0,1},{0,2}}
#define RIGHT_POS {{0,2},{1,2},{2,2}}
#define DOWN_POS {{2,2},{2,1},{2,0}}
#define LEFT_POS {{2,0},{1,0},{0,0}}

using namespace std;

int cube[6][3][3];

void rotate(int index, bool isClockwise) {
	int i, j, k;

	// * 영향받는 4면의 데이터 처리	 
	int offset = -1;
	int to = 1;
	if (!isClockwise) {
		offset = 1;
		to = 3;
	}

	// clockwiseDimension[UP]: UP을 돌릴 때 영향받는 면들의 순서가 L,B,R,F 이다.
	int clockwiseDimension[6][4] = {
		{LEFT,BACK,RIGHT,FRONT},{UP,FRONT,DOWN,BACK},
		{UP,RIGHT,DOWN,LEFT},{UP,BACK,DOWN,FRONT},
		{UP,LEFT,DOWN,RIGHT},{LEFT,FRONT,RIGHT,BACK}
	};

	// clockwiseDimensionSequence[UP][L]: UP을 돌릴 때 L에서 영향받는 좌표들의 순서
	pair<int, int> clockwiseDimensionSequence[6][4][3] = {
		{UP_POS,UP_POS,UP_POS,UP_POS}, // UP
		{LEFT_POS,LEFT_POS,RIGHT_POS,RIGHT_POS}, // LEFT
		{DOWN_POS,LEFT_POS,DOWN_POS,RIGHT_POS}, // FRONT
		{RIGHT_POS,LEFT_POS,LEFT_POS,RIGHT_POS}, // RIGHT			  
		{UP_POS,LEFT_POS,UP_POS,RIGHT_POS}, // BACK		  
		{DOWN_POS,DOWN_POS,DOWN_POS,DOWN_POS} // DOWN
	};

	// ABCD -> BCDA를 만드는 것을 상기하라
	// 'A'를 저장
	int tmp[3];
	for (j = 0; j < 3; j++) {
		int x = clockwiseDimensionSequence[index][0][j].first;
		int y = clockwiseDimensionSequence[index][0][j].second;
		tmp[j] = cube[clockwiseDimension[index][0]][x][y];
	}

	// BCDD
	i = 0;
	for (k=0;k<3;k++) {
		int curDimension = clockwiseDimension[index][i];
		int nextDimension = clockwiseDimension[index][(i + offset + 4)%4];

		for (j = 0; j < 3; j++) {
			pair<int, int> curPos = clockwiseDimensionSequence[index][i][j];
			pair<int, int> nextPos = clockwiseDimensionSequence[index][(i + offset + 4) % 4][j];

			cube[curDimension][curPos.first][curPos.second] = cube[nextDimension][nextPos.first][nextPos.second];
		}

		i = (i + offset + 4) % 4;
	}

	// BCDA
	for (j = 0; j < 3; j++) {
		int x = clockwiseDimensionSequence[index][to][j].first;
		int y = clockwiseDimensionSequence[index][to][j].second;
		cube[clockwiseDimension[index][to]][x][y] = tmp[j];
	}


	// * 대상 면의 회전 처리  
	i = 7;
	int saveIndex = 6;
	int loadIndex = 0;
	offset = -1;
	if (!isClockwise) {
		i = 0;
		saveIndex = 0;
		loadIndex = 6;
		offset = 1;
	}

	// rotation을 따라 2칸을 건너뛰어 복제하는 로직
	pair<int, int> rotation[] = {
		{ 0, 0 }, { 0,1 }, { 0,2 }, { 1,2 }, { 2,2 }, { 2,1 }, { 2,0 }, { 1,0 }
	};

	// 임시 저장
	tmp[0] = cube[index][rotation[saveIndex].first][rotation[saveIndex].second];
	tmp[1] = cube[index][rotation[saveIndex+1].first][rotation[saveIndex+1].second];

	// 8개 중 6개를 채워준다
	for (k = 0; k < 6; k++) {
		cube[index][rotation[i].first][rotation[i].second] = cube[index][rotation[(i + offset*2 + 8) % 8].first][rotation[(i + offset*2 + 8) % 8].second];
		i = (i + offset + 8) % 8;
	}

	// 나머지 2개를 임시 저장된 데이터를 넣어준다
	cube[index][rotation[loadIndex].first][rotation[loadIndex].second] = tmp[0];
	cube[index][rotation[loadIndex+1].first][rotation[loadIndex+1].second] = tmp[1];
}

void printDimension(int direction) {
	char colors[6] = { 'w', 'g', 'r', 'b', 'o', 'y' };
	int i, j;
	for (i = 0; i < 3; i++) {
		for (j = 0; j < 3; j++) {
			cout << colors[cube[direction][i][j]];
		}
		cout << "\n";
	}
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	map<char, int> dimensionForDirection = {
		{'U', 0}, {'L', 1},{'F',2},{'R',3},{'B',4},{'D',5}
	};

	int t, k;
	cin >> t;
	for (k = 0; k < t; k++) {
		int d, i, j;

		// Init a cube
		for (d = 0; d < 6; d++) {
			for (i = 0; i < 3; i++) {
				for (j = 0; j < 3; j++) cube[d][i][j] = d;
			}
		}

		// Input
		int n;
		cin >> n;

		// Solution
		for (i = 0; i < n; i++) {
			char dim, clockwise;
			cin >> dim >> clockwise;

			rotate(dimensionForDirection[dim], clockwise == '+');
		}

		printDimension(UP);
	}
}
