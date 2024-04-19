import sys

input = sys.stdin.readline

N, M, V = map(int, input().split())
C = list(map(int, input().split()))

start_index = V - 1
circle_length = N - V + 1

for _ in range(M):
    K = int(input())
    if K < start_index:
        print(C[K])
    else:
        offset = K - start_index
        index = start_index + (offset % circle_length)
        print(C[index])