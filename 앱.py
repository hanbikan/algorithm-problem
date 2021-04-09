import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memories = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

costSum = sum(costs)
dp = [[0]*(costSum+1) for _ in range(N+1)]
minCost = costSum

for i in range(1, N+1):
    curMemory = memories[i]
    curCost = costs[i]

    for j in range(1, costSum+1):
        if curCost > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-curCost] + curMemory)

        if dp[i][j] >= M:
            minCost = min(minCost, j)

print(minCost)
