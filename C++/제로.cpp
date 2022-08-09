#include <iostream>
#include <stack>
using namespace std;

int main()
{
	int K;
	cin >> K;

	stack<int> s;
	for (int i = 0; i < K; i++) {
		int tmp;
		cin >> tmp;
		if (tmp == 0) s.pop();
		else s.push(tmp);
	}
	
	// Get sum of the stack
	int res = 0;
	while (!s.empty()) {
		res += s.top();
		s.pop();
	}
	cout << res;

	return 0;
}
