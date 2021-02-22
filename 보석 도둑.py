import math
def getGreaterEqualIndex(sortedNums, num):
    left, right = 0, len(sortedNums)-1
    while left<right+1:
        mid = (left+right)//2
        if num<sortedNums[mid]:
            right = mid-1
        elif num>sortedNums[mid]:
            left = mid+1
        else: return mid
    return right+1

N, K = map(int, input().split())
M, V = 0, 1
Jewelries = []
for _ in range(N):
    Jewelries.append(list(map(int, input().split())))
Jewelries = sorted(Jewelries, key=lambda x:x[V], reverse=True)
C = []
for _ in range(K): C.append(int(input()))
C.sort() # 2 10

RET=0
for Jewelry in Jewelries:
    idxMinBag = getGreaterEqualIndex(C, Jewelry[M])
    if idxMinBag < len(C):
        del C[idxMinBag]
        RET+=1
print(RET)