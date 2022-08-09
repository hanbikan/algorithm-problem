import sys
input = sys.stdin.readline

P = [0, 1, 1, 1, 2]

T = int(input())
for _ in range(T):
    N = int(input())

    for i in range(len(P), N+1):
        P.append(P[i-1] + P[i-5])

    print(P[N])
