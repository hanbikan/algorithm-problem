import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dx = [1, 0]
dy = [0, 1]

def f(x, y):
    maxx = 0
    for k in range(2):
        nx,ny = x + dx[k], y + dy[k]
        if 0<=nx<=N-1 and 0<=ny<=M-1:
            if(dp[nx][ny] == -1): f(nx,ny)
            maxx = max(maxx, dp[nx][ny])

    dp[x][y] = mapp[x][y] + maxx

if __name__ == '__main__':
    N, M = map(int,input().split())
    mapp = [list(map(int,input().split())) for _ in range(N)]
    
    dp = [[-1]*M for _ in range(N)]
    f(0, 0)
    print(dp[0][0])