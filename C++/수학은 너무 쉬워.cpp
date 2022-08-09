#include <bits/stdc++.h>
#define INF 1000001
using namespace std;

int N;
vector<int> input;
bool isPrime[INF];
vector<int> primes;
vector<vector<int>> counts;
vector<int> totalCount;

bool getIsPrime(int n) {
	if (n == 2) return true;

	int i;
	for (i = 2; i < sqrt(n) + 1; i++) {
		if (n % i == 0) return false;
	}
	return true;
}

void setPrimes(int n) {
	if (!isPrime[n]) return;
	else {
		if (getIsPrime(n)) {
			primes.push_back(n);

			int i;
			for (i = n * 2; i < INF; i += n) {
				isPrime[i] = false;
			}
		}
	}
}

void setCount(int index) {
	int cur = input.at(index);
	int div = 2;
	int i;
	for (i = 0; i < primes.size() && cur > 1; i++) {
		int p = primes.at(i);
		if (cur % p == 0) {
			counts[index][i]++;
			totalCount[i]++;

			cur /= p;
			i--;
		}
	}
}

void solution() {
	int i;
	for (i = 2; i < INF; i++) setPrimes(i);

	totalCount = vector<int>(primes.size());
	counts = vector<vector<int>>(N, vector<int>(primes.size()));

	for (i = 0; i < N; i++) {
		setCount(i);
	}

	int maxScore = 1;
	int diff = 0;
	for (i = 0; i < primes.size(); i++) {
		int p = primes.at(i);
		int aver = totalCount[i] / N;

		if (totalCount[i] > 0) {
			maxScore *= pow(p, aver);
		}

		for (int j = 0; j < N; j++) {
			if (counts[j][i] < aver) {
				diff += aver - counts[j][i];
			}
		}
	}
	cout << maxScore << " " << diff;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	cin >> N;

	int i;
	for (i = 2; i < INF; i++) {
		isPrime[i] = true;
	}

	for (i = 0; i < N; i++) {
		int n;
		cin >> n;

		input.push_back(n);
	}

	solution();

	return 0;
}