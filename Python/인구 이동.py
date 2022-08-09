from collections import defaultdict
from copy import deepcopy
import sys
input = sys.stdin.readline

dx = [1, 0]
dy = [0, 1]

def f():
    global parents

    # Set parents by checking differences for adjacent nodes
    parents = [i for i in range(N*N)]
    for i in range(N):
        for j in range(N):
            merge_parent(i, j)

    # Calculate sums, counts of each groups
    sums = defaultdict(int)
    counts = defaultdict(int)
    for i in range(N):
        for j in range(N):
            p = find(
                convert_position_to_index(i, j)
            )
            sums[p] += population[i][j]
            counts[p] += 1

    # Exception: There is no elements to be merged
    if len(sums) == N*N:
        return False

    # Modify population by parents
    for i in range(N):
        for j in range(N):
            p = find(
                convert_position_to_index(i, j)
            )
            population[i][j] = sums[p] // counts[p]

    return True

def merge_parent(x, y):
    for k in range(2):
        nx, ny = x + dx[k], y + dy[k]
        if not (nx <= N-1 and ny <= N-1): continue

        diff = abs(population[x][y] - population[nx][ny])

        if L <= diff <= R:
            union(
                convert_position_to_index(x, y),
                convert_position_to_index(nx, ny)
            )

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    px, py = find(x), find(y)
    if px < py:
        parents[py] = px
    else:
        parents[px] = py

def convert_position_to_index(x, y):
    return x * N + y

def convert_index_to_position(index):
    return (index // N, index % N)

if __name__ == '__main__':
    N, L, R = map(int, input().split())
    population = [list(map(int,input().split())) for _ in range(N)]

    res = 0
    while(True):
        is_moved = f()
        if is_moved:
            res += 1
        else:
            break

    print(res)