#include <iostream>
using namespace std;

// n!에서 p의 승수를 구한다
int get_power(int n, int p) {
	int res = 0;

	while (n >= p) {
		res += n / p;
		n /= p;
	}

	return res;
}

int get_power_from_combination(int n, int m, int p) {
	return get_power(n, p) - get_power(m, p) - get_power(n - m, p);
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int n, m;
	cin >> n >> m;

	cout << min(get_power_from_combination(n, m, 2), get_power_from_combination(n, m, 5));

	return 0;
}
