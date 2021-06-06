import sys
input = sys.stdin.readline


def getSumsToPrint(inputs):
    sortedInputs = sorted(
        sorted(inputs, key=lambda x: x[0]), key=lambda x: x[1])
    prefixSums = [[0] for _ in range(N+1)]

    prevSize = 0
    prevColor = 0
    prevZeroIndex = 0

    sumsToPrint = {}

    for i in range(N):
        c, s = sortedInputs[i]
        prefixSums[0].append(prefixSums[0][-1] + s)
        prefixSums[c].append(prefixSums[c][-1] + s)

        if s == prevSize:
            if c != prevColor:
                sumsToPrint[c, s] = prefixSums[0][prevZeroIndex] - \
                    prefixSums[c][-1]
        else:
            sumsToPrint[c, s] = prefixSums[0][-1] - prefixSums[c][-1]
            prevZeroIndex = i+1

        prevSize = s
        prevColor = c

    return sumsToPrint


if(__name__ == '__main__'):
    N = int(input())

    # 입력
    inputs = []
    for _ in range(N):
        inputs.append(tuple(map(int, input().split())))

    # 처리
    sumsToPrint = getSumsToPrint(inputs)

    # 출력
    for input in inputs:
        print(sumsToPrint[input])
