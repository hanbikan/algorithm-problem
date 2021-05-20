import sys
input = sys.stdin.readline


def dfs(building, depth):
    global buildingsOnDepth

    if buildingsOnDepth.get(depth):
        if building in buildingsOnDepth[depth]:
            return

        buildingsOnDepth[depth].add(building)
    else:
        buildingsOnDepth[depth] = set([building])

    # 탈출
    if building == targetBuilding:
        return

    for next in nextBuildings[building]:
        dfs(next, depth+1)


def searchBuilding(building):
    global costsToBuild

    # 탈출
    if building == targetBuilding:
        return

    for next in nextBuildings[building]:
        costsToBuild[next] = max(
            costsToBuild[next], costsToBuild[building] + costs[next])


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())

    costs = [0]
    costs += list(map(int, input().split()))

    nextBuildings = {i: [] for i in range(N+1)}
    requiredBuildings = {i: [] for i in range(N+1)}

    for _ in range(K):
        cur, next = map(int, input().split())
        nextBuildings[cur].append(next)
        requiredBuildings[next].append(cur)

    # 헤더 빌딩(0번)에, 처음부터 지을 수 있는 건물들 연결
    for b in range(1, N+1):
        if requiredBuildings[b] == []:
            nextBuildings[0].append(b)
            requiredBuildings[b].append(0)

    targetBuilding = int(input())

    # 깊이 별로 빌딩들을 나눔
    buildingsOnDepth = {}
    dfs(0, 0)

    # 깊이에 따른 탐색
    costsToBuild = [0 for _ in range(N+1)]
    for buildings in buildingsOnDepth.values():
        for b in buildings:
            searchBuilding(b)

    print(costsToBuild[targetBuilding])
