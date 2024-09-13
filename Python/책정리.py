import sys, bisect
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
# LIS
stack = [nums[0]]
for i in range(1,N):
    index = bisect.bisect_left(stack, nums[i])
    if index < len(stack):
        stack[index] = nums[i]
    else:
        stack.append(nums[i])
print(N - len(stack))