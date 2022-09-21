from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
info = [[0]*(M+1)] + [list(map(int,input().split())) for _ in range(N)]

dp = [[[0, 0] for _ in range(N+1)] for _ in range(M+1)]
for i in range(1, M+1):
    for j in range(1, N+1):
        for cost in range(0, j+1):
            benefit = info[cost][i]
            if dp[i][j][0] < dp[i-1][j-cost][0] + benefit:
                dp[i][j] = [dp[i-1][j-cost][0] + benefit, cost]

print(dp[-1][-1][0])
j = N
to_print = deque()
for i in range(M, 0, -1):
    used = dp[i][j][1]
    to_print.appendleft(used)
    j -= used
print(*to_print)