import sys
input = sys.stdin.readline


def getParents(tree, N):
    parents = [-1 for _ in range(N+1)]
    todo = [1]

    while todo:
        cur = todo.pop(0)

        for node in tree[cur]:
            if parents[node] == -1:
                todo.append(node)
                parents[node] = cur

    return parents


if __name__ == '__main__':
    N = int(input())

    tree = {i: [] for i in range(1, N+1)}
    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    parents = getParents(tree, N)
    for i in range(2, N+1):
        print(parents[i])
