t = int(input())
for _ in range(t):
    n = int(input())
    nums = [input() for _ in range(n)]
    nums.sort()
    flag = True
    for i in range(n-1):
        if nums[i] == nums[i+1][:len(nums[i])]:
            flag = False
            break
    if flag: print('YES')
    else: print('NO')