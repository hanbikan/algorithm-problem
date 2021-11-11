#include <iostream>
#define REP(i,a,b) for(int i=(a);i<(b);i++)
using namespace std;

int nums1[100][100];
int nums2[100][100];
int nums3[100][100];

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int N, M;
	cin >> N >> M;
	REP(i, 0, N) {
		REP(j, 0, M) cin >> nums1[i][j];
	}

	int K;
	cin >> M >> K;
	REP(i, 0, M) {
		REP(j, 0, K) cin >> nums2[i][j];
	}

	// Solution
	REP(i, 0, N) {
		REP(j, 0, K) {
			int res = 0;
			REP(k, 0, M) res += nums1[i][k] * nums2[k][j];

			nums3[i][j] = res;
		}
	}

	// Print
	REP(i, 0, N) {
		REP(j, 0, K) cout << nums3[i][j] << " ";
		cout << "\n";
	}
}
