import sys
input = sys.stdin.readline

N = int(input())
bricks = [[0, 0, 0]] + [list(map(int,input().split())) + [i] for i in range(1, N + 1)]
bricks.sort()

# Solution
max_index = 0
max_height = 0
dp = [[0, []]] # height_sum, stacked_bricks
for i in range(1, N + 1):
    brick = bricks[i]
    dp.append([brick[1], [brick]])
    for j in range(1, i):
        if bricks[j][2] < brick[2]:
            if dp[i][0] < dp[j][0] + brick[1]:
                dp[i][0] = dp[j][0] + brick[1]
                dp[i][1] = dp[j][1].copy() + [brick]
    
    if dp[i][0] > max_height:
        max_index = i
        max_height = dp[i][0]

stack = dp[max_index][1]
print(len(stack))
for brick in stack:
    print(brick[-1])