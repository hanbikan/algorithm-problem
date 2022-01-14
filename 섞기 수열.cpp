#include <bits/stdc++.h>
using namespace std;

int N;
int A[20001];
bool isVisited[20001];

int gcd(int x, int y) {
	if (y != 0) {
		return gcd(y, x % y);
	}
	else {
		return x;
	}
}

long long lcm(long long x, long long y) {
	return (x * y) / gcd(x, y);
}

int getCount(int n, int count) {
	// 이미 방문을 했다는 것은 탐색 시작점이라는 것을 말해준다
	if (isVisited[n]) return count;
	else {
		isVisited[n] = true;
		return getCount(A[n], count + 1);
	}
}

void solution() {
	int i;
	int res = 1;
	for (i = 1; i < N + 1; i++) {
		if (isVisited[i]) continue;
		res = lcm(res, getCount(i, 0));
	}

	cout << res;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	cin >> N;
	
	int i;
	for (i = 1; i < N + 1; i++) {
		cin >> A[i];
	}

	solution();

	return 0;
}
