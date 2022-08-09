import sys
input = sys.stdin.readline

nums = [int(c) for c in str(input().rstrip())]

if (0 in nums) and (sum(nums) % 3 == 0):
    for n in sorted(nums, reverse=True):
        print(n, end="")
else:
    print(-1)
