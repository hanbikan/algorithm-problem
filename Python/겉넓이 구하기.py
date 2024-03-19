import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int,input().split())
heights = [list(map(int,input().split())) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        cur = 2
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
                cur += max(0, heights[i][j] - heights[nx][ny])
            else:
                cur += heights[i][j]
        result += cur

print(result)