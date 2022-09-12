import sys
input = sys.stdin.readline

def check():
    for i in range(len(nums)):
        if i+1 != nums[i]:
            return 0

    return 1

N, K = map(int,input().split())
nums = list(map(int,input().split()))

nums.sort()

i = 1
while i < len(nums):
    if nums[i-1] == nums[i]:
        nums.append(nums[i] + K)
        nums.pop(i)
        nums.sort()
    else:
        i += 1
        
print(check())