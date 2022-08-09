N = int(input())
k = int(input())

left, right = 1, k

while left <= right:
    mid = (left+right)//2

    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid//i, N)

    if cnt >= k:
        RET = mid
        right = mid-1
    else:
        left = mid+1
print(RET)
