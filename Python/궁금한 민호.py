import sys
input = sys.stdin.readline


def getSum():
    sum = 0
    isAdded = [[False]*N for _ in range(N)]

    for i in range(N):
        dp = djikstra(i)

        # 불가능한 경우
        if dp == False:
            return -1

        # dp를 돌면서 sum
        for j in range(N):
            dpLength = len(dp[j])

            if dpLength == 0:
                continue

            for k in range(dpLength - 1):
                fr, to = dp[j][k], dp[j][k+1]
                if isAdded[fr][to] == False:
                    sum += graph[fr][to]
                    isAdded[fr][to] = True

            fr, to = dp[j][-1], j
            if isAdded[fr][to] == False:
                sum += graph[fr][to]
                isAdded[fr][to] = True

    return sum//2


def djikstra(start):
    todo = [([start], 0)]
    dp = [[] for _ in range(N)]

    while todo:
        curPath, curDist = todo.pop(0)
        curNode = curPath[-1]

        for n in range(N):
            if n == curNode:
                continue

            nextDist = curDist + graph[curNode][n]
            if nextDist == graph[start][n]:
                todo.append((curPath + [n], nextDist))
                dp[n] = curPath

            # 불가능한 경우
            elif nextDist < graph[start][n]:
                return False

    return dp


if __name__ == '__main__':
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    print(getSum())
