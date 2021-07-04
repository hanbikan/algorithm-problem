import sys
input = sys.stdin.readline


def getMinCost(index, isVisited):
    # Base Case
    # 모든 곳을 방문했을 경우
    if isVisited == MAX_BINARY:
        if W[index][START_INDEX] != 0:
            return W[index][START_INDEX]
        else:
            return INF

    # 이미 같은 방법으로 방문한 적이 있을 경우
    if dp[index][isVisited] != 0:
        return dp[index][isVisited]

    # Recursive Case
    # 아직 방문하지 않은, 방문 가능한 도시들을 돌면서 minCost 갱신
    minCost = INF
    for i in range(N):
        if getBitFromBinary(isVisited, i) == 0 and W[index][i] != 0:
            minCost = min(
                minCost, W[index][i] + getMinCost(i, setBinaryTrue(isVisited, i)))

    dp[index][isVisited] = minCost

    return minCost


def setBinaryTrue(binary, index):
    return binary | 1 << index


def getBitFromBinary(binary, index):
    return (binary >> index) % 2


if __name__ == '__main__':
    N = int(input())
    W = [list(map(int, input().split())) for _ in range(N)]

    START_INDEX = 0
    MAX_BINARY = (1 << N) - 1
    INF = 1000001*16

    dp = [[0]*(MAX_BINARY + 1) for _ in range(N)]

    minCost = getMinCost(START_INDEX, 1)
    print(minCost)
