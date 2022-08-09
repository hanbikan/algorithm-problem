#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> graph[501];
bool isVisited[501];
bool isTree;

void setIsTree(int node, int prev) {
	if (isVisited[node]) {
		isTree = false;
		return;
	}

	isVisited[node] = true;

	int i;
	for (i = 0; i < graph[node].size(); i++) {
		int next = graph[node].at(i);
		if (next != prev) setIsTree(next, node);
	}
}

int getTreeCount() {
	int i, res = 0;

	for (i = 1; i < n + 1; i++) {
		if (!isVisited[i]) {
			isTree = true;
			setIsTree(i, 0);
			if (isTree) res += 1;
		}
	}

	return res;
}

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int caseCount = 1;
	while (1) {
		int i;

		cin >> n >> m;
		if (n == 0 && m == 0) break;

		// 초기화
		for (i = 1; i < n + 1; i++) {
			graph[i].clear();
			isVisited[i] = false;
		}

		// 입력
		for (i = 0; i < m; i++) {
			int a, b;
			cin >> a >> b;
			graph[a].push_back(b);
			graph[b].push_back(a);
		}

		// Solution
		cout << "Case " << caseCount << ": ";

		int treeCount = getTreeCount();
		if (treeCount == 0) cout << "No trees.\n";
		else if (treeCount == 1) cout << "There is one tree.\n";
		else cout << "A forest of " << treeCount << " trees.\n";

		caseCount++;
	}

	return 0;
}