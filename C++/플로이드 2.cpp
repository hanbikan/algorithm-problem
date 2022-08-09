#include <iostream>
#include <vector>
#define REP(i, a, b) for(int i = (a);i<(b);i++)
#define INF 1000000001

using namespace std;

int w[101][101];
vector<int> routes[101][101];

void printRoute(vector<int> v) {
	cout << v.size() << " ";
	REP(i, 0, v.size()) {
		cout << v[i] << " ";
	}

	cout << "\n";
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int n;
	cin >> n;
	int m;
	cin >> m;
	
	REP(i, 1, 101) {
		REP(j, 1, 101) w[i][j] = INF;
	}
	REP(i, 1, n + 1) w[i][i] = 0;

	REP(i, 0, m) {
		int a, b, c;
		cin >> a >> b >> c;
		if (w[a][b] > c) {
			w[a][b] = c;

			vector<int> v;
			v.push_back(a);
			v.push_back(b);
			routes[a][b] = v;
		}
	}

	// 플로이드
	REP(k, 1, n+1) {
		REP(i, 1, n + 1) {
			REP(j, 1, n + 1) {
				if (w[i][j] > w[i][k] + w[k][j]) {
					w[i][j] = w[i][k] + w[k][j];

					vector<int> v = routes[i][k];
					v.insert(v.end(), routes[k][j].begin()+1, routes[k][j].end());
					routes[i][j] = v;
				}
			}
		 }
	}

	// Print 1
	REP(i, 1, n + 1) {
		REP(j, 1, n + 1) {
			if (w[i][j] == INF) cout << "0 ";
			else cout << w[i][j] << " ";
		}
		cout << "\n";
	}

	// Print 2
	REP(i, 1, n + 1) {
		REP(j, 1, n + 1) {
			printRoute(routes[i][j]);
		}
	}
}
