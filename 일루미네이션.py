import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

dx = [-1, 0, 1, 1, 0, -1]
dy = [-1, -2, -1, 1, 2, 1]

def f(x,y):
    global is_visited
    res = 0

    for k in range(6):
        nx, ny = x + dx[k], y + dy[k]

        if not (0 <= nx <= H-1 and 0 <= ny <= 2*W-1): continue
        if info[nx][ny] == 0:
            if not is_visited[nx][ny]:
                is_visited[nx][ny] = True
                res += f(nx, ny)
        elif info[nx][ny] == 1:
            res += 1
    
    return res

if __name__ == '__main__':
    W, H = map(int, input().split())

    info = [[-1]*(2*W) for _ in range(H)]
    for i in range(H):
        line = list(map(int, input().split()))

        for j in range(W):
            if i%2==0: new_j = j*2+1
            else: new_j = j*2

            info[i][new_j] = line[j]
    
    # Traversal
    to_visit = []
    for i in range(H):
        for j in range(2):
            if info[i][j] == 0:
                to_visit.append([i,j])
        if W > 1:
            for j in range(2*W-2, 2*W):
                if info[i][j] == 0:
                    to_visit.append([i,j])

    for j in range(2*W):
        if info[0][j] == 0:
            to_visit.append([0,j])
        if H > 1:
            if info[H-1][j] == 0:
                to_visit.append([H-1,j])

    res = 0
    is_visited = [[False]*(2*W) for _ in range(H)]
    for x, y in to_visit:
        if is_visited[x][y]: continue

        is_visited[x][y] = True
        res += f(x, y)


    # Add res for building outside
    for i in range(H):
        if info[i][0] == 1:
            res += 3
        if info[i][1] == 1:
            res += 1

        if W > 1:
            if info[i][2*W-1] == 1:
                res += 3
            if info[i][2*W-2] == 1:
                res += 1

    for j in range(2*W):
        if info[0][j] == 1:
            if j == 2*W-1:
                res += 1
            else:
                res += 2
        if H > 1:
            if info[H-1][j] == 1:
                if (H%2 == 0 and j == 0) or (H%2 == 1 and j == 2*W-1):
                    res += 1
                else:
                    res += 2

    print(res)