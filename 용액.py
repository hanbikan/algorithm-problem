import sys
input = sys.stdin.readline


def getMinAbsIndices():
    left, right = 0, N-1
    minAbsSum = 2000000001
    minAbsIndices = [-1, -1]

    while left < right:
        curSum = nums[left] + nums[right]
        curAbsSum = abs(curSum)

        if minAbsSum > curAbsSum:
            minAbsSum = curAbsSum
            minAbsIndices = [left, right]

        if curSum > 0:
            right -= 1
        else:
            left += 1

    return minAbsIndices


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))

    nums.sort()

    i1, i2 = getMinAbsIndices()
    print(nums[i1], nums[i2])
