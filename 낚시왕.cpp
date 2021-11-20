#include <iostream>
#include <vector>
using namespace std;

struct Shark {
	bool isAlive;
	int x, y;
	int speed;
	int dir;
	int size;
};

int R, C;
vector<Shark> sharks;
int map[101][101]; // sharks의 인덱스들 저장
int nextMap[101][101];  

// 상 하 우 좌
int dx[5] = { 0, -1, 1, 0, 0 };
int dy[5] = { 0, 0, 0, 1, -1};

int catchShark(int y) {
	int res = 0;

	int i;
	for (i = 1; i < R+1; i++) {
		if (map[i][y] != 0 && sharks[map[i][y]].isAlive) {
			res = sharks[map[i][y]].size;
			sharks[map[i][y]].isAlive = false;
			map[i][y] = 0;
			break;
		}
	}

	return res;
}

pair<int, int> getNextPosition(int index, int x, int y) {
	// 상, 하
	if (sharks[index].dir <= 2) {
		// Set nx
		int offsetX = (dx[sharks[index].dir] * (sharks[index].speed % (2 * (R - 1))));
		int nx = x + offsetX;
		if (offsetX >= 0) {
			if (nx >= 2 * R - 1) nx -= 2 * (R - 1);
			else if (nx >= R) {
				if (sharks[index].dir % 2 == 0) sharks[index].dir--;
				else sharks[index].dir++;
				nx = 2 * R - nx;
			}
		}
		else {
			if (nx <= -R + 2) nx += 2 * (R - 1);
			else if (nx <= 1) {
				if (sharks[index].dir % 2 == 0) sharks[index].dir--;
				else sharks[index].dir++;
				nx = 2 - nx;
			}
		}

		return { nx, y };
	}
	// 좌, 우
	else {
		// Set ny
		int offsetY = (dy[sharks[index].dir] * (sharks[index].speed % (2 * (C - 1))));
		int ny = y + offsetY;

		if (offsetY >= 0) {
			if (ny >= 2 * C - 1) ny -= 2 * (C - 1);
			else if (ny >= C) {
				if (sharks[index].dir % 2 == 0) sharks[index].dir--;
				else sharks[index].dir++;
				ny = 2 * C - ny;
			}
		}
		else {
			if (ny <= -C + 2) ny += 2 * (C - 1);
			else if (ny <= 1) {
				if (sharks[index].dir % 2 == 0) sharks[index].dir--;
				else sharks[index].dir++;
				ny = 2 - ny;
			}
		}

		return { x, ny };
	}
}

void moveShark(int x, int y, int nx, int ny) {
	// 중복 X
	if (nextMap[nx][ny] == 0)
		nextMap[nx][ny] = map[x][y];
	// 위치가 겹치면서 현재 이동할 상어가 더 큰 경우
	else if (sharks[map[x][y]].size > sharks[nextMap[nx][ny]].size) {
		sharks[nextMap[nx][ny]].isAlive = false;
		nextMap[nx][ny] = map[x][y];
	}
	// 위치가 겹치지만 현재 이동할 상어가 더 작은 경우
	else
		sharks[map[x][y]].isAlive = false;
}

void moveSharks() {
	int i, j;

	// Init nextMap
	for (i = 1; i < R + 1; i++) {
		for (j = 1; j < C + 1; j++) nextMap[i][j] = 0;
	}

	// Set nextMap depending on sharks
	for (i = 1; i < sharks.size(); i++) {
		if (!sharks[i].isAlive) continue;

		int x = sharks[i].x;
		int y = sharks[i].y;

		pair<int, int> nextPos = getNextPosition(i, x, y);
		int nx = nextPos.first;
		int ny = nextPos.second;

		sharks[i].x = nx;
		sharks[i].y = ny;

		moveShark(x, y, nx, ny);
	}

	// Deepcopy: map <- nextMap
	for (i = 1; i < R + 1; i++) {
		for (j = 1; j < C + 1; j++) map[i][j] = nextMap[i][j];
	}
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int M;
	cin >> R >> C >> M;

	sharks.push_back(Shark());
	int i, j;

	// Init map
	for (i = 1; i < R + 1; i++) {
		for (j = 1; j < C + 1; j++) map[i][j] = 0;
	}

	for (i = 0; i < M; i++) {
		int r, c, s, d, z;
		cin >> r >> c >> s >> d >> z;

		Shark sh;
		sh.isAlive = true;  sh.x = r; sh.y = c;
		sh.speed = s; sh.dir = d; sh.size = z;
		sharks.push_back(sh);

		map[r][c] = sharks.size() - 1;
	}

	// Solution
	int res = 0;
	for (j = 1; j < C+1; j++) {
		res += catchShark(j);
		moveSharks();
	}
	cout << res;
}
