import sys
input = sys.stdin.readline

EAST, WEST, NORTH, SOUTH = 1, 2, 3, 4

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

pos_by_dir = [
    [],
    [
        [1,1], [1,2], [3,1], [1,0]
    ],
    [
        [1,1], [1,0], [3,1], [1,2]
    ],
    [
        [1,1], [0,1], [3,1], [2,1]
    ],
    [
        [1,1], [2,1], [3,1], [0,1]
    ]
]

def roll_dice(dir):
    cur_x, cur_y = 1, 1
    tmp = dice_map[1][1]
    for k in range(1, 4):
        next_x, next_y = pos_by_dir[dir][k]
        dice_map[cur_x][cur_y] = dice_map[next_x][next_y]
        cur_x, cur_y = next_x, next_y
    dice_map[cur_x][cur_y] = tmp

def print_dice():
    for i in range(len(dice_map)):
        for j in range(len(dice_map[i])):
            if dice_map[i][j] == -1:
                print(" ", end="")
            else:
                print(dice_map[i][j], end="")
        print()
    print()

dice_map = [
    [-1,0,-1],
    [0,0,0],
    [-1,0,-1],
    [-1,0,-1]
]

N, M, x, y, K = map(int,input().split())
mapp = [list(map(int,input().split())) for _ in range(N)]
dirs = list(map(int,input().split()))
for dir in dirs:
    next_x, next_y = x + dx[dir], y + dy[dir]
    if not (0 <= next_x <= N - 1 and 0 <= next_y <= M - 1):
        continue
    x, y = next_x, next_y
    roll_dice(dir)
    if mapp[x][y] == 0:
        mapp[x][y] = dice_map[1][1]
    else:
        dice_map[1][1] = mapp[x][y]
        mapp[x][y] = 0
    print(dice_map[3][1])