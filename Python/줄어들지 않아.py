import sys
input = sys.stdin.readline

W = 10
H = 64 + 1

dp = [[0] * W for _ in range(H)]
dp[1] = [1] * W
for i in range(2, H):
    for j in range(10):
        dp[i][j] = sum(dp[i - 1][j:])

for _ in range(int(input())):
    n = int(input())
    print(sum(dp[n]))