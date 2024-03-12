import sys
input = sys.stdin.readline

S, C = map(int,input().split())
sizes = [int(input()) for _ in range(S)]

l, r = 1, max(sizes)
while l <= r:
    m = (l + r) // 2
    possible = 0
    for size in sizes:
        possible += size // m
    if possible >= C:
        l = m + 1
    else:
        r = m - 1

by = (l + r) // 2
result = 0
possible = 0
for size in sizes:
    result += size % by
    possible += size // by
result += (possible - C) * by

print(result)