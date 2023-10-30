import sys
input = sys.stdin.readline
STUDENT = 'S'
TEACHER = 'T'
OBJECT = 'O'
EMPTY = 'X'

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def is_valid_matrix():
    for sx, sy in student_indexes:
        for k in range(4):
            x, y = sx + dx[k], sy + dy[k]
            while (0 <= x <= N - 1) and (0 <= y <= N - 1):
                if matrix[x][y] == TEACHER:
                    return False
                elif matrix[x][y] == OBJECT:
                    break
                x += dx[k]
                y += dy[k]
    return True

def f(index, remain_objs):
    if remain_objs == 0:
        return is_valid_matrix()
    
    for i in range(index, N * N - remain_objs + 1):
        x, y = i // N, i % N
        if matrix[x][y] == EMPTY:
            matrix[x][y] = OBJECT
            if f(x * N + y, remain_objs - 1):
                return True
            matrix[x][y] = EMPTY
    
    return False

N = int(input())
matrix = [list(map(str, input().rstrip().split())) for _ in range(N)]

student_indexes = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == STUDENT:
            student_indexes.append([i, j])

if f(0, 3):
    print("YES")
else:
    print("NO")