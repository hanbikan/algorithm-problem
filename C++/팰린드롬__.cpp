#include <bits/stdc++.h>
using namespace std;

int nums[2000001];
int N;
int A[2000001];

void manacher() {
	int i;

	int r = 0, p = 0;
	for (i = 0; i < N; i++) {
		// Set initial value of A
		if (i <= r) A[i] = min(r - i, A[2*p - i]);
		else A[i] = 0;

		// Get the palindrome longer
		while ((i - A[i] - 1 >= 0 && i + A[i] + 1 <= N - 1) &&
			(nums[i - A[i] - 1] == nums[i + A[i] + 1])) A[i] += 1;

		// Update r, p
		if (r < i + A[i]) {
			r = i + A[i];
			p = i;
		}
	}
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int i;

	cin >> N;

	// Expand the input: "123" -> " 0102030" for manacher
	for (i = 0; i < N; i++) {
		nums[i * 2] = 0;
		cin >> nums[i * 2 + 1];
	}
	N = N * 2 + 1;
	nums[N - 1] = 0;

	manacher();

	int M;
	cin >> M;
	for (i = 0; i < M; i++) {
		int S, E;
		cin >> S >> E;
		S--; E--;

		// ((S + E)/2) * 2 + 1 = S + E + 1 ... original index to expanded index
		if (A[S + E + 1] >= E - S + 1) cout << "1\n";
		else cout << "0\n";
	}

	return 0;
}
