from collections import defaultdict, deque
import sys
input = sys.stdin.readline
 
i = 0.00
while i < 10:
    print(i, int(i*100), int(i*100 + 0.5))
    i += 0.01