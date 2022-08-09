#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int parents[4000001];

int findParent(int x) {
	if (parents[x] == x) return parents[x];

	return findParent(parents[x]);
}

void unionParents(int x, int y) {
	int xParent = findParent(x);
	int yParent = findParent(y);

	if (xParent < yParent) parents[xParent] = yParent;
	else parents[yParent] = xParent;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int i, j;
	int N, M, K;
	cin >> N >> M >> K;

	// Set nums
	vector<int> nums;
	for (i = 0; i < M; i++) {
		int tmp;
		cin >> tmp;
		nums.push_back(tmp);
	}
	sort(nums.begin(), nums.end());

	// Init parents
	for (i = 0; i < M; i++) parents[i] = i;

	// Solution
	for (i = 0; i < K; i++) {
		int tmp;
		cin >> tmp;
										 
		int index = lower_bound(nums.begin(), nums.end(), tmp+1) - nums.begin();
		cout << nums[findParent(index)] << "\n";

		if (index <= M-1) unionParents(findParent(index), findParent(index) + 1);
	}
}