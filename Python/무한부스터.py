import sys
input = sys.stdin.readline

dx = [1, 0]
dy = [0, 1]

def f(x, y):
    if x == N-1 and y == M-1:
        return 0

    res = float('inf')
    for i in range(info[x][y], 0, -1):
        for j in range(2):
            nx, ny = x + dx[j]*i, y + dy[j]*i

            if not (0 <= nx <= N-1 and 0 <= ny <= M-1): continue
            if dp[nx][ny] == -1:
                f(nx, ny)

            res = min(res, dp[nx][ny] + 1)
    
    dp[x][y] = res


if __name__ == '__main__':
    N, M = map(int, input().split())
    info = [list(map(int,input().split())) for _ in range(N)]
    
    dp = [[-1]*M for _ in range(N)]
    dp[N-1][M-1] = 0
    f(0,0)
    print(dp[0][0])