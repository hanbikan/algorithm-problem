S=int(input())
l, r = 1, S
while l<=r:
    m=(l+r)//2
    curSum = m*(m+1)//2
    if curSum<=S:
        RET=m
        l=m+1
    else:
        r=m-1
print(RET)