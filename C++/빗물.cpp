#include <bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(0); cout.tie(0); cin.tie(0);

	int H, W;
	cin >> H >> W;
	int i;

	int res = 0;
	int curInput, prevInput;
	cin >> prevInput;

	int left = prevInput;
	stack<int> stack;
	stack.push(prevInput);
	for (i = 1; i < W; i++) {
		cin >> curInput;
		if (prevInput < curInput) {
			int popped = 0;
			int h = min(left, curInput);
			while (stack.size() > 1) {
				int cur = stack.top();
				if (cur > h) break;

				stack.pop();
				popped++;
				res += h - cur;
			}

			if (left > curInput) {
				int j;
				// 5 1 4 -> 5 4 4
				for (j = 0; j < popped; j++) {
					stack.push(h);
				}
			}
			else {
				stack.pop(); // left에 해당하는 것까지 모두 지운다.
				left = curInput;
			}
		}
		stack.push(curInput);

		prevInput = curInput;
	}

	cout << res;

	return 0;
}