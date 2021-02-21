N = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)
acc = 1
for i in range(N):
    if acc < nums[i]: break
    acc += nums[i]
print(acc)