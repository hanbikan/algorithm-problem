from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

lst = []
while True:
    line = str(input().rstrip())
    if (line == "E"): break
    lst.append(line)

lst.sort()
for item in lst: print(item)