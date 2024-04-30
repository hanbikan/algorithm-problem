import sys, itertools
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
difficulty = list(map(int, input().split()))
difficulty.sort()

result = 0
for i in range(N):
    for j in range(i + 1, N):
        if difficulty[j] - difficulty[i] < X:
            continue

        lr_sum = difficulty[i] + difficulty[j]
        for k in range(j - i):
            cb = itertools.combinations(difficulty[i + 1:j], k)
            for comb in cb:
                cur_sum = lr_sum + sum(comb)
                if L <= cur_sum <= R:
                    result += 1
print(result)