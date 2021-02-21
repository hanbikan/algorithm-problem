N = int(input())
INPUT = [0]*301
dp = [0]*301
for i in range(N):
    INPUT[i] = int(input())
dp[0] = INPUT[0]
dp[1] = INPUT[0]+INPUT[1]
dp[2] = max(INPUT[0]+INPUT[2], INPUT[1]+INPUT[2])
for i in range(3, N):
    dp[i] = max(dp[i-3]+INPUT[i-1]+INPUT[i], dp[i-2]+INPUT[i])
print(dp[N-1])