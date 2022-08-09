import sys
input = sys.stdin.readline


def setVerticesColor(start):
    global verticesColor

    todo = [start]
    verticesColor[start] = 1

    while todo:
        curVertex = todo.pop(0)

        for next in graph[curVertex]:
            if verticesColor[next] == 0:
                verticesColor[next] = verticesColor[curVertex]*-1
                todo.append(next)
            elif verticesColor[curVertex] == verticesColor[next]:
                return False

    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = {i: [] for i in range(1, V+1)}

    for _ in range(E):
        e1, e2 = map(int, input().split())
        graph[e1].append(e2)
        graph[e2].append(e1)

    # -1: Red, 0: Undefined, 1: Blue
    verticesColor = [0 for _ in range(V+1)]
    isBipartiteGraph = True
    for v in graph.keys():
        if verticesColor[v] == 0:
            if setVerticesColor(v) == False:
                isBipartiteGraph = False
                break

    if isBipartiteGraph:
        print("YES")
    else:
        print("NO")
