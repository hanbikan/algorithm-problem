import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
MOD = 1_000_000_007

N, M = map(int, input().split())

dp = [1] * (N + 1)
for i in range(1, N + 1):
    dp[i] = dp[i - 1] if i < M else (dp[i - 1] + dp[i - M]) % MOD
print(dp[-1])