#include <iostream>
#include <algorithm>
#define INF 2000000001
using namespace std;

int	nums[100000];

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) cin >> nums[i];

	// Solution
	sort(nums, nums + N);

	int res_abs = INF;
	int res_l = 0;
	int res_r = 0;

	int l = 0;
	int r = N - 1;
	while (l < r) {
		if (abs(nums[l] + nums[r]) < res_abs) {
			res_abs = abs(nums[l] + nums[r]);
			res_l = nums[l];
			res_r = nums[r];
		}

		if (nums[l] + nums[r] > 0) r--;
		else l++;
	}

	cout << res_l << " " << res_r;

	return 0;
}
