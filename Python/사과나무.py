from bisect import bisect_left
import sys
input = sys.stdin.readline

def solution():
    for i in range(N):
        heights[i] = heights[i] % 3
        if heights[i] == 0:
            continue
        to_reduce_for_next = (not (heights[i] - 1)) + 1

        index = bisect_left(heights, to_reduce_for_next, lo = i + 1)
        if index >= N: return False
        heights[index] -= to_reduce_for_next
    
    return True

N = int(input())
heights = list(map(int,input().split()))
heights.sort()

if solution():
    print("YES")
else:
    print("NO")