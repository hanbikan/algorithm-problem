import sys
input = sys.stdin.readline

TOP, RIGHT, BOTTOM, LEFT = 0, 1, 2, 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 0 -> 1
# 1 -> 0
# 2 -> 3
# 3 -> 2
def convert_dir(dir):
    if 0 <= dir <= 1:
        return (dir + 1) % 2
    else:
        return (dir + 1) % 2 + 2

def f(x, y, dir):
    cur_x, cur_y, cur_dir = x, y, dir
    while True:
        if mapp[cur_x][cur_y] == 1:
            cur_dir = convert_dir(cur_dir)
        nx, ny = cur_x + dx[cur_dir], cur_y + dy[cur_dir]

        if not (0 <= nx <= N-1 and 0 <= ny <= M-1):
            # top left
            if cur_x == cur_y == 0:
                if cur_dir == LEFT: return 1
                else: return N * 2 + M * 2
            # bottom left
            elif cur_x == N-1 and cur_y == 0:
                if cur_dir == LEFT: return N
                else: return N + 1
            # bottom right
            elif cur_x == N-1 and cur_y == M-1:
                if cur_dir == BOTTOM: return N + M
                else: return N + M + 1
            # top right
            elif cur_x == 0 and cur_y == M-1:
                if cur_dir == RIGHT: return N * 2 + M
                else: return N * 2 + M + 1
            else:
                # left
                if cur_y == 0: return cur_x + 1
                # bottom
                elif cur_x == N-1: return N + cur_y + 1
                # right
                elif cur_y == M-1: return N + M + (N - cur_x)
                # top
                else: return N * 2 + M + (M - cur_y)

        cur_x, cur_y = nx, ny

N, M = map(int,input().split())
mapp = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    print(f(i, 0, RIGHT), end=" ")

for j in range(M):
    print(f(N-1, j, TOP), end=" ")

for i in range(N-1, -1, -1):
    print(f(i, M-1, LEFT), end=" ")

for j in range(M-1, -1, -1):
    print(f(0, j, BOTTOM), end=" ")