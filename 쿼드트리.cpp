#include <iostream>
#define REP(i, a, b) for(int i=(a);i<(b);i++)
using namespace std;

int nums[64][64];

int getSameNumber(int x1, int y1, int x2, int y2) {
	int res = nums[x1][y1];

	REP(i, x1, x2 + 1) {
		REP(j, y1, y2 + 1) {
			if (res != nums[i][j]) return -1;
		}
	}

	return res;
}

void printQuardTree(int x1, int y1, int x2, int y2) {
	int res = getSameNumber(x1, y1, x2, y2);
	if (res != -1) {
		cout << res;
		return;
	}

	cout << "(";
	int midX = (x1 + x2) / 2;
	int midY = (y1 + y2) / 2;
	printQuardTree(x1, y1, midX, midY);
	printQuardTree(x1, midY+1, midX, y2);
	printQuardTree(midX + 1, y1, x2, midY);
	printQuardTree(midX + 1, midY + 1, x2, y2);
	cout << ")";
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	int N;
	cin >> N;

	char forInput[1];
	REP(i, 0, N) {
		cin.getline(forInput, 1);
		REP(j, 0, N) {
			char tmp;
			cin >> tmp;
			nums[i][j] = tmp - '0';
		}
	}

	printQuardTree(0, 0, N - 1, N - 1);
}
