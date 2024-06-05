import sys
input = sys.stdin.readline

N = int(input())

dp = [[0] * 8 for _ in range(N + 1)]
dp[0][7] = 1

for i in range(1, N + 1):
    dp[i][0] = dp[i - 1][7]
    dp[i][1] = dp[i - 1][6]
    dp[i][4] = dp[i - 1][3]
    dp[i][3] = dp[i - 1][4] + dp[i - 1][7]
    dp[i][6] = dp[i - 1][1] + dp[i - 1][7]
    dp[i][7] = dp[i - 1][0] + dp[i - 1][3] + dp[i - 1][6]

print(dp[-1][-1])