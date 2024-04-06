import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B, C = map(int,input().split())

# N개의 시험장에 N명의 총감독관 배치
result = N
for i in range(N):
    A[i] = max(0, A[i] - B)

# 부감독관 배치
for i in range(N):
    result += A[i] // C
    if A[i] % C != 0:
        result += 1

print(result)