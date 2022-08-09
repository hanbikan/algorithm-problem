import sys
input = sys.stdin.readline


def setDp(start):
    todo = [start]
    dp[start] = (0, 0)

    while todo:
        cur = todo.pop(0)

        if cur == 1:
            break

        if cur % 3 == 0 and dp[cur//3][0] > dp[cur][0] + 1:
            dp[cur//3] = (dp[cur][0] + 1, cur)
            todo.append(cur//3)

        if cur % 2 == 0 and dp[cur//2][0] > dp[cur][0] + 1:
            dp[cur//2] = (dp[cur][0] + 1, cur)
            todo.append(cur//2)

        if dp[cur-1][0] > dp[cur][0] + 1:
            dp[cur-1] = (dp[cur][0] + 1, cur)
            todo.append(cur-1)


def printPath():
    path = []
    cur = 1

    while cur != 0:
        path.append(cur)
        cur = dp[cur][1]

    print(*reversed(path))


if __name__ == '__main__':
    N = int(input())
    dp = [(float('inf'), 0)]*(N+1)

    setDp(N)

    print(dp[1][0])
    printPath()
