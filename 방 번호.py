import sys
input = sys.stdin.readline


def getNumbersWithMaxDigit():
    global money

    numbersWithMaxDigit = []

    # 0 제외한 숫자들 중에 가장 싼 것으로 첫자리 결정
    minCost, minIndex = getMinCostAndIndex(costs[1:10])
    if money - minCost < 0:
        return []

    money -= minCost
    numbersWithMaxDigit.append(minIndex+1)

    # 가장 싼 것으로 남은 자리들 결정
    minCost, minIndex = getMinCostAndIndex(costs)
    while money-minCost >= 0:
        money -= minCost
        numbersWithMaxDigit.append(minIndex)

    return numbersWithMaxDigit


def getMinCostAndIndex(costs):
    minCost = costs[0]
    minIndex = 0

    for i in range(1, len(costs)):
        if minCost > costs[i]:
            minCost = costs[i]
            minIndex = i

    return minCost, minIndex


# curNums를 앞자리부터, 최대한 큰 숫자로 교체
def getPossibleMaxNumber(nums):
    global money

    for i in range(maxDigit):
        possibleMaxDigit = getPossibleMaxDigit(nums, i)

        if possibleMaxDigit != -1:
            money += costs[nums[i]] - costs[possibleMaxDigit]
            nums[i] = possibleMaxDigit

    return nums


# nums[index]에서 변경할 수 있는 가장 큰 숫자를 반환함
def getPossibleMaxDigit(nums, index):
    target = nums[index]

    for i in range(N-1, target, -1):
        if money + costs[target] - costs[i] >= 0:
            return i

    return -1


N = int(input())
costs = list(map(int, input().split()))
money = int(input())

if N == 1:
    print(0)
else:
    # 자릿수 지정
    numbersWithMaxDigit = getNumbersWithMaxDigit()
    maxDigit = len(numbersWithMaxDigit)

    # 주어진 돈으로 0이상의 값이 나오지 않음
    if maxDigit == 0:
        print(0)
    else:
        # 연산
        numbersWithMaxDigit = getPossibleMaxNumber(numbersWithMaxDigit)

        # 출력
        for n in numbersWithMaxDigit:
            print(n, end="")
