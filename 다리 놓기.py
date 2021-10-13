import sys
import math
input = sys.stdin.readline


def get_combination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))


def solution(N, M):
    return get_combination(M, N)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(solution(N, M))
