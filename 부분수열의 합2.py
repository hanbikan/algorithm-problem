import sys
import itertools
input = sys.stdin.readline


def setValidSetCount():
    global validSetCount

    leftSums = []
    for i in range(N//2 + 1):
        for s in itertools.combinations(nums[:N//2], i):
            leftSums.append(sum(s))
    leftLength = len(leftSums)
    leftSums.sort()

    rightSums = []
    for i in range(N - N//2 + 1):
        for s in itertools.combinations(nums[N//2:], i):
            rightSums.append(sum(s))
    rightLength = len(rightSums)
    rightSums.sort(reverse=True)

    l, r = 0, 0
    while l < leftLength and r < rightLength:
        curLeft, curRight = leftSums[l], rightSums[r]
        curSum = leftSums[l] + rightSums[r]

        if curSum == S:
            ls, rs = l, r
            while ls < leftLength and leftSums[ls] == curLeft:
                ls += 1
            while rs < rightLength and rightSums[rs] == curRight:
                rs += 1

            validSetCount += (ls-l)*(rs-r)
            l, r = ls, rs
        elif curSum < S:
            l += 1
        elif curSum > S:
            r += 1


if __name__ == '__main__':
    N, S = map(int, input().split())
    nums = list(map(int, input().split()))

    validSetCount = 0
    setValidSetCount()

    print(validSetCount-1 if S == 0 else validSetCount)
