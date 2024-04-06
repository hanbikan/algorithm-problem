from collections import deque
import sys
input = sys.stdin.readline

def in_range(x, y):
    return 1 <= x <= N and 1 <= y <= N

def play():
    mapp = [[EMPTY] * (N + 1) for _ in range(N + 1)]
    mapp[1][1] = BODY
    for apple_x, apple_y in apple_positions:
        mapp[apple_x][apple_y] = APPLE

    positions = deque([[1,1]])
    dir = RIGHT
    time = 1
    while True:
        head_x, head_y = positions[-1]

        # move
        next_x, next_y = head_x + dx[dir], head_y + dy[dir]
        if not in_range(next_x, next_y) or mapp[next_x][next_y] == BODY:
            return time
        
        if mapp[next_x][next_y] == APPLE:
            positions.append([next_x, next_y])
            mapp[next_x][next_y] = BODY
        else: # EMPTY
            positions.append([next_x, next_y])
            mapp[next_x][next_y] = BODY
            x_to_remove, y_to_remove = positions.popleft()
            mapp[x_to_remove][y_to_remove] = EMPTY
        
        # set dir
        if actions.get(time):
            if actions[time] == 'D':
                dir = (dir + 1) % 4
            else:
                dir = (dir + 3) % 4
        
        time += 1

EMPTY, APPLE, BODY = 0, 1, 2

RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
K = int(input())
apple_positions = [list(map(int,input().split())) for _ in range(K)]
L = int(input())
actions = {}
for _ in range(L):
    X, C = input().split()
    X = int(X)
    actions[X] = C

print(play())