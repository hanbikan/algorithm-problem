import sys
input = sys.stdin.readline

G = int(input())
l, r = 1, 100000

res = []
while l < r:
    diff = pow(r, 2) - pow(l, 2)
    if diff > G: r -= 1
    elif diff < G:
        l += 1
        r += 1
    else:
        res.append(r)
        l += 1
        r += 1

if len(res) == 0: res.append(-1)
for i in range(len(res)):
    print(res[i])