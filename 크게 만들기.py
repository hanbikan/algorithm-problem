import sys
input = sys.stdin.readline


# p 이전 숫자들 중에 -1이 아닌 것이 있다면 해당 인덱스를 받아옴
def getPreviousNumberIndex(p, numberList):
    p -= 1
    while p >= 0:
        if numberList[p] == -1:
            p -= 1
        else:
            return p

    return -1


def getRemovedMaxNumberList(numberList):
    kCount = 0
    p, n = 0, 1

    # 앞에서부터 숫자 비교하면서 삭제(= -1로 바꿈)
    while n <= N-1:
        if kCount >= K:
            return numberList

        if numberList[p] < numberList[n]:
            kCount += 1
            numberList[p] = -1

            previousNumberIndex = getPreviousNumberIndex(p, numberList)
            if previousNumberIndex != -1:
                p = previousNumberIndex
                continue

        p = n
        n += 1

    # 남은 것들이 있다면, 뒤에서 모두 처리(-1)
    for i in range(N-1, -1, -1):
        if kCount >= K:
            break

        if numberList[i] != -1:
            numberList[i] = -1
            kCount += 1

    return numberList


def solution(s):
    numberList = [int(c) for c in s]

    removedMaxNumberList = getRemovedMaxNumberList(numberList)
    for n in removedMaxNumberList:
        if n != -1:
            print(n, end="")


N, K = map(int, input().split())
s = str(input().rstrip())
solution(s)
