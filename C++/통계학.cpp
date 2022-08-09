#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int N;
	cin >> N;

	int counts[8001] = {0,};
	vector<int> nums;
	int a = 0;
	int maxCount = 0;
	for (int i = 0; i < N; i++) {
		int tmp;
		cin >> tmp;
		nums.push_back(tmp);

		a += tmp;
		counts[tmp+4000]++;
		if (maxCount < counts[tmp + 4000]) maxCount = counts[tmp + 4000];
	}

	cout << round((double)a / (double)N) << "\n";

	sort(nums.begin(), nums.end());
	cout << nums[N/2] << "\n";

	int c;
	int cnt = 0;
	for (int i = 0; i < 8001; i++) {
		if (counts[i] == maxCount) {
			c = i-4000;
			cnt++;
			if (cnt == 2) break;
		}
	}
	cout << c << "\n";

	cout << nums[N - 1] - nums[0] << "\n";
}
