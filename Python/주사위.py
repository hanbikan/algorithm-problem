import sys
input = sys.stdin.readline

d2 = [[0,1], [0,2], [0,3], [0,4], [1,2], [1,3], [2,4], [3,4], [1,5], [2,5], [3,5], [4,5]]
d3 = [[0,1,2], [0,1,3], [0,2,4], [0,3,4], [5,1,2], [5,1,3], [5,2,4], [5,3,4]]

N = int(input())
nums = list(map(int,input().split()))

if (N == 1):
    print(sum(nums) - max(nums))
else:
    min_d1 = min(nums)
    min_d2 = float('inf')
    for i, j in d2:
        min_d2 = min(min_d2, nums[i] + nums[j])
    min_d3 = float('inf')
    for i, j, k in d3:
        min_d3 = min(min_d3, nums[i] + nums[j] + nums[k])

    print(
        (min_d3 * 4 + min_d2 * (4 * (N - 2)) + min_d1 * pow(N - 2, 2))
        + (min_d2 * 4 + min_d1 * (4 * (N - 2))) * (N - 1)
    )