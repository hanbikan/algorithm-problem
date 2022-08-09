import sys
input = sys.stdin.readline
nums = list(map(int, input().strip()))
nums.sort(reverse=True)
for num in nums:
    print(num, end="")
