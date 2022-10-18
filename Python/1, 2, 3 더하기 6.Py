import sys
input = sys.stdin.readline
MOD = 1000000009

dp = [0,1,2,2,3,3,6,6,11,11]
for i in range(10, 100001):
    dp.append((dp[i-2]*2 - dp[i-8]) % MOD)

for _ in range(int(input())):
    n = int(input())
    print(dp[n])