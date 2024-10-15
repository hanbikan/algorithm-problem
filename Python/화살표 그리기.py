import sys
input = sys.stdin.readline

N = int(input())
cps = []
for _ in range(N):
    p, c = map(int, input().split())
    cps.append((c, p))
cps.sort()

result = 0
for i in range(N):
    c, p = cps[i]

    to_add = float('inf')
    if i - 1 >= 0 and cps[i - 1][0] == c:
        to_add = min(to_add, abs(cps[i - 1][1] - cps[i][1]))
    if i + 1 <= N-1 and cps[i + 1][0] == c:
        to_add = min(to_add, abs(cps[i + 1][1] - cps[i][1]))
    if to_add != float('inf'):
        result += to_add
print(result)