import sys
input = sys.stdin.readline

N = int(input())
t_and_p = [list(map(int,input().split())) for _ in range(N)]

dp = [[0, 0] for _ in range(N + 1)]
for d in range(N - 1, -1, -1):
    next_day = d + t_and_p[d][0]
    if next_day <= N:
        dp[d][0] = t_and_p[d][1] + max(dp[next_day])

    dp[d][1] = max(dp[d + 1]) if d + 1 <= N else 0

print(max(dp[0]))