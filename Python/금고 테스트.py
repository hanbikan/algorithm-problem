import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j == 1: dp[i][j] = i
        elif j > i or j >= 9: dp[i][j] = dp[i][j - 1]
        else:
            dp[i][j] = float('inf')
            for a in range(i // 2 + 1):
                b = i - a - 1
                dp[i][j] = min(dp[i][j], max(dp[a][j - 1], dp[b][j]) + 1)

print(dp[-1][-1])