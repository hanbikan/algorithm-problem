import sys
input = sys.stdin.readline


def gcd(n, m):
    if m != 0:
        return gcd(m, n % m)
    else:
        return n


def lcm(n, m, gcd):
    return n*m//gcd


if __name__ == '__main__':
    N, M = map(int, input().split())

    res = gcd(N, M)
    print(res)
    print(lcm(N, M, res))
