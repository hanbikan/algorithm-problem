from bisect import bisect_left
import sys
input = sys.stdin.readline

D, N = map(int,input().split())
oven_diameters = list(map(int,input().split()))
pizza_diameters = list(map(int,input().split()))

# Modify oven_diameters
# 5 6 4 3 6 2 3
# 5 5 4 3 3 2 2
# 2 2 3 3 4 5 5(for binary search)
minn = oven_diameters[0]
for i in range(1, D):
    if oven_diameters[i] > minn:
        oven_diameters[i] = minn
    else:
        minn = min(minn, oven_diameters[i])
oven_diameters = oven_diameters[::-1]

# Binary search
result = 0
l = 0
for d in pizza_diameters:
    index = bisect_left(oven_diameters, d, lo = l)
    if index >= D:
        result = 0
        break
    result = D - index
    l = index + 1

print(result)