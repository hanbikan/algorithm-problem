from bisect import bisect_left, bisect_right
import sys
import random
input = sys.stdin.readline

# N = random.randrange(2, 4)
a = [1,3,3,3,4,5]
print(bisect_left(a, 2))
print(bisect_right(a, 6 - 1))