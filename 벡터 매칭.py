import sys
import itertools
input = sys.stdin.readline


def getPointsSum(points):
    xSum, ySum = 0, 0

    for x, y in points:
        xSum += x
        ySum += y

    return xSum, ySum


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N = int(input())
        points = [list(map(int, input().split())) for _ in range(N)]

        minLengthSum = float('inf')

        # 모든 포인트의 x, y의 전체 합을 구함
        xSum, ySum = getPointsSum(points)

        # p1, p2로 v1을 구한다고 하자. 이 때 벡터는 p1 - p2 또는 p2 - p1이다.
        # 즉, 하나는 더하고, 하나는 빼야한다. 크게 보면 모든 점에서 절반은 더하고 절반은 빼게 된다.
        # 최종적으로 이 벡터들을 모두 더한 뒤 길이를 구하기 때문에, N개 중에 N//2를 선택하여,
        # 한쪽은 좌표의 값을 더해주고, 나머지 절반은 좌표의 값을 빼준 뒤 길이를 구하면 된다.
        cases = list(itertools.combinations(points, N//2))
        casesLength = len(cases)

        for i in range(casesLength//2):
            positiveXSum, positiveYSum = 0, 0

            # 선택된 모든 좌표들을 더함
            for x, y in cases[i]:
                positiveXSum += x
                positiveYSum += y

            # (NegativeSum) = (전체 합) - (PositiveSum)
            negativeXSum = xSum - positiveXSum
            negativeYSum = ySum - positiveYSum

            minLengthSum = min(minLengthSum, ((
                positiveXSum - negativeXSum)**2 + (positiveYSum - negativeYSum)**2)**(0.5))

        print("{:.12f}".format(minLengthSum))
