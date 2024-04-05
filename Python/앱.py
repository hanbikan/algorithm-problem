from bisect import bisect_left
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

max_cost = 0
app = []
for m, c in zip(input().split(), input().split()):
    m, c = int(m), int(c)
    max_cost += c
    if c == 0:
        M -= m
        N -= 1
    else:
        app.append([m, c])

dp = [[0] * (max_cost + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    m, c = app[i - 1]
    for j in range(1, max_cost + 1):
        if j >= c:
            dp[i][j] = max(
                dp[i - 1][j],
                dp[i - 1][j - c] + m
            )
        else:
            dp[i][j] = dp[i - 1][j]

index = bisect_left(dp[-1], M)
if dp[-1][index] >= M:
    print(index)
else:
    print(index + 1)