import sys
input = sys.stdin.readline

def calculate_y(y):
    return (y + N) % N

def can_cover_with_next_y(x, y):
    return enemies[x][y] + enemies[x][calculate_y(y + 1)] <= W

T = int(input())
for _ in range(T):
    N, W = map(int,input().split())
    enemies = [list(map(int,input().split())) for _ in range(2)]

    result = float('inf')
    for k in range(4):
        c0 = True
        c1, c2 = can_cover_with_next_y(0, -1), can_cover_with_next_y(1, -1)
        c3 = c1 and c2

        if k == 0 and c0:
            dp = [[float('inf')] * 4 for _ in range(N + 1)]
            dp[0][0] = 0
        elif k == 1 and c1:
            dp = [[float('inf')] * 4 for _ in range(N + 1)]
            dp[0][1] = 0
        elif k == 2 and c2:
            dp = [[float('inf')] * 4 for _ in range(N + 1)]
            dp[0][2] = 0
        elif k == 3 and c3:
            dp = [[float('inf')] * 4 for _ in range(N + 1)]
            dp[0][3] = 0
        else:
            continue

        for i in range(1, N + 1):
            c0 = True
            c0_vertical = enemies[0][i - 1] + enemies[1][i - 1] <= W
            c1, c2 = can_cover_with_next_y(0, i - 1), can_cover_with_next_y(1, i - 1)
            c3 = c1 and c2

            dp[i][0] = min(
                dp[i - 1][0] + 2,
                dp[i - 1][1] + 1,
                dp[i - 1][2] + 1,
                dp[i - 1][3]
            )
            if c0_vertical:
                dp[i][0] = min(dp[i][0], dp[i - 1][0] + 1)
            if c1:
                dp[i][1] = min(dp[i - 1][0] + 2, dp[i - 1][2] + 1)
            if c2:
                dp[i][2] = min(dp[i - 1][0] + 2, dp[i - 1][1] + 1)
            if c3:
                dp[i][3] = dp[i - 1][0] + 2
        result = min(result, dp[-1][k])

    print(result)

'''
1
8 100
70 60 55 43 57 60 44 50
58 40 47 90 45 52 80 40

1
4 100
50 100 100 50
100 100 100 100
'''