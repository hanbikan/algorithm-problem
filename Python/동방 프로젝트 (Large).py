import sys
input = sys.stdin.readline

'''
1 2, 2 4 -> 1 4
1 2, 3 4 -> 1 2, 3 4
1 5, 2 10 -> 1 10

sort
1 2
1 3
1 4
-> only 1 4
1 4, 2 6, 3 8, 9 10: pairs[i][1] >= pairs[i+1][0]인 경우 -> (pairs[i][0], pairs[i+1][1])
-> 1 8, 9 10

+ 1 10, 2 5 -> 1 10
'''
N = int(input())
M = int(input())
pairs = [list(map(int,input().split())) for _ in range(M)]
pairs.sort()

next_pairs = []
for i in range(M-1): # 1 2, 1 3 -> 1 3
    if pairs[i][0] != pairs[i+1][0]:
        next_pairs.append(pairs[i])
if (len(pairs) >= 1 and len(next_pairs) >= 1 and pairs[-1][0] != next_pairs[-1][0]) or (len(pairs) >= 1 and len(next_pairs) == 0):
    next_pairs.append(pairs[-1])

pairs = next_pairs
M = len(pairs)

next_pairs = []
# 1 10, 2 5, 3 6, 4 11 -> 1 10, 4 11
i = 0
while i < M:
    next_pairs.append(pairs[i])
    j = i + 1
    while j < M:
        if pairs[j][1] > pairs[i][1]:
            break
        j += 1
    i = j
pairs = next_pairs
M = len(pairs)

parents = [i for i in range(N + 1)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    px, py = find(x), find(y)
    if px < py:
        parents[py] = px
    else:
        parents[px] = py

for i in range(M - 1):
    s, e = pairs[i]
    ns, ne = pairs[i+1]
    for j in range(s+1, e+1 if e > ne else min(e, ns)+1):
        union(s, j)
if len(pairs) >= 1:
    s, e = pairs[-1]
    for j in range(s+1, e+1):
        union(s, j)

sett = set()
for i in range(1, N+1):
    sett.add(parents[i])
print(len(sett))

'''
5
2
1 2
2 3

5
2
1 2
3 4

5
2
1 4
2 3

12
4
1 10
2 5
3 6
4 11
'''