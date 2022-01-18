#include <bits/stdc++.h>
using namespace std;

int K;
int nums[1024];

void f(int start, int end) {
	queue<pair<int, int>> q;
	q.push({ start,end });

	while (!q.empty()) {
		queue<pair<int, int>> nq;
		while (!q.empty()) {
			int s = q.front().first;
			int e = q.front().second;
			int m = (s + e) / 2;
			q.pop();
			cout << nums[m] << " ";

			if (s != e) {
				nq.push({ s,m - 1 });
				nq.push({ m + 1, e });
			}
		}
		cout << "\n";
		q = nq;
	}
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	cin >> K;
	int i;
	for (i = 1; i < pow(2, K); i++) {
		cin >> nums[i];
	}

	f(1, pow(2, K) - 1);

	return 0;
}