import sys

input = sys.stdin.readline

N, M = map(int, input().split())
D = [0] + [int(input()) for _ in range(N)]

# dp[0][i][j]: 시간이 i이고 지침 지수가 j일 때 도달 가능한 최대 거리
# dp[0]: 휴식 X, dp[1]: 휴식 중
'''
dp[0]
0 0 0
0 5 0
0 3 8
0 9 7
0 7 11
0 19 17

dp[1]
0 0 0
0 0 0
5 0 0
5 8 0
9 7 0
9 11 0
'''
dp = [[[0] * (M + 1) for _ in range(N + 1)] for _ in range(2)]
for i in range(1, N + 1):
    for j in range(min(M, i) + 1):
        if j == 0: # 지침 지수가 0인 채로 휴식
            dp[1][i][j] = dp[1][i - 1][j]
        if j == 1: # 휴식하다가 달리기 시작
            dp[0][i][j] = dp[1][i - 1][0] + D [i]
        if j - 1 >= 0: # 달림
            dp[0][i][j] = max(dp[0][i][j], dp[0][i - 1][j - 1] + D[i])
        if j + 1 < M + 1: # 휴식
            dp[1][i][j] = max(dp[1][i][j], dp[0][i - 1][j + 1], dp[1][i - 1][j + 1])

print(dp[1][-1][0])