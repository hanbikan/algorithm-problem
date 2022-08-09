import sys
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    px, py = find(x), find(y)

    if px < py:
        parent[py] = px
    else:
        parent[px] = py


if __name__ == '__main__':
    N, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(M)]
    info.sort(key=lambda x: x[2])

    parent = [i for i in range(N+1)]

    total_cost = 0
    last_cost = 0
    for a, b, c in info:
        if find(a) != find(b):
            union(a, b)
            total_cost += c
            last_cost = c

    print(total_cost - last_cost)
