import sys
input = sys.stdin.readline


def getFactorial(num):
    factorial = 1
    for i in range(2, num+1):
        factorial *= i

    return factorial


if __name__ == '__main__':
    n, m = map(int, input().split())

    result = getFactorial(n)//(getFactorial(m)*getFactorial(n-m))
    print(result)
