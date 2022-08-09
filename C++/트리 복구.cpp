#include <bits/stdc++.h>
using namespace std;

string preorder, inorder;
int preorderIndex;

void f(int start, int end) {
	if (start > end) return;

	int mid = inorder.find(preorder[preorderIndex++]);

	// postorder
	f(start, mid - 1);
	f(mid + 1, end);
	cout << inorder[mid];
}
int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	while (true) {
		preorder.clear();
		inorder.clear();
		cin >> preorder >> inorder;
		int len = preorder.length();

		// 탈출 조건
		if (len == 0) break;

		preorderIndex = 0;
		f(0, len -1);
		cout << "\n";
	}

	return 0;
}