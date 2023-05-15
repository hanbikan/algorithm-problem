from math import ceil
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
counts = [int(input()) for _ in range(M)]

result = float('inf')
l, r = 1, max(counts)
while l <= r:
    mid = (l + r) // 2
    summ = 0
    for count in counts:
        summ += ceil(count / mid)
    
    if summ <= N:
        result = mid
        r = mid - 1
    else:
        l = mid + 1
print(result)