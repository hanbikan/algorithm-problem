import sys
input = sys.stdin.readline


def getMinLength():
    start, end = 0, 0
    curSum = 0
    minLength = 100001

    while start < N:
        if curSum >= S:
            minLength = min(minLength, end-start)
            curSum -= nums[start]
            start += 1
        elif end >= N:
            break
        else:
            curSum += nums[end]
            end += 1

    return minLength if minLength != 100001 else 0


if __name__ == '__main__':
    N, S = map(int, input().split())
    nums = list(map(int, input().split()))

    minLength = getMinLength()

    print(minLength)
