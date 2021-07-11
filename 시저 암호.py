import sys
input = sys.stdin.readline


def getPi(target):
    targetLength = len(target)
    pi = [0]*targetLength
    j = 0

    for i in range(1, targetLength):
        while j > 0 and target[i] != target[j]:
            j = pi[j-1]

        if target[i] == target[j]:
            j += 1
            pi[i] = j

    return pi


def getLeftShiftedChar():
    aLength = len(A)
    leftShiftedChar = {}

    for i in range(aLength):
        leftShiftedChar[A[i]] = A[i-1]

    return leftShiftedChar


def printShifts():
    shifts = []
    aLength = len(A)
    curS = S

    # shifts 추가
    if isStringCount1(curS, W):
        shifts.append(0)

    for i in range(1, aLength):
        curS = shiftLeft(curS)

        if isStringCount1(curS, W):
            shifts.append(i)

    # 출력
    shiftsLength = len(shifts)

    if shiftsLength == 0:
        print("no solution")
    elif shiftsLength == 1:
        print("unique:", shifts[0])
    else:
        print("ambiguous:", end="")
        for n in shifts:
            print("", n, end="")
        print()


def isStringCount1(string, target):
    stringCount = 0
    stringLength = len(string)
    targetLength = len(target)

    i, j = 0, 0

    while i < stringLength:
        if string[i] == target[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = pi[j-1]

        if j == targetLength:
            stringCount += 1
            if stringCount >= 2:
                return False

            j = pi[j-1]

    return stringCount == 1


def shiftLeft(s):
    shifted = s
    length = len(s)

    for i in range(length):
        shifted[i] = leftShiftedChar[shifted[i]]

    return shifted


if __name__ == '__main__':
    N = int(input())

    for _ in range(N):
        A, W, S = list(input().rstrip()), list(
            input().rstrip()), list(input().rstrip())

        pi = getPi(W)
        leftShiftedChar = getLeftShiftedChar()

        printShifts()
