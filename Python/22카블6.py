import sys
input = sys.stdin.readline

dirs = ['d','u','r','l']
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def f(x, y, strr, n, m, k):
    if mapp[x][y] == 'E' and (k - len(strr)) % 2 == 0:
        return [strr]
    if len(strr) >= k:
        return []

    res = []
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        nstr = strr + [dirs[dir]]
        if not (0 <= nx <= n-1 and 0 <= ny <= m-1): continue
        if is_visited[nx][ny]: continue

        is_visited[nx][ny] = True
        res += f(nx, ny, nstr, n, m, k)
        is_visited[nx][ny] = False
    return res

def solution(n, m, x, y, r, c, k):
    x -= 1
    y -= 1
    r -= 1
    c -= 1

    global is_visited, mapp
    
    mapp = [['.']*m for _ in range(n)]
    mapp[x][y] = 'S'
    mapp[r][c] = 'E'

    is_visited = [[False]*m for _ in range(n)]
    
    print(f(x, y, [], n, m, k))
    

print(solution(3,4,2,3,3,1,5))