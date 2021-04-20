import sys
input = sys.stdin.readline

N = int(input())
nums = [0]*10001
for _ in range(N):
    nums[int(input())] += 1

for i in range(10001):
    for j in range(nums[i]):
        sys.stdout.write(str(i)+"\n")
