import sys
input = sys.stdin.readline


def getLanCountAfterCut(lans, cutBy):
    lanCountAfterCut = 0
    for lan in lans:
        lanCountAfterCut += lan//cutBy
    return lanCountAfterCut


K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

left, right = 1, max(lans)
while left <= right:
    mid = (left+right)//2
    lanCountAfterCut = getLanCountAfterCut(lans, mid)

    if N <= lanCountAfterCut:
        left = mid+1
    else:
        right = mid-1
print(right)
