from queue import PriorityQueue
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

ROW, COLUMN = 0, 1

EMPTY, TREE = 0, 1
B_ROW, B_COLUMN = 2, -2
E_ROW, E_COLUMN = 3, -3

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
x_range = [[[1,1,1], [-1,-1,-1], [0,0,0], [0,0,0]], [[0,1,2], [-2,-1,0], [-1,0,1], [-1,0,1]]]
y_range = [[[-1,0,1], [-1,0,1], [0,1,2], [-2,-1,0]], [[0,0,0], [0,0,0], [1,1,1], [-1,-1,-1]]]
x_range_rotation = [-1,-1,-1,0,1,1,1,0]
y_range_rotation = [-1,0,1,1,1,0,-1,-1]

def check_range(x, y, k, rotation):
    for i in range(3):
        dx, dy = x_range[rotation][k][i], y_range[rotation][k][i]
        if not (0 <= x+dx <= N-1 and 0 <= y+dy <= N-1) or mapp[x+dx][y+dy] == 1:
            return False
    return True

def check_rotation_range(x, y):
    for k in range(len(x_range_rotation)):
        dx, dy = x_range_rotation[k], y_range_rotation[k]
        if not (0 <= x+dx <= N-1 and 0 <= y+dy <= N-1) or mapp[x+dx][y+dy] == 1:
            return False
    return True
            
N = int(input())
mapp = [list(str(input().rstrip())) for _ in range(N)]

# Set position and rotation of B & E + Set mapp to list of int
b_positions = []
e_positions = []
for i in range(N):
    for j in range(N):
        if mapp[i][j] == 'B':
            b_positions.append([i,j])
            mapp[i][j] = 0
        elif mapp[i][j] == 'E':
            e_positions.append([i,j])
            mapp[i][j] = 0
        elif mapp[i][j] == '0':
            mapp[i][j] = 0
        else:
            mapp[i][j] = 1

b_position = [
    sum(b_positions[i][0] for i in range(3)) // 3,
    sum(b_positions[i][1] for i in range(3)) // 3
]
b_rotation = ROW if b_positions[0][0] == b_positions[1][0] else COLUMN

e_position = [
    sum(e_positions[i][0] for i in range(3)) // 3,
    sum(e_positions[i][1] for i in range(3)) // 3
]
e_rotation = ROW if e_positions[0][0] == e_positions[1][0] else COLUMN

mapp[b_position[0]][b_position[1]] = B_ROW if b_rotation == ROW else B_COLUMN
mapp[e_position[0]][e_position[1]] = E_ROW if e_rotation == ROW else E_COLUMN

visited_at = [[[float('inf')]*N for _ in range(N)], [[float('inf')]*N for _ in range(N)]]
visited_at[b_rotation][b_position[0]][b_position[1]] = 0

# Solution
pq = PriorityQueue()
pq.put([1, b_position, b_rotation])
while not pq.empty():
    cur_count, cur_position, cur_rotation = pq.get()
    if cur_position == e_position and cur_rotation == e_rotation:
        break

    for k in range(4):
        nx, ny = cur_position[0] + dx[k], cur_position[1] + dy[k]
        if not check_range(cur_position[0], cur_position[1], k, cur_rotation): continue
        if visited_at[cur_rotation][nx][ny] <= cur_count: continue

        mapp[nx][ny] = mapp[cur_position[0]][cur_position[1]]
        mapp[cur_position[0]][cur_position[1]] = 0
        visited_at[cur_rotation][nx][ny] = cur_count
        pq.put([cur_count + 1, [nx,ny], cur_rotation])
        mapp[cur_position[0]][cur_position[1]] = mapp[nx][ny]
        mapp[nx][ny] = 0

    if check_rotation_range(cur_position[0], cur_position[1]):
        if visited_at[(cur_rotation + 1) % 2][cur_position[0]][cur_position[1]] > cur_count:
            mapp[cur_position[0]][cur_position[1]] *= -1
            visited_at[(cur_rotation + 1) % 2][cur_position[0]][cur_position[1]] = cur_count
            pq.put([cur_count + 1, cur_position, (cur_rotation + 1) % 2])
            mapp[cur_position[0]][cur_position[1]] *= -1

to_print = visited_at[e_rotation][e_position[0]][e_position[1]]
print(to_print if to_print != float('inf') else 0)