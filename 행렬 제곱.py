import sys
input = sys.stdin.readline


def getNSquaredMatrix(n):
    # Base Case
    if n == 1:
        return matrix

    # Recursive Case
    halfSquared = getNSquaredMatrix(n//2)
    if n % 2 == 0:
        return squareMatrix(halfSquared, halfSquared)
    else:
        return squareMatrix(squareMatrix(halfSquared, halfSquared), matrix)


def squareMatrix(matrixA, matrixB):
    return [[squareElement(i, j, matrixA, matrixB) for j in range(N)] for i in range(N)]


def squareElement(x, y, matrixA, matrixB):
    return sum(matrixA[x][i] * matrixB[i][y] for i in range(N)) % 1000


if __name__ == '__main__':
    # 입력
    N, B = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 처리
    nSquaredMatrix = getNSquaredMatrix(B) if B >= 2 else [
        [matrix[i][j] % 1000 for j in range(N)] for i in range(N)]

    # 출력
    for row in nSquaredMatrix:
        print(*row)
