import sys, heapq
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < H and 0 <= y < W

def bfs():
    if W == 1 and H == 1:
        if mapp[0][0] == EMPTY:
            return 0
        else:
            return -1

    # dp[k][x][y]
    dp = [[[float('inf') for _ in range(W)] for _ in range(H)] for _ in range(K + 1)]
    q = [(0, 0, 0, 0)]  # moved, x, y, used_k
    dp[0][0][0] = 0

    while q:
        moved, x, y, used_k = heapq.heappop(q)

        d_len = d_len_extended if used_k < K else d_len_monkey
        for k in range(d_len):
            next_moved = moved + 1
            dx, dy = d_pos[k]
            nx, ny = x + dx, y + dy
            next_used_k = used_k
            if k >= d_len_monkey:
                next_used_k += 1

            if not in_range(nx, ny):
                continue
            if mapp[nx][ny] != EMPTY:
                continue

            if nx == H - 1 and ny == W - 1:
                return next_moved

            if next_moved < dp[next_used_k][nx][ny]:
                dp[next_used_k][nx][ny] = next_moved
                heapq.heappush(q, (next_moved, nx, ny, next_used_k))

    return -1

EMPTY, WALL = 0, 1

d_pos = [
    # Monkey
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
    # Horse
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
]
d_len_monkey = 4
d_len_extended = len(d_pos)

K = int(input())
W, H = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(H)]

print(bfs())