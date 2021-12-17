#include <iostream>
#include <queue>
#include <vector>
#include <tuple>
#define INF 1000001
using namespace std;

int N;
int costs[1000][3];
int dp[1000][3][3]; // index, color, first

int getDp(int index, int color, int first) {
	// dp에 값이 아직 설정되지 않았을 경우
	if (dp[index][color][first] == 0) {
		if (index == N - 1) {
			if (first == color) dp[index][color][first] = INF;
			else dp[index][color][first] = costs[index][color];
		}
		else {
			dp[index][color][first] = min(
				getDp(index + 1, (color + 1) % 3, first),
				getDp(index + 1, (color + 2) % 3, first)
			) + costs[index][color];
		}
	}

	return dp[index][color][first];
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	cin >> N;
	
	// Set costs
	int i;
	for (i = 0; i < N; i++)
		cin >> costs[i][0] >> costs[i][1] >> costs[i][2];
	
	// Set minCost using DP
	int minCost = INF;
	for (i = 0; i < 3; i++)
		minCost = min(minCost, getDp(0, i, i));
	cout << minCost;

	return 0;
}
