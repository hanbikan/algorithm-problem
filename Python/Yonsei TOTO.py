import sys
input = sys.stdin.readline


def getMinMileage(p, l, nums):
    minMileageIndex = p - l
    if minMileageIndex < 0:
        return 1
    else:
        nums.sort()
        return nums[minMileageIndex]


def getMaxClassCount(m, mileages):
    maxClassCount = 0
    mileages.sort()

    for mileage in mileages:
        m -= mileage
        if m < 0:
            break

        maxClassCount += 1

    return maxClassCount


if __name__ == '__main__':
    n, m = map(int, input().split())
    mileages = []

    # input / set mileages
    for i in range(n):
        p, l = map(int, input().split())
        nums = list(map(int, input().split()))

        mileages.append(getMinMileage(p, l, nums))

    # spend mileages / output
    maxClassCount = getMaxClassCount(m, mileages)
    print(maxClassCount)
