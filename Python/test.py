from bisect import bisect_left, bisect_right
import sys
import random
input = sys.stdin.readline

# N = random.randrange(2, 4)

a = [1, 4, 6]
print(bisect_right(a, 10) - 1)