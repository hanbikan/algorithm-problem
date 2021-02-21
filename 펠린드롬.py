import sys
read = sys.stdin.readline

def IsPalindrome(nums):
    for i in range(len(nums)//2):
        if nums[i]!=nums[len(nums)-1-i]: return False
    return True

N=int(input())
nums = list(map(int,read().strip().split()))
DP=[[False for i in range(j, len(nums))] for j in range(len(nums))]
M=int(input())
for i in range(M):
    q = list(map(int,read().strip().split()))
    if DP[q[0]-1][q[1]-1-(q[0]-1)]:
        print(1)

    elif IsPalindrome(nums[q[0]-1:q[1]]):
        print(1)
        for j in range((q[1]-q[0])//2+1):
            DP[q[0]-1+j][q[1]-1-2*j-(q[0]-1)] = True
    else: print(0)