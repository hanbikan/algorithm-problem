import sys
import math
import itertools
input = sys.stdin.readline


def getDistance(p1, p2):
    return math.sqrt(((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2))


def find(x):
    if parent[x] == x:
        return x

    px = find(parent[x])
    parent[x] = px
    return px


def union(x, y):
    px, py = find(x), find(y)

    if px > py:
        parent[px] = py
    else:
        parent[py] = px


if __name__ == '__main__':
    # 입력
    N = int(input())
    stars = [list(map(float, input().split())) for _ in range(N)]

    # For union-find
    parent = [i for i in range(N)]

    # For kruskal
    sets = []
    for i1, i2 in itertools.combinations(parent, 2):
        sets.append([i1, i2, getDistance(stars[i1], stars[i2])])

    # 거리에 대해 오름차순 정렬
    sets.sort(key=lambda x: x[2])

    # Kruskal
    minCost = 0
    for i1, i2, d in sets:
        if find(i1) != find(i2):
            union(i1, i2)
            minCost += d

    # 출력
    print("{:.2f}".format(minCost))
