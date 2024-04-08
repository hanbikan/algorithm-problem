import sys
input = sys.stdin.readline

d = [[1,0],[0,1],[-1,0],[0,-1]]
VISITED = 0

result = 0

def dfs(x, y, count, sum):
    global result

    if count == 0:
        result = max(result, sum)
        return

    for dx, dy in d:
        next_x, next_y = x + dx, y + dy
        if not (0 <= next_x <= N - 1 and 0 <= next_y <= M - 1) or mapp[next_x][next_y] == VISITED:
            continue

        tmp = mapp[next_x][next_y]

        mapp[next_x][next_y] = VISITED
        dfs(next_x, next_y, count - 1, sum + tmp)
        mapp[next_x][next_y] = tmp

        # For ㅗ, ㅏ, ㅜ, ㅓ: 수선의 발에서 시작하는 dfs
        if count == 2:
            mapp[next_x][next_y] = VISITED
            dfs(x, y, count - 1, sum + tmp)
            mapp[next_x][next_y] = tmp

N, M = map(int,input().split())
mapp = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        tmp = mapp[i][j]
        mapp[i][j] = 0
        dfs(i, j, 3, tmp)
        mapp[i][j] = tmp

print(result)