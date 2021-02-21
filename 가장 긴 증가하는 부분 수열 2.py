N = int(input())
nums = list(map(int, input().split()))
dp = [0]

for i in range(N):
    left = 0
    right = len(dp)-1

    while left<=right:
        mid=(right+left)//2
        if dp[mid]<nums[i]:
            left = mid + 1
        else:
            right = mid - 1
    
    if left >= len(dp):
        dp.append(nums[i])
        print(1)
    else:
        dp[left] = nums[i]
        print(2)
print(dp)