#include <iostream>
#include <map>
using namespace std;

map<char, pair<int, int>> dir;
char info[1000][1000];

bool isSearchIndependent(int x, int y) {
	if (info[x][y] == 0) return true;
	else if (info[x][y] == 1) return false;

	char c = info[x][y];
	info[x][y] = 0;	// 이번 탐색 때 방문
	bool res = isSearchIndependent(x + dir[c].first, y + dir[c].second);
	info[x][y] = 1;	// 이전 탐색 때 방문

	return res;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	dir.insert(make_pair('U', make_pair(-1, 0)));
	dir.insert(make_pair('D', make_pair(1, 0)));
	dir.insert(make_pair('L', make_pair(0, -1)));
	dir.insert(make_pair('R', make_pair(0, 1)));

	int N, M;
	cin >> N >> M;

	int i, j;
	for (i = 0; i < N; i++) {
		for (j = 0; j < M; j++) cin >> info[i][j];
	}

	// Solution
	int count = 0;
	for (i = 0; i < N; i++) {
		for (j = 0; j < M; j++) {
			if (isSearchIndependent(i, j)) count++;
		}
	}
	cout << count;
}