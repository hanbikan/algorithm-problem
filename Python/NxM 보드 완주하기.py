import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def f(x, y, count, remainder):
    if remainder == 0:
        return count

    res = float('inf')
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if not (0 <= nx <= N-1 and 0 <= ny <= M-1): continue
        if mapp[nx][ny] == '*': continue
        if is_visited[nx][ny]: continue

        nx2, ny2 = get_next_position(nx, ny, k)
        diff = abs(x - nx2) + abs(y - ny2)

        set_is_visited_continuously(x, y, nx2, ny2, k, True)
        res = min(res, f(nx2, ny2, count + 1, remainder - diff))
        set_is_visited_continuously(x, y, nx2, ny2, k, False)
    
    return res

def get_next_position(x, y, dir):
    while True:
        nx, ny = x + dx[dir], y + dy[dir]
        if not (0 <= nx <= N-1 and 0 <= ny <= M-1): break
        if mapp[nx][ny] == '*': break
        if is_visited[nx][ny]: break

        x, y = nx, ny

    return x, y

def set_is_visited_continuously(x, y, x_dest, y_dest, dir, flag):
    global is_visited
    while not (x == x_dest and y == y_dest):
        is_visited[x][y] = flag
        x, y = x + dx[dir], y + dy[dir]

case = 1
while True:
    try:
        N, M = map(int,input().split())
        mapp = []
        empty_count = 0
        empty_positions = []
        for i in range(N):
            line = []
            strr = str(input().rstrip())
            for j in range(M):
                c = strr[j]
                line.append(c)
                if c == '.':
                    empty_count += 1
                    empty_positions.append([i,j])
            mapp.append(line)

        is_visited = [[False]*M for _ in range(N)]
        res = float('inf')
        for x, y in empty_positions:
            is_visited[x][y] = True
            res = min(res, f(x, y, 0, empty_count-1))
            is_visited[x][y] = False
        if res == float('inf'): res = -1
        print("Case " + str(case) + ": " + str(res))

        case += 1
    except:
        break