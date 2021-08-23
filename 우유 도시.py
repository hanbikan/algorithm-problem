import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
STRAWBERRY, CHOCOLATE, BANANA = 0, 1, 2


def getMaxMilkCount(toEat, x, y):
    # Recursive case
    if x == N-1 and y == N-1:
        if milks[x][y] == toEat:
            return 1
        else:
            return 0

    # dp가 이미 있을 시
    if dp[toEat][x][y] != -1:
        return dp[toEat][x][y]

    next_milk = (toEat + 1) % 3

    # 양 방향 탐색
    if x + 1 <= N-1 and y + 1 <= N-1:
        dp[toEat][x][y] = max(
            max(getMaxMilkCount(next_milk, x+1, y),
                getMaxMilkCount(next_milk, x, y+1)) + 1,
            max(getMaxMilkCount(toEat, x+1, y), getMaxMilkCount(toEat, x, y+1))
        ) if milks[x][y] == toEat else max(getMaxMilkCount(toEat, x+1, y), getMaxMilkCount(toEat, x, y+1))

    # 남쪽 탐색
    elif x + 1 <= N-1:
        dp[toEat][x][y] = max(
            getMaxMilkCount(next_milk, x+1, y) + 1, getMaxMilkCount(toEat, x+1, y)) if milks[x][y] == toEat else getMaxMilkCount(toEat, x+1, y)

    # 동쪽 탐색
    elif y + 1 <= N-1:
        dp[toEat][x][y] = max(
            getMaxMilkCount(next_milk, x, y+1) + 1, getMaxMilkCount(toEat, x, y+1)) if milks[x][y] == toEat else getMaxMilkCount(toEat, x, y+1)

    return dp[toEat][x][y]


if __name__ == '__main__':
    N = int(input())
    milks = [list(map(int, input().split())) for _ in range(N)]

    dp = [[[-1]*N for _ in range(N)] for _ in range(3)]
    print(getMaxMilkCount(STRAWBERRY, 0, 0))
