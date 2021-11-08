#include <iostream>
using namespace std;

bool is_all_same_papers(int** nums, int x1, int y1, int x2, int y2) {
	int val = nums[x1][y1];	// 비교 대상

	for (int i = x1; i < x2 + 1; i++) {
		for (int j = y1; j < y2 + 1; j++) {
			if (nums[i][j] != val) return false;
		}
	}

	return true;
}

pair<int, int> divide_and_conquer(int** nums, int x1, int y1, int x2, int y2) {
	pair<int, int> res = make_pair(0, 0);
	if (is_all_same_papers(nums, x1, y1, x2, y2)) {
		if (nums[x1][y1] == 0) return make_pair(1, 0);
		else return make_pair(0, 1);
	}

	int mid_x = (x1 + x2) / 2;
	int mid_y = (y1 + y2) / 2;

	pair<int, int> tmp;
	tmp = divide_and_conquer(nums, x1, y1, mid_x, mid_y); // left-top		
	res.first += tmp.first; res.second += tmp.second;
	tmp = divide_and_conquer(nums, mid_x + 1, y1, x2, mid_y); // right-top
	res.first += tmp.first; res.second += tmp.second;
	tmp = divide_and_conquer(nums, x1, mid_y+1, mid_x, y2); // left-bottom
	res.first += tmp.first; res.second += tmp.second;
	tmp = divide_and_conquer(nums, mid_x + 1, mid_y+1, x2, y2); // right-top
	res.first += tmp.first; res.second += tmp.second;

	return res;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	// Input
	int N;
	cin >> N;
	int i, j;
	int** nums = (int **)malloc(sizeof(int*) * N);
	for (i = 0; i < N; i++) {
		nums[i] = (int*)malloc(sizeof(int)*N);
		for (j = 0; j < N; j++) cin >> nums[i][j];
	}

	// Solution
	pair<int, int> res = divide_and_conquer(nums, 0, 0, N - 1, N - 1);
	cout << res.first << "\n";
	cout << res.second << "\n";

	// Free
	for (i = 0; i < N; i++) {
		free(nums[i]);
	} free(nums);

	return 0;
}
