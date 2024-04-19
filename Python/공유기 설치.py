import sys

input = sys.stdin.readline

N, C = map(int, input().split())
x = [int(input()) for _ in range(N)]

x.sort()
l, r = 0, x[-1] - x[0]
while l <= r:
    m = (l + r) // 2

    put_count = 1
    last_put = x[0]
    for i in range(1, N):
        if x[i] - last_put >= m:
            last_put = x[i]
            put_count += 1

    if put_count >= C:
        l = m + 1
    else:
        r = m - 1

print(l - 1)