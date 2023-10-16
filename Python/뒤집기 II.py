import sys
input = sys.stdin.readline

def is_in_range(x, y):
    return 0 <= x <= N - 1 and 0 <= y <= M - 1

def switch(x, y):
    for i in range(x + 1):
        for j in range(y + 1):
            matrix[i][j] = (matrix[i][j] + 1) % 2

N, M = map(int,input().split())
matrix = []
for _ in range(N):
    to_append = []
    line = str(input().rstrip())
    for c in line:
        if c == '0':
            to_append.append(0)
        else:
            to_append.append(1)
    matrix.append(to_append)

start_positions = []
for i in range(N - 1, -1, -1):
    start_positions.append([i, M - 1])
for j in range(M - 2, -1, -1):
    start_positions.append([0, j])

count = 0
for start_i, start_j in start_positions:
    i, j = start_i, start_j
    while is_in_range(i, j):
        if matrix[i][j] == 1:
            switch(i, j)
            count += 1
        i += 1
        j -= 1
    start_i -= 1

print(count)