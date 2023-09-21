import sys
input = sys.stdin.readline

def rotate_clockwise_by_45():
    directions = [
        [-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]
    ]
    for i in range(1, n // 2 + 1):
        x, y = get_position(directions[-1], i)
        tmp = matrix[x][y]
        for j in range(len(directions) - 1, 0, -1):
            x, y = get_position(directions[j], i)
            px, py = get_position(directions[j - 1], i)
            matrix[x][y] = matrix[px][py]
        x, y = get_position(directions[0], i)
        matrix[x][y] = tmp

def get_position(direction, distance):
    return n // 2 + direction[0] * distance, n // 2 + direction[1] * distance

def print_matrix():
    for i in range(n):
        print(*matrix[i])

T = int(input())
for _ in range(T):
    n, d = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    rotate_count = (d + 360) // 45
    for _ in range(rotate_count):
        rotate_clockwise_by_45()
    print_matrix()