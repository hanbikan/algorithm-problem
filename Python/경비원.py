import sys
input = sys.stdin.readline
NORTH, EAST, SOUTH, WEST = 1, 2, 3, 4
DIR, OFFSET = 0, 1

def get_position(dir, offset):
    if dir == NORTH:
        x, y = 0, offset
    elif dir == EAST:
        x, y = offset, W
    elif dir == SOUTH:
        x, y = H, offset
    else:
        x, y = offset, 0
    
    return x, y

if __name__ == '__main__':
    W, H = map(int, input().split())
    N = int(input())

    info = []
    for i in range(N):
        dir, offset = map(int, input().split())
        if dir == 2:
            dir = SOUTH
        elif dir == 3:
            dir = WEST
        elif dir == 4:
            dir = EAST

        info.append([dir, offset])

    me_dir, me_offset = map(int, input().split())
    if me_dir == 2:
        me_dir = SOUTH
    elif me_dir == 3:
        me_dir = WEST
    elif me_dir == 4:
        me_dir = EAST

    # Solution
    res = 0
    me_x, me_y = get_position(me_dir, me_offset)
    for i in range(N):
        diff = abs((me_dir - info[i][DIR]))
        if diff == 0:
            res += abs(me_offset - info[i][OFFSET])
        elif diff == 1 or diff == 3:
            cur_x, cur_y = get_position(*info[i])
            res += abs(me_x - cur_x) + abs(me_y - cur_y)
        else:
            if me_dir == NORTH or me_dir == SOUTH:
                res += H + min(
                        me_offset + info[i][OFFSET],
                        (W - me_offset) + (W - info[i][OFFSET])
                    )
            else:
                res += W + min(
                        me_offset + info[i][OFFSET],
                        (H - me_offset) + (H - info[i][OFFSET])
                    )
    print(res)