import sys
input = sys.stdin.readline

def paste(src, dest, dest_x, dest_y, repeat = 1):
    for i in range(1, 21):
        if dest_x + i > 20:
            break
        for j in range(1, 21):
            if dest_y + j > 20:
                break
            dest[dest_x + i][dest_y + j] += src[i][j] * repeat

dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

dp[1][1][1] = 1

for i in range(2, 21):
    center_count = i - 2
    paste(dp[i - 1], dp[i], 0, 0, center_count)
    paste(dp[i - 1], dp[i], 1, 0)
    paste(dp[i - 1], dp[i], 0, 1)

T = int(input())
for _ in range(T):
    N, L, R = map(int, input().split())
    print(dp[N][L][R])