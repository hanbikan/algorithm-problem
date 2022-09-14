from collections import deque
import sys
input = sys.stdin.readline

def test_gears(g1, g2):
    for i in range(max(len(g1), len(g2))):
        if i < len(g1) and i < len(g2):
            if int(g1[i]) + int(g2[i]) >= 4:
                return False
    
    return True

gear1 = deque()
for c in str(input().rstrip()):
    gear1.append(int(c))
len1 = len(gear1)
gear2 = deque()
for c in str(input().rstrip()):
    gear2.append(int(c))
len2 = len(gear2)

# 0000002112112112
# 2212112
res = float('inf')
extended_gear1 = deque([0]*(len2 - 1) + list(gear1))
current_gear2 = gear2
for s in range(len1 + len2):
    if test_gears(extended_gear1, current_gear2):
        start = min(s, len2 - 1)
        end = max(len1 + len2 - 1, s + len2)
        res = min(res, end - start)
    current_gear2.appendleft(0)

print(res)