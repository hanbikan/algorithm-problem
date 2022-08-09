import sys
input = sys.stdin.readline


def getFarthestNodeAndPrefixWeight(start, n):
    todo = [(start, 0)]
    isVisited = [False]*(n+1)

    farthestNode = start
    maxWeight = 0

    while todo:
        node, weight = todo.pop(0)
        isVisited[node] = True

        if maxWeight < weight:
            maxWeight = weight
            farthestNode = node

        for n, w in nodes[node]:
            if isVisited[n] == False:
                todo.append((n, weight + w))

    return (farthestNode, maxWeight)


if __name__ == '__main__':
    n = int(input())

    nodes = {i: [] for i in range(1, n+1)}

    for _ in range(n-1):
        a, b, c = map(int, input().split())
        nodes[a].append((b, c))
        nodes[b].append((a, c))

    farthestNodeFromRoot, _ = getFarthestNodeAndPrefixWeight(1, n)
    _, diameter = getFarthestNodeAndPrefixWeight(farthestNodeFromRoot, n)
    print(diameter)
