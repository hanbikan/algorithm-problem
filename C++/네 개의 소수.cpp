#include <bits/stdc++.h>
using namespace std;

int N;
bool isPrime[1000001];
vector<int> primes;

bool isPrimeNumber(int n) {
	int i;
	for (i = 2; i < int(sqrt(n)) + 1; i++) {
		if (n % i == 0) return false;
	}

	return true;
}

void setPrimes() {
	int i, j;

	for (i = 2; i < N + 1; i++) isPrime[i] = true;

	for (i = 2; i < N + 1; i++) {
		if (isPrime[i]) {
			if (isPrimeNumber(i)) {
				primes.push_back(i);

				j = i * 2;
				while (j <= N) {
					isPrime[j] = false;
					j += i;
				}
			}
		}
	}
}

void solution() {
	int i;
	if (N < 8) {
		cout << "-1";
		return;
	}

	// 골드바흐의 추측
	vector<int> res;
	if (N % 2 == 1) {
		res.push_back(2);
		res.push_back(3);
		N -= 5; // 2, 3
	}
	else {
		res.push_back(2);
		res.push_back(2);
		N -= 4; // 2, 2
	}

	for (i = 0; i < primes.size(); i++) {
		if (isPrime[N - primes[i]]) {
			res.push_back(primes[i]);
			res.push_back(N - primes[i]);
			break;
		}
	}

	// 출력
	for (i = 0; i < res.size(); i++) {
		cout << res.at(i) << " ";
	}
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	cin >> N;

	setPrimes();
	solution();

	return 0;
}
