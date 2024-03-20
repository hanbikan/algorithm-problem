import sys
input = sys.stdin.readline

def in_range(x, y):
    return (0 <= x <= 2 and 0 <= y <= 2) or (x == 3 and y == 0)

MOD = 1_234_567

dx = [1,-1,0,0]
dy = [0,0,1,-1]

dp = [
    [[1,1,1], [1,1,1], [1,1,1], [1]],
]

for _ in range(2, 1001):
    new_dp = [[0,0,0], [0,0,0], [0,0,0], [0]]
    for i in range(len(new_dp)):
        for j in range(len(new_dp[i])):
            for k in range(4):
                adj_i, adj_j = i + dx[k], j + dy[k]
                if in_range(adj_i, adj_j):
                    new_dp[i][j] = (new_dp[i][j] + dp[-1][adj_i][adj_j]) % MOD
    dp.append(new_dp)

T = int(input())
for _ in range(T):
    N = int(input())
    cur_dp = dp[N - 1]
    summ = 0
    for i in range(len(cur_dp)):
        for j in range(len(cur_dp[i])):
            summ = (summ + cur_dp[i][j]) % MOD
    print(summ)