import sys
input = sys.stdin.readline
AB = ['A', 'B']

N = int(input())
strr = ' ' + str(input().rstrip())

dp = [[0 for _ in range(N + 1)] for _ in range(2)]
for i in range(1, N + 1):
    for j in range(2):
        if strr[i] == AB[j]:
            dp[j][i] = dp[j][i - 1]
        else:
            dp[j][i] = min(dp[j][i - 1] + 1, dp[(j + 1) % 2][i - 1] + 1)
print(dp[0][-1])