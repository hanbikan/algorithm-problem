#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int i;

	int N;
	cin >> N;

	int* nums = (int*)malloc(sizeof(int) * N);
	for (i = 0; i < N; i++) cin >> nums[i];

	sort(nums, nums + N);

	int M;
	cin >> M;
	for (i = 0; i < M; i++) {
		int tmp;
		cin >> tmp;
		cout << upper_bound(nums, nums + N, tmp) - lower_bound(nums, nums + N, tmp) << " ";
	}

	free(nums);

	return 0;
}
