import sys
input = sys.stdin.readline


def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def getMinSpanningTreeWeight():
    minSpanningTreeWeight = 0

    for a, b, c in vertices:
        if find(a) != find(b):
            union(a, b)
            minSpanningTreeWeight += c

    return minSpanningTreeWeight


if __name__ == '__main__':
    V, E = map(int, input().split())

    parents = [i for i in range(V+1)]

    vertices = [list(map(int, input().split())) for _ in range(E)]
    vertices.sort(key=lambda x: x[2])

    print(getMinSpanningTreeWeight())
