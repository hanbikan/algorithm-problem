import sys
input = sys.stdin.readline


def setDistances(node):
    global distances

    for n, d in tree[node]:
        if distances[n] == -1:
            distances[n] = distances[node] + d

            setDistances(n)


if __name__ == '__main__':
    V = int(input())

    # 입력 기반으로 tree 구성
    tree = [[] for i in range(V+1)]

    for _ in range(V):
        curNums = list(map(int, input().split()))
        curNumsLen = len(curNums)

        for i in range(1, curNumsLen-1, 2):
            tree[curNums[0]].append((curNums[i], curNums[i+1]))

    # 단말 노드 아무거나 지정
    for i in range(1, V+1):
        if len(tree[i]) == 1:
            terminalNode = i
            break

    # 단말 노드를 기준으로 탐색하여, 거리가 가장 먼 노드의 정보를 얻음
    distances = [-1]*(V+1)
    distances[terminalNode] = 0
    setDistances(terminalNode)
    maxDistanceNode = distances.index(max(distances))

    # 가장 먼 거리에 해당하는 노드에서 탐색하여 최대 길이를 구함
    distances = [-1]*(V+1)
    distances[maxDistanceNode] = 0
    setDistances(maxDistanceNode)
    maxDistance = max(distances)

    print(maxDistance)
