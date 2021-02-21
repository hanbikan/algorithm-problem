import sys
read = sys.stdin.readline
#N=int(input())
#nums = list(map(int, read().strip().split()))
N=6
nums=[10,20,10,30,20,50]

arr = []
arr.append(nums[0])

reverse = []
reverse.append(0)

for i in range(1, N):
    h = nums[i]

    if arr[-1] < h:
        arr.append(h)
        reverse.append(len(arr)-1)
    else:
        l = 0
        r = len(arr)
        m = 0
        while l < r:
            m = (l+r)//2
            if arr[m] < h:
                l = m+1
            else:
                r = m
        
        arr[r] = h
        reverse.append(r)
    print(arr, reverse)

print(len(arr))

answer = ''
count = len(arr)-1
for i in reversed(range(len(reverse))):
    if reverse[i] == count:
        answer = '{} '.format(nums[i]) + answer
        count -= 1

print(answer)
