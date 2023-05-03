import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

result = 0 if K >= 2 else sum(nums)
sums = [0] * (K - 1) + [sum(nums)]
divs = [-1] * (K - 1)
while True:
    min_sum = sums[0]
    min_index = 0
    for i in range(1, K):
        if sums[i] <= min_sum:
            min_sum = sums[i]
            min_index = i
    
    if min_index == K - 1: break

    divs[min_index] += 1
    to_give = nums[divs[min_index]]
    sums[min_index] += to_give
    sums[min_index + 1] -= to_give
    
    result = max(result, min(sums))

print(result)

'''
8 3
12 7 19 20 17 14 9 10

0 / 0 / 12 7 19 20 17 14 9 10 -> 0 0 108 | -1 -1
0 / 12 / 7 19 20 17 14 9 10 -> 0 12 96 | -1 0
12 / 0 / 7 19 20 17 14 9 10 -> 12 0 96 | 0 0
12 / 7 / 19 20 17 14 9 10 -> 12 7 79 | 0 1
12 / 7 19 / 20 17 14 9 10 -> 12 26 60 | 0 2
12 7 / 19 / 20 17 14 9 10 -> 19 19 60 | 1 2
12 7 / 19 20 / 17 14 9 10 -> 19 39 50 | 1 3
12 7 19 / 20 / 17 14 9 10 -> 38 20 50 | 2 3
12 7 19 / 20 17 / 14 9 10 -> 38 37 33 | 2 4
terminated because the last one is the smallest
'''