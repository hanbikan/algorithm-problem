from bisect import bisect_right
import sys
input = sys.stdin.readline

def f(n):
    if n == 0:
        return "m"

    index = bisect_right(table1, n) - 1
    if index == -1:
        return "o"
    else:
        if table1[index] == n:
            return "m"
        else:
            if table1[index] + 1 <= n <= table1[index] + table2[index] - 1:
                return "o"
            else:
                return f(n - table1[index] - table2[index])

N = int(input())
table1 = [3]
table2 = [4]
while True:
    to_append = table1[-1] * 2 + table2[-1]
    if to_append > 1_000_000_000:
        break
    table1.append(to_append)
    table2.append(table2[-1] + 1)

print(f(N - 1))