import sys, itertools
input = sys.stdin.readline

K, N = map(int, input().split())
rankss = [list(map(int, input().split())) for _ in range(K)]

count = 0
for cb in itertools.combinations([i for i in range(1, N + 1)], 2):
    a, b = cb
    flag = True
    target = rankss[0].index(a) < rankss[0].index(b)
    for k in range(1, K):
        ranks = rankss[k]
        if (ranks.index(a) < ranks.index(b)) != target:
            flag = False
            break

    if flag:
        count += 1

print(count)