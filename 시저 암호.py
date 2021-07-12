import sys
input = sys.stdin.readline


def getPi(keyword):
    keywordLength = len(keyword)
    pi = [0]*keywordLength
    j = 0

    for i in range(1, keywordLength):
        while j > 0 and keyword[i] != keyword[j]:
            j = pi[j-1]

        if keyword[i] == keyword[j]:
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
    if isThereOneKeyword(curS, W):
        shifts.append(0)

    for i in range(1, aLength):
        curS = shiftLeft(curS)

        if isThereOneKeyword(curS, W):
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


def isThereOneKeyword(string, keyword):
    keywordCount = 0
    stringLength = len(string)
    keywordLength = len(keyword)

    i, j = 0, 0

    while i < stringLength:
        if string[i] == keyword[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = pi[j-1]

        if j == keywordLength:
            keywordCount += 1
            if keywordCount >= 2:
                return False

            j = pi[j-1]

    return keywordCount == 1


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
