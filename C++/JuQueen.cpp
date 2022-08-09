#include <bits/stdc++.h>
using namespace std;

int C, N, O;
pair<int, int> tree[4587520*4 + 1]; // min, max
int lazy[4587520*4 + 1];

void propagateTree(int index, int start, int end) {
	if (lazy[index] != 0) {
		tree[index].first += lazy[index];
		tree[index].second += lazy[index];

		if (start != end) {
			lazy[index * 2] += lazy[index];
			lazy[index * 2 + 1] += lazy[index];
		}

		lazy[index] = 0;
	}
}

void initializeTree(int index, int start, int end) {
	if (start == end) return;
	else {
		int mid = (start + end) / 2;
		initializeTree(index * 2, start, mid);
		initializeTree(index * 2 + 1, mid + 1, end);
	}
	tree[index] = { 0, 0 };

	return;
}

void updateTree(int toAdd, int left, int right, int index, int start, int end) {
	propagateTree(index, start, end);

	if (end < left || right < start) return;

	if (left <= start && end <= right) {
		lazy[index] += toAdd;
		propagateTree(index, start, end);

		return;
	}

	int mid = (start + end) / 2;
	updateTree(toAdd, left, right, index * 2, start, mid);
	updateTree(toAdd, left, right, index * 2 + 1, mid+1, end);

	tree[index].first = min(tree[index * 2].first, tree[index * 2 + 1].first);
	tree[index].second = max(tree[index * 2].second, tree[index * 2 + 1].second);
}

pair<int, int> queryTree(int left, int right, int index, int start, int end) {
	propagateTree(index, start, end);

	if (end < left || right < start) return {10001, -10001};

	if (left <= start && end <= right) return tree[index];

	int mid = (start + end) / 2;
	pair<int, int> leftRes = queryTree(left, right, index * 2, start, mid);
	pair<int, int> rightRes = queryTree(left, right, index * 2 + 1, mid + 1, end);
	
	return { min(leftRes.first, rightRes.first), max(leftRes.second, rightRes.second) };
}

int getToAdd(pair<int, int> minMax, int toAdd) {
	int res = toAdd;
	if (minMax.first + toAdd < 0) res = -minMax.first;
	else if (minMax.second + toAdd > N) res = N - minMax.second;

	return res;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int i;

	cin >> C >> N >> O;

	initializeTree(1, 1, C);

	string operation;
	int X, A, B, S;
	for (i = 0; i < O; i++) {
		cin >> operation;
		if (operation.compare("change") == 0) {
			cin >> X >> S;
			X++;

			int toAdd = getToAdd(queryTree(X, X, 1, 1, C), S);
			updateTree(toAdd, X, X, 1, 1, C);
			cout << toAdd << "\n";
		}
		else if (operation.compare("groupchange") == 0) {
			cin >> A >> B >> S;
			A++; B++;

			int toAdd = getToAdd(queryTree(A, B, 1, 1, C), S);
			updateTree(toAdd, A, B, 1, 1, C);
			cout << toAdd << "\n";
		}
		else if (operation.compare("state") == 0) {
			cin >> X;
			X++;

			cout << queryTree(X, X, 1, 1, C).first << "\n";
		}
	}

	return 0;
}
