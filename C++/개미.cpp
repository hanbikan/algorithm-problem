#include <bits/stdc++.h>
#define MAX_LOG 16 //log2(100000)
using namespace std;

int n;
int energy[100001];
vector<pair<int, int>> graph[100001];
pair<int, int> table[MAX_LOG][100001];
int level[100001];

void setGraphSparseAndLevel() {
	level[1] = 0;

	queue<int> q;
	q.push(1);

	int i, cur, next, curLevel = 1;
	while (!q.empty()) {
		queue<int> nq;

		while (!q.empty()) {
			cur = q.front();
			q.pop();

			vector<int> toErase;

			for (i = 0; i < graph[cur].size(); i++) {
				next = graph[cur].at(i).first;

				if (level[next] == 0 && next != 1) {
					nq.push(next);
					level[next] = curLevel;

					toErase.push_back(i);
				}
			}

			// 1부터 시작하는 edges들을 모두 지움
			for (i = toErase.size()-1; i >= 0; i--) {
				graph[cur].erase(graph[cur].begin() + toErase.at(i));
			}
		}

		q = nq;
		curLevel++;
	}

	graph[1].push_back({ 1,0 });
}

void setTable() {
	int i;
	for (i = 1; i < n + 1; i++) {
		table[0][i] = graph[i].at(0);
	}

	int k;
	for (k = 1; k < MAX_LOG; k++) {
		for (i = 1; i < n + 1; i++) {
			int midNode = table[k - 1][i].first;
			int midCost = table[k - 1][i].second;

			table[k][i].first = table[k - 1][midNode].first;
			table[k][i].second = table[k - 1][midNode].second + midCost;
		}
	}
}

pair<int, int> moveAndGetPair(int node, int k) {
	int curNode = node;
	int curCost = 0;
	int i;
	for (i = MAX_LOG; i >= 0; i--) {
		if ((k & (1 << i)) != 0) {
			curCost += table[i][curNode].second;
			curNode = table[i][curNode].first;
		}
	}

	return {curNode, curCost};
}

void solution() {
	setGraphSparseAndLevel();
	setTable();

	int i;
	for (i = 1; i < n + 1; i++) {
		int left = 0;
		int right = level[i];

		while (left <= right) {
			int mid = (left + right) / 2;

			pair<int, int> pair = moveAndGetPair(i, mid);
			if (pair.second <= energy[i]) {
				left = mid + 1;
			}
			else {
				right = mid - 1;
			}
		}

		cout << moveAndGetPair(i, right).first << "\n";
	}
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	cin >> n;
	
	int i;
	for (i = 1; i < n+1; i++) {
		cin >> energy[i];
	}

	int a, b, c;
	for (i = 0; i < n - 1; i++) {
		cin >> a >> b >> c;
		graph[a].push_back({ b, c });
		graph[b].push_back({ a, c });
	}

	solution();

	return 0;
}
