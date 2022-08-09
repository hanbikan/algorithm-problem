#include <iostream>
using namespace std;
#define INF 10000001

int graph[101][101];

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int n, m;
	cin >> n >> m;

	int i, j, k;
	for (i = 0; i < 101; i++) {
		for (j = 0; j < 101; j++) graph[i][j] = INF;
	}

	for (i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		graph[a][b] = min(graph[a][b], c);
	}

	// Solution
	for (k = 1; k < n+1; k++) {
		for (i = 1; i < n + 1; i++) {
			for (j = 1; j < n + 1; j++) {
				graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
			}
		}
	}

	// Print
	for (i = 1; i < n+1; i++) {
		for (j = 1; j < n + 1; j++) {
			if (i == j || graph[i][j] == INF) cout << "0 ";
			else cout << graph[i][j] << " ";
		 }
		cout << "\n";
	}

	return 0;
}
