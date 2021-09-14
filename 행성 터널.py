import sys
input = sys.stdin.readline


def get_info():
    info = []

    for k in range(3):
        positions.sort(key=lambda x: x[k])

        for i in range(1, N):
            info.append([positions[i], positions[i-1],
                         abs(positions[i][k] - positions[i-1][k])])

    info.sort(key=lambda x: x[2])

    return info


def find_parent(x):
    if parents[x] == x:
        return x

    parents[x] = find_parent(parents[x])
    return parents[x]


def union(x, y):
    px, py = find_parent(x), find_parent(y)

    if sum(px) < sum(py):
        parents[py] = px
    else:
        parents[px] = py


def get_total_cost():
    info = get_info()
    total_cost = 0
    linked = 0

    for pos1, pos2, cost in info:
        if find_parent(tuple(pos1)) != find_parent(tuple(pos2)):
            union(tuple(pos1), tuple(pos2))
            total_cost += cost

            linked += 1
            if linked >= N-1:
                break

    return total_cost


if __name__ == '__main__':
    # Input
    N = int(input())
    positions = [list(map(int, input().split())) for _ in range(N)]

    # For union-find
    parents = {tuple(pos): tuple(pos) for pos in positions}

    # Solution
    total_cost = get_total_cost()
    print(total_cost)
