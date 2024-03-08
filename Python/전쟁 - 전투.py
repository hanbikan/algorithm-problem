import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def get_size(x, y, color):
    result = 1
    is_visited[x][y] = True

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]

        if 0 <= nx <= N - 1 and 0 <= ny <= M - 1 and not is_visited[nx][ny] and mapp[nx][ny] == color:
            result += get_size(nx, ny, color)
    
    return result

M, N = map(int,input().split())
mapp = [str(input().rstrip()) for _ in range(N)]

is_visited = [[False] * M for _ in range(N)]
w, b = 0, 0
for i in range(N):
    for j in range(M):
        if not is_visited[i][j]:
            size = get_size(i, j, mapp[i][j])
            if mapp[i][j] == 'B':
                b += size * size
            else:
                w += size * size

print(w, b)