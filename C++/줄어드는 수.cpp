#include <bits/stdc++.h>
using namespace std;

int N;
string f(string num) {
	int i;
	for (i = 0; i < N-1; i++) {
		int j, k;
		for (j = num.length() - 1; j > 0; j--) {
			if (num[j - 1] > num[j] + 1) {
				for (k = 0; k < num.length() - j - 1; k++) {
					num[num.length() - 1 - k] = '0' + k;
				}
				num[j] += 1;
				break;
			}
		}

		// 첫째자리 증가 또는 문자열 길이 증가
		if (j == 0) {
			if (num[0] == '9') {
				if (num.length() == 10) return "-1";

				for (k = 0; k < num.length(); k++) {
					num[num.length() - 1 - k] = '0' + k;
				}
				num = to_string(num.length()) + num;
			}
			else {
				for (k = 0; k < num.length() - 1; k++) {
					num[num.length() - 1 - k] = '0' + k;
				}
				num[0] += 1;
			}
		}
	}

	return num;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	cin >> N;
	cout << f("0");

	return 0;
}