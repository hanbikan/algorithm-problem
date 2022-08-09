import sys
input = sys.stdin.readline
INF = 2999999998


def getMinAbsFluids():
    minAbsSum = INF
    minAbsFluids = [0, 0, 0]

    for i in range(N-2):
        left, right = i + 1, N - 1

        while left < right:
            curSum = fluids[i] + fluids[left] + fluids[right]
            curAbsSum = abs(curSum)

            # minAbs 갱신
            if curAbsSum < minAbsSum:
                minAbsSum = curAbsSum
                minAbsFluids = [fluids[i], fluids[left], fluids[right]]

            # 0에 수렴하게끔 인덱스 조정
            if curSum > 0:
                right -= 1
            elif curSum < 0:
                left += 1
            else:
                return minAbsFluids

    return minAbsFluids


if __name__ == '__main__':
    N = int(input())
    fluids = list(map(int, input().split()))

    fluids.sort()

    minAbsFluids = getMinAbsFluids()
    print(*minAbsFluids)
