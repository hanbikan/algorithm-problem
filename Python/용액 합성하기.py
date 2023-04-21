from fileinput import close
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))

l, r = 0, N - 1
closest = 200000000

while (l < r):
    cur = nums[l] + nums[r]
    if (abs(cur) < abs(closest)):
        closest = cur
    
    if cur > 0:
        r -= 1
    else:
        l += 1

print(closest)