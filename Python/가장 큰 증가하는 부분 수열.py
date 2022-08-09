import sys
input = sys.stdin.readline


def getMinGreaterEqualIndex(left, right, value):
    while left <= right:
        mid = (left+right)//2

        if stack[mid] >= value:
            right = mid-1
        else:
            left = mid+1

    return left


N = int(input())
nums = list(map(int, input().split()))

stack = [nums[0]]

for i in range(1, N):
    if nums[i] > stack[-1]:
        stack.append(nums[i])
    else:
        maxLowerIndex = getMinGreaterEqualIndex(0, len(stack)-1, nums[i])
        stack[maxLowerIndex] = nums[i]

print(len(stack))
