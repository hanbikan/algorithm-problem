from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

stack = []
for num in nums:
    index = bisect_left(stack, num)

    if index == len(stack):
        stack.append(num)
    else:
        stack[index] = num

print(len(stack))