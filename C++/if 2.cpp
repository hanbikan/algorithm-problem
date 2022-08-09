#include <iostream>
using namespace std;
int main() {
    int a = 98765431;
    float b = 98765432;
    int c = 98765432;

    if (a == b && b == c && c != a) {
        cout << "true" << '\n';
    }
    else {
        cout << "false" << '\n';
    }
    return 0;
}