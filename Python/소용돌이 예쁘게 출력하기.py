import sys
input = sys.stdin.readline

RIGHT, TOP, LEFT, BOTTOM = 0, 1, 2, 3
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def to_absolute_position(x, y):
    return x + SIDE, y + SIDE

def f(index, x, y, dir, to_reach):
    global mapp
    cur_x, cur_y = x, y

    while True:
        ax, ay = to_absolute_position(cur_x, cur_y)
        mapp[ax][ay] = index
        index += 1
        cur_x, cur_y = cur_x + dx[dir], cur_y + dy[dir]
        if not (abs(cur_x) <= SIDE and abs(cur_y) <= SIDE): return
        if dir == RIGHT or dir == LEFT:
            if abs(cur_y) == to_reach: break
        else:
            if abs(cur_x) == to_reach: break
    
    if dir == BOTTOM:
        to_reach += 1
    f(index, cur_x, cur_y, (dir + 1) % 4, to_reach)



r1, c1, r2, c2 = map(int,input().split())
SIDE = max(abs(r1), abs(c1), abs(r2), abs(c2))
LENGTH = SIDE * 2 + 1

mapp = [[0]*LENGTH for _ in range(LENGTH)]
f(1, 0, 0, RIGHT, 1)

ar1, ac1 = to_absolute_position(r1, c1)
ar2, ac2 = to_absolute_position(r2, c2)
for i in range(ar1, ar2 + 1):
    print(*mapp[i][ac1:ac2+1])