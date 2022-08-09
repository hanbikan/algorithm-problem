#include <bits/stdc++.h>
#define INF 300
using namespace std;

pair<int, int> s;
pair<int, int> e;
int dx, dy;
double a;
double c;

double getYFromLinear(double x) {
	return a * x + c;
}

double getDistance(pair<int, int> p1, pair<int, int> p2) {
	return sqrt(pow(p1.first - p2.first, 2) + pow(p1.second - p2.second, 2));
}

void solution() {
	int x = e.first;
	double y, curDist;
	double prevDist = INF;
	int prevX = -1;
	int prevY = -1;

	int offset = 1;
	if (dx < 0) offset = -1;

	for (x = e.first;;x+=offset) {
		y = getYFromLinear(x);
		if (y != (int)y) continue;

		curDist = getDistance(s, { x, y });

		if (curDist > prevDist) break;

		prevDist = curDist;
		prevX = x;
		prevY = y;
	}

	cout << prevX << " " << prevY;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);


	int tmp1, tmp2;
	cin >> tmp1 >> tmp2;
	s = make_pair(tmp1, tmp2);

	cin >> tmp1 >> tmp2;
	e = make_pair(tmp1, tmp2);

	cin >> dx >> dy;
	if (dx == 0) {
		int x, y;
		if(dy > 0) {
			x = e.first;
			if (e.second >= s.second) y = e.second;
			else y = s.second;
		}
		else {
			x = e.first;
			if (e.second <= s.second) y = e.second;
			else y = s.second;
		}
		cout << x << " " << y;
	}
	else {
		a = (double)dy / (double)dx;

		// Linear: y = ax + c
		c = e.second - e.first * a;

		solution();
	}

	return 0;
}
