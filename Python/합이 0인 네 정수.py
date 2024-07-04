import sys, bisect, math
input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab_sums = []
for a in A:
    for b in B:
        ab_sums.append(a + b)
ab_sums.sort()

cd_sums = []
for c in C:
    for d in D:
        cd_sums.append(c + d)
cd_sums.sort()

result = 0
u, d = 0, len(cd_sums) - 1
log_length = int(math.log(len(ab_sums)))
while u < len(ab_sums) and 0 <= d:
    summ = ab_sums[u] + cd_sums[d]
    if summ > 0:
        if d - log_length >= 0 and ab_sums[u] + cd_sums[d - log_length] > 0:
            d = bisect.bisect_left(cd_sums, -ab_sums[u] + 1) - 1
        else:
            d -= 1
    elif summ < 0:
        if u + log_length < len(ab_sums) and ab_sums[u + log_length] + cd_sums[d] < 0:
            u = bisect.bisect_left(ab_sums, -cd_sums[d])
        else:
            u += 1
    else:
        if u + log_length < len(ab_sums) and ab_sums[u + log_length] == ab_sums[u]:
            nu = bisect.bisect_left(ab_sums, ab_sums[u] + 1)
        else:
            nu = u + 1
            while nu < len(ab_sums) and ab_sums[nu] == ab_sums[u]:
                nu += 1

        if d - log_length >= 0 and cd_sums[d - log_length] == cd_sums[d]:
            nd = bisect.bisect_left(cd_sums, cd_sums[d]) - 1
        else:
            nd = d - 1
            while nd >= 0 and cd_sums[nd] == cd_sums[d]:
                nd -= 1

        result += (nu - u) * (d - nd)
        u = nu
        d = nd

print(result)