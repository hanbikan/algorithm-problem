import sys
input = sys.stdin.readline


def gcd(x, y):
    if y != 0:
        return gcd(y, x % y)
    else:
        return x


def lcm(x, y):
    return (x*y)//gcd(x, y)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        print(lcm(a, b))
