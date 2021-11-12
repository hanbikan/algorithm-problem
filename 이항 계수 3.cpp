#include <iostream>
#define REP(i, a, b) for(int i=(a);i<(b);i++)
#define MOD 1000000007
using namespace std;

long long getFactorial(long long n) {
	long long res = 1;
	REP(i, 2, n + 1) res = i * res % MOD;

	return res;
}

// Get t^n
long long getPower(long long t, long long n) {
	if (n == 1) return t;

	if (n % 2 == 0) {
		long long res = getPower(t, n / 2) % MOD;
		return res * res % MOD;
	}
	else
		return getPower(t, n-1) * t % MOD;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	long long N, K;
	cin >> N >> K;

	// Get (K!(N-K)!)^1000000005
	long long t = getFactorial(K) * getFactorial(N - K) % MOD;
	long long res = getPower(t, MOD - 2);

	// res * N!
	cout << res * getFactorial(N) % MOD;
}