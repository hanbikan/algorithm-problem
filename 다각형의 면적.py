import sys
input = sys.stdin.readline


def getPolygonArea():
    polygonArea = 0
    x0, y0 = x[0], y[0]

    for i in range(1, N-1):
        polygonArea += (
            (x[i] - x0) * (y[i+1] - y0) - (x[i+1] - x0) * (y[i] - y0)
        ) / 2

    return abs(polygonArea)


if __name__ == '__main__':
    N = int(input())

    x, y = [], []
    for _ in range(N):
        curX, curY = list(map(int, input().split()))
        x.append(curX)
        y.append(curY)

    polygonArea = getPolygonArea()
    print(round(polygonArea, 1))
