from bisect import bisect_left
import sys
input = sys.stdin.readline

needs = int(input())
m, n = map(int,input().split())
p1 = [int(input()) for _ in range(m)]
extended_p1 = p1 + p1[:-1]
p2 = [int(input()) for _ in range(n)]
extended_p2 = p2 + p2[:-1]

# Setup prefix sums
prefix_sum1 = []
tmp = 0
for p in extended_p1:
    tmp += p
    prefix_sum1.append(tmp)
prefix_sum2 = []
tmp = 0
for p in extended_p2:
    tmp += p
    prefix_sum2.append(tmp)

# Setup sorted possible sums for pizzas
s1 = []
for s in range(len(p1)):
    for e in range(s + 1, s + len(p1)):
        to_append = prefix_sum1[e - 1]
        if s - 1 >= 0:
            to_append -= prefix_sum1[s - 1]
        s1.append(to_append)
s1.append(prefix_sum1[len(p1) - 1])
s1.append(0)
s1.sort()

s2 = []
for s in range(len(p2)):
    for e in range(s + 1, s + len(p2)):
        to_append = prefix_sum2[e - 1]
        if s - 1 >= 0:
            to_append -= prefix_sum2[s - 1]
        s2.append(to_append)
s2.append(prefix_sum2[len(p2) - 1])
s2.append(0)
s2.sort()

# Solution
result = 0
for item1 in s1:
    to_find = needs - item1
    i1 = bisect_left(s2, to_find)
    if i1 <= len(s2) - 1 and item1 + s2[i1] == needs:
        i2 = bisect_left(s2, to_find + 1)
        result += i2 - i1

print(result)