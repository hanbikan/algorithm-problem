#include <iostream>
using namespace std;

int isVisited[1001];
int nums[1001];

void dfs(int node) {
	isVisited[node] = 1;
	if (isVisited[nums[node]] == 0) dfs(nums[node]);
}

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0); 

	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		int res = 0;
		int j;

		int N;
		cin >> N;

		for (j = 1; j < N + 1; j++) isVisited[j] = 0;

		for(j = 1; j < N + 1; j++) cin >> nums[j];

		for (j = 1; j < N + 1; j++) {
			if (isVisited[j] == 0) {
				res++;
				dfs(j);
			}
		}

		cout << res << "\n";
	}

	return 0;
}
