#include <bits/stdc++.h>
#define INF 1000001
using namespace std;

int m, n;
vector<pair<int, int>> constellation; // 별자리
vector<pair<int, int>> stars;
set<pair<int, int>> starsSet;

pair<int, int> checkConstellationAndGetDiff(int starIndex) {
	int pivotX = constellation.at(0).first;
	int pivotY = constellation.at(0).second;
	int diffX = stars.at(starIndex).first - pivotX;
	int diffY = stars.at(starIndex).second - pivotY;

	int i;
	for (i = 1; i < m; i++) {
		int x = constellation.at(i).first + diffX;
		int y = constellation.at(i).second + diffY;
		if (starsSet.find({ x,y }) == starsSet.end()) return { INF,INF };
	}
	return { diffX,diffY };
}

void solution() {
	int i;
	for (i = 0; i < n; i++) {
		pair<int, int> res = checkConstellationAndGetDiff(i);
		if (res.first != INF) {
			cout << res.first << " " << res.second;
			break;
		}
	}
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int i, x, y;
	cin >> m;
	for (i = 0; i < m; i++) {
		cin >> x >> y;
		constellation.push_back({x,y});
	}

	cin >> n;
	for (i = 0; i < n; i++) {
		cin >> x >> y;
		stars.push_back({ x,y });
		starsSet.insert({ x,y });
	}

	solution();

	return 0;
}
