from copy import deepcopy
import sys
input = sys.stdin.readline

NUM, DIR = 0, 1
SHARK = 0

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def in_range(x, y):
    return 0 <= x < 4 and 0 <= y < 4

def move_fishes():
    for n in range(1, 16 + 1):
        x, y = pos_by_num[n]
        if x == None:
            continue
        dir = num_and_dir[x][y][DIR]
        for d_offset in range(len(dx)):
            nd = (dir + d_offset) % len(dx)
            nx = x + dx[nd]
            ny = y + dy[nd]
            if in_range(nx, ny) and num_and_dir[nx][ny][NUM] != SHARK:
                next_num = num_and_dir[nx][ny][NUM]
                # Move
                tmp = pos_by_num[n].copy()
                pos_by_num[n] = [nx, ny]
                if next_num != None: pos_by_num[next_num] = [tmp[0], tmp[1]]

                tmp = num_and_dir[nx][ny].copy()
                num_and_dir[nx][ny] = [n, nd]
                num_and_dir[x][y] = [tmp[0], tmp[1]]

                break

def print_all():
    print("pos_by_num")
    for i in range(16 + 1):
        print("{0}: {1}".format(i, pos_by_num[i]), end = " ")
    print()
    print("num_and_dir")
    for i in range(len(num_and_dir)):
        print(num_and_dir[i])
    print()
    print()

def dfs(ate):
    global num_and_dir, pos_by_num, max_ate
    _num_and_dir = deepcopy(num_and_dir)
    _pos_by_num = deepcopy(pos_by_num)

    max_ate = max(ate, max_ate)

    move_fishes()
    shark_x, shark_y = pos_by_num[SHARK]
    shark_dir = num_and_dir[shark_x][shark_y][DIR]
    for d in range(1, 3 + 1):
        nx = shark_x + dx[shark_dir] * d
        ny = shark_y + dy[shark_dir] * d
        if in_range(nx, ny) and num_and_dir[nx][ny][NUM] != None:
            _num_and_dir2 = deepcopy(num_and_dir)
            _pos_by_num2 = deepcopy(pos_by_num)

            # Eat
            killed = num_and_dir[nx][ny][NUM]
            pos_by_num[SHARK] = [pos_by_num[killed][0], pos_by_num[killed][1]]
            pos_by_num[killed] = [None, None]
            num_and_dir[nx][ny][NUM] = SHARK
            num_and_dir[shark_x][shark_y] = [None, None]

            dfs(ate + killed)

            num_and_dir = _num_and_dir2
            pos_by_num = _pos_by_num2
    num_and_dir = _num_and_dir
    pos_by_num = _pos_by_num

num_and_dir = []
pos_by_num = {}
for i in range(4):
    to_append = []
    line = list(map(int,input().split()))
    for j in range(0, len(line), 2):
        to_append.append([line[j], line[j + 1] - 1])
        pos_by_num[line[j]] = [i, j // 2]
    num_and_dir.append(to_append)

# Put a shark
killed = num_and_dir[0][0][NUM]
num_and_dir[0][0][NUM] = SHARK
pos_by_num[SHARK] = [0, 0]
pos_by_num[killed] = [None, None]

max_ate = killed
dfs(killed)
print(max_ate)