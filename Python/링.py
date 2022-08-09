import sys
input = sys.stdin.readline


def gcd(x, y):
    if y != 0:
        return gcd(y, x % y)
    else:
        return x


if __name__ == '__main__':
    N = int(input())
    rings = list(map(int, input().split()))

    for i in range(1, N):
        g = gcd(rings[0], rings[i])
        print("{0}/{1}".format(rings[0]//g, rings[i]//g))
