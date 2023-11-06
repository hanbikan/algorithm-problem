from bisect import bisect_left, bisect_right
import sys
import random
input = sys.stdin.readline

# N = random.randrange(2, 4)

a = [1,2,2,4,5]
print(bisect_left(a, 3))