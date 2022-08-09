#include <bits/stdc++.h>
using namespace std;

int N, k;
// time, id, index
priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> counter;

// counter에서 가장 낮은 시간인 것들을 time, id, index -> index, time, id로 재배열하여 반환
priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> popCounter() {
	priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> res;
	int time = get<0>(counter.top());
	res.push({ get<2>(counter.top()), get<0>(counter.top()), get<1>(counter.top()) });
	counter.pop();

	while (!counter.empty() && time == get<0>(counter.top())) {
		res.push({ get<2>(counter.top()), get<0>(counter.top()), get<1>(counter.top()) });
		counter.pop();
	}

	return res;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0);

	cin >> N >> k;

	int i;
	for (i = 0; i < k; i++) {
		counter.push({ 0, 0, i });
	}

	long long sum = 0;
	int p;
	int id, w;

	// index, time, id
	priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> toInsert;
	
	for (i = 0; i < N; i++) {
		cin >> id >> w;

		if (toInsert.empty()) {
			toInsert = popCounter(); // counter -> toInsert
			p = i - (k - 1);
		}

		// 가장 왼쪽에 있는 테이블을 꺼냄
		tuple<int, int, int> top = toInsert.top();
		toInsert.pop();

		// 좌항: 나가는 순서, 우항: id
		sum += (p + toInsert.size()) * get<2>(top);

		// 시간을 계속해서 누적합하는 방식으로 입력 값을 counter에 채워넣음
		counter.push({ get<1>(top) + w, id, get<0>(top) });
	}

	// 남아있는 고객 처리
	for (; i < N+k;i++) {
		if (toInsert.empty()) {
			toInsert = popCounter();
			p = i - (k - 1);
		}

		tuple<int, int, int> top = toInsert.top();
		toInsert.pop();

		sum += (p + toInsert.size()) * get<2>(top);
	}

	cout << sum;

	return 0;
}