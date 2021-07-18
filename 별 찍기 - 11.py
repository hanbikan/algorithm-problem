import sys
input = sys.stdin.readline


def printStar(N):
    curStar = [
        "  *   ",
        " * *  ",
        "***** "]
    curLen = 3

    while curLen < N:
        for i in range(curLen):
            curStar.append(curStar[i]*2)
            curStar[i] = " "*curLen + curStar[i] + " "*curLen

        curLen *= 2

    for s in curStar:
        print("".join(s))


if __name__ == '__main__':
    N = int(input())
    printStar(N)
