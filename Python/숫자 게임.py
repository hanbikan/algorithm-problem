import sys
input = sys.stdin.readline


def getMinMaxSum():
    # a, b를 변형시키고 다시 원상복구하기 위함
    originalA = [a[i] for i in range(101)]
    originalB = [b[i] for i in range(101)]

    ai, bi = getNotZeroIndex(a, 1, False), getNotZeroIndex(b, 100, True)
    minVar = min(a[ai], b[bi])
    a[ai] -= minVar
    b[bi] -= minVar

    minMaxSum = 0
    while ai != -1 and bi != -1:
        minMaxSum = max(minMaxSum, ai + bi)

        ai, bi = getNotZeroIndex(
            a, ai, False), getNotZeroIndex(b, bi, True)
        minVar = min(a[ai], b[bi])
        a[ai] -= minVar
        b[bi] -= minVar

    # a, b 원상복구
    for i in range(1, 101):
        a[i] = originalA[i]
        b[i] = originalB[i]

    return minMaxSum


# 0이 아닌 다음 인덱스 반환
def getNotZeroIndex(nums, startIndex, isReversed):
    if isReversed == False:
        for i in range(startIndex, 101):
            if nums[i] >= 1:
                return i
    else:
        for i in range(startIndex, 0, -1):
            if nums[i] >= 1:
                return i

    return -1


if __name__ == '__main__':
    N = int(input())

    a = [0]*101
    b = [0]*101

    for _ in range(N):
        ai, bi = map(int, input().split())
        a[ai] += 1
        b[bi] += 1

        minMaxSum = getMinMaxSum()
        print(minMaxSum)
