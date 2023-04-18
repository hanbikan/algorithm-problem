import sys
input = sys.stdin.readline

N, B, W = map(int, input().split())
line = str(input().rstrip())

b, w = 0, 0

res = 0
s, e = 0, 0
while e < N:
    if b > B:
        if line[s] == 'W': w -= 1
        else: b -= 1
        s += 1
    else:
        if line[e] == 'W': w += 1
        else: b += 1
        e += 1

    if b <= B and w >= W:
        res = max(res, w + b)

print(res)