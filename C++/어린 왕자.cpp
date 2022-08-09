#include <iostream>
#include <math.h>
using namespace std;

bool isPointInCircle(int x, int y, int cx, int cy, int r) {
	// (cx - x)^2 + (cy - y)^2 <= r^2
	int left = pow(x - cx, 2) + pow(y - cy, 2);
	int right = pow(r, 2);

	return left <= right;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int T;
	cin >> T;
	
	int i, j;
	for (i = 0; i < T; i++) {
		int res = 0;
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;

		int n;
		cin >> n;

		for (j = 0; j < n; j++) {
			int cx, cy, r;
			cin >> cx >> cy >> r;
			res += isPointInCircle(x1, y1, cx, cy, r) ^ isPointInCircle(x2, y2, cx, cy, r);
		}

		cout << res << "\n";
	}
}
