#include <iostream>
using namespace std;

int parents[500001];

int find(int x) {
	if (x == parents[x]) return x;

	return find(parents[x]);
}

void doUnion(int x, int y) {
	int parent_x = find(parents[x]);
	int parent_y = find(parents[y]);

	if (parent_x < parent_y) parents[parent_y] = parent_x;
	else parents[parent_x] = parent_y;
}

int main()
{
	int i;

	int n, m;
	cin >> n >> m;

	for (i = 1; i < n + 1; i++) parents[i] = i;

	int res = 0;
	for (i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;

		if (find(a) == find(b)) {
			res = i + 1;
			break;
		}
		else doUnion(a, b);
	}

	cout << res;

	return 0;
}
