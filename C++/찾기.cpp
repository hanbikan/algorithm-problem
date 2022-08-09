#include <iostream>
#include <vector>
#include <string>
#define INF 1000000
using namespace std;

int pi[INF + 1];

void setPi(string keyword) {
	int keywordLength = keyword.size();

	int j = 0;
	for (int i = 1; i < keywordLength; i++) {
		while (keyword[i] != keyword[j] && j > 0) {
			j = pi[j - 1];
		}

		if (keyword[i] == keyword[j]) {
			j++;
			pi[i] = j;
		}
	}
}

vector<int> doKMP(string str, string keyword) {
	vector<int> indices;

	setPi(keyword);

	int stringLength = str.size();
	int keywordLength = keyword.size();

	int i = 0;
	int j = 0;
	while (i < stringLength) {
		if (str[i] == keyword[j]) {
			i++;
			j++;
		}
		else {
			if (j > 0) j = pi[j - 1];
			else i++;
		}

		if (j == keywordLength) {
			j = pi[j - 1];
			indices.push_back(i - keywordLength + 1);
		}
	}

	return indices;
}

int main()
{
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	string T, P;
	getline(cin, T);
	getline(cin, P);

	vector<int> indices = doKMP(T, P);

	cout << indices.size() << "\n";
	for (int i = 0; i < indices.size(); i++) cout << indices[i] << " ";
}
