import sys
input = sys.stdin.readline

N = int(input())
R1 = list(map(int, input().split()))
R2 = list(map(int, input().split()))
N1 = [x for x in R1 if x != 0]
N2 = [x for x in R2 if x != 0]
L1 = len(N1)
L2 = len(N2)

dp = [[[-float('inf')]*(L2+1) for _ in range(L1+1)] for _ in range(N+1)] # dp[k][i][j]
for k in range(N+1):
    for i in range(min(L1,k)+1):
        for j in range(min(L2,k)+1):
            if i == 0 or j == 0:
                dp[k][i][j] = 0
                continue
            dp[k][i][j] = max(
                dp[k-1][i-1][j-1] + N1[i-1] * N2[j-1],
                dp[k-1][i-1][j],
                dp[k-1][i][j-1],
            )

print(dp[-1][-1][-1])