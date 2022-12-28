import sys
input = sys.stdin.readline

def print_dp():
    for i in range(N+1): print(dp[i])

def set_dp_moving_to_top_right(x, y):
    while 1 <= x <= N and 1 <= y <= N:
        if nums[x] == nums[y]:
            dp[x][y] = True
            x -= 1
            y += 1
        else:
            break

N = int(input())
nums = [0] + list(map(int,input().split()))

dp = [[False]*(N+1) for _ in range(N+1)]

# Set diagonals True
start_positions = []
for i in range(1, N):
    dp[i][i] = True
    start_positions.append([i,i])
    if nums[i] == nums[i+1]:
        dp[i][i+1] = True
        start_positions.append([i,i+1])
dp[N][N] = True
start_positions.append([N,N])

# Set dp
for start_x, start_y in start_positions:
    set_dp_moving_to_top_right(start_x-1, start_y+1)

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    if dp[S][E]: print(1)
    else: print(0)