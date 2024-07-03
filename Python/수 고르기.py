import sys, bisect
input = sys.stdin.readline

def solution(N, M, nums):
    if N == 1 or M == 0:
        return 0

    nums.sort()
    result = float('inf')

    for num in nums:
        target = num + M
        index = bisect.bisect_left(nums, target)
        if 0 <= index < N and nums[index] - num >= M:
            result = min(result, nums[index] - num)

    return result

N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]

print(solution(N, M, nums))