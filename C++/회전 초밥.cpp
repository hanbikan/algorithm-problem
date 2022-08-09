#include <bits/stdc++.h>
using namespace std;

int N, d, k, c;
int sushi[3000000];
int typeCount[3001];
int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	// 접시의 수, 초밥 가짓수, 연속, 쿠폰
	cin >> N >> d >> k >> c;

	int i;
	for (i = 0; i < N; i++) {
		cin >> sushi[i];
	}

	// Solution
	int res = 0;
	int dCount = 0;
	for (i = 0; i < k; i++) {
		typeCount[sushi[i]]++;
		if (typeCount[sushi[i]] == 1) dCount++;

		if (typeCount[c] == 0) res = max(res, dCount + 1);
		else res = max(res, dCount);
	}
	
	for (i = k; i < N+k; i++) {
		typeCount[sushi[i % N]]++;
		if (typeCount[sushi[i % N]] == 1) dCount++;
		typeCount[sushi[(i - k) % N]]--;
		if (typeCount[sushi[(i-k) % N]] == 0) dCount--;

		if (typeCount[c] == 0) res = max(res, dCount + 1);
		else res = max(res, dCount);
	}

	cout << res;

	return 0;
}