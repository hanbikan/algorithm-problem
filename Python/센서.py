import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
censors = list(map(int, input().split()))
censors.sort()

if N < K:
    print(0)
else:
    distancesBetweenCensors = []
    for i in range(N-1):
        distancesBetweenCensors.append(censors[i+1]-censors[i])
    distancesBetweenCensors.sort()

    for _ in range(K-1):
        distancesBetweenCensors.pop()
    print(sum(distancesBetweenCensors))
