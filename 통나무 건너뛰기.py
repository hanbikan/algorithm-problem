import sys
input = sys.stdin.readline


def getMaxDifferenceBetweenAdjacent(nums):
    nums.sort()

    maxDifference = max(abs(nums[0]-nums[1]), abs(nums[-1]-nums[-2]))
    for i in range(N-2):
        maxDifference = max(maxDifference, abs(nums[i]-nums[i+2]))

    return maxDifference


T = int(input())
for _ in range(T):
    N = int(input())
    heights = list(map(int, input().split()))

    maxDifference = getMaxDifferenceBetweenAdjacent(heights)
    print(maxDifference)
