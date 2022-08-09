#include <bits/stdc++.h>
using namespace std;

int N, M, K;
int positions[50];

void solution() {
	string res;

	int start = 0;
	int end = N;

	while (start <= end) {
		int mid = (start + end) / 2;
		
		// 사전상 늦은 순서를 출력해야하므로 첫번째 자리를 선택을 강제한다.
		string cur = "1";
		int selected = 1;
		int prev = 0;
		
		// Set cur
		int i;
		for (i = 1; i < K; i++) {
			if (positions[i] - positions[prev] >= mid) {
				cur += "1";
				selected++;
				prev = i;

				if (selected == M) break;
			}
			else {
				cur += "0";
			}
		}

		// 오른쪽에 0 채우기(M번 선택해서 중간에 빠져나올 경우)
		while (cur.size() < K) cur += "0";

		// 충분히 많이 선택했을 때는 mid값을 증가시킨다.
		if (selected == M) {
			start = mid + 1;
			res = cur;
		}
		// vice versa
		else {
			end = mid - 1;
		}
	}

	cout << res;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int i;
	cin >> N >> M >> K;
	for (i = 0; i < K; i++) cin >> positions[i];

	solution();

	return 0;
}