import sys

input = sys.stdin.readline
MOD = 1000000007
SIZE = 8


def multiply_matrix(matrix1, matrix2):
    return [[sum(matrix1[i][k]*matrix2[k][j] % MOD for k in range(SIZE)) % MOD
             for j in range(SIZE)] for i in range(SIZE)]


def solution(D):
    # dp 초기화
    dp1 = [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0]
    ]

    dp2 = [[0]*SIZE for _ in range(SIZE)]
    for i in range(SIZE):
        dp2[i][i] = 1

    # 분할 정복
    while D > 0:
        if D % 2 != 0:
            dp2 = multiply_matrix(dp2, dp1)
            D -= 1
        dp1 = multiply_matrix(dp1, dp1)
        D //= 2

    return dp2[0][0]


if __name__ == '__main__':
    D = int(input())
    print(solution(D))
