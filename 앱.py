N, M = map(int, input().split())
app = []
for m, c in zip(input().split(), input().split()):
    app.append((int(c), int(m)))
app.sort()
dp1, dp2 = {0: 0}, {0: 0}
res = 10**6

for c, m in app:
    for key in dp1:
        new = key + c
        if new > res:
            continue
        if new in dp2:
            dp2[new] = max(dp1[key]+m, dp2[new])
        else:
            dp2[new] = dp1[key] + m
        if dp2[new] >= M:
            res = min(res, new)
    print(dp2)
    dp1 = dp2.copy()

print(res)
