#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int N, M;
int in[1001];
vector<int> graph[1001];
int result[1001];

void solution() {
	// 큐 초기화
	queue<int> q;
	int i;
	for (i = 1; i < N + 1; i++) {
		if (in[i] == 0) {
			q.push(i);
			result[i] = 1;
		}
	}

	// 레벨 단위 위상정렬
	int level = 2;
	while (!q.empty()) {
		queue<int> nq;

		while (!q.empty()) {
			int cur = q.front(); q.pop();

			for (i = 0; i < graph[cur].size(); i++) {
				int next = graph[cur].at(i);

				in[next] -= 1;
				if (in[next] == 0) {
					nq.push(next);
					result[next] = level;
				}
			}
		}

		q = nq;
		level++;
	}

	// 출력
	for (i = 1; i < N + 1; i++) cout << result[i] << " ";
}

int main()
{
	cin >> N >> M;

	int i;
	for (i = 0; i < M; i++) {
		int A, B;
		cin >> A >> B;
		graph[A].push_back(B);
		in[B] += 1;
	}

	solution();

	return 0;
}
