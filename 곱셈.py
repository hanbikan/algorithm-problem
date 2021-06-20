import sys
input = sys.stdin.readline


def getRemainderRecursively(curB):
    if curB == 1:
        return a % c

    halfRemainder = getRemainderRecursively(curB//2)
    toReturn = halfRemainder*halfRemainder
    if curB % 2 != 0:
        toReturn *= a

    return toReturn % c


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(getRemainderRecursively(b))
