import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def get_diff_position():
    for i in range(N):
        for j in range(M):
            if(matrix1[i][j] != matrix2[i][j]): return i, j
    
    return -1, -1

def inject_vaccine(x, y):
    global matrix1
    matrix1[x][y] = origin2

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if not (0 <= nx <= N-1 and 0 <= ny <= M-1): continue
        if matrix1[nx][ny] != origin1: continue

        inject_vaccine(nx, ny)

def is_two_matrices_same():
    for i in range(N):
        for j in range(M):
            if(matrix1[i][j] != matrix2[i][j]): return False
    
    return True

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix1 = [list(map(int, input().split())) for _ in range(N)]
    matrix2 = [list(map(int, input().split())) for _ in range(N)]

    # Find an element which has changed
    startX, startY = get_diff_position()
    if(startX == -1): # There is no diff elems
        print("YES")
    else:
        origin1 = matrix1[startX][startY]
        origin2 = matrix2[startX][startY]
        inject_vaccine(startX, startY)

        if(is_two_matrices_same()):
            print("YES")
        else:
            print("NO")

