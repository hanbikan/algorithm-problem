import sys
input = sys.stdin.readline


def getMinCost(meats):
    # 무게에 대해서도 정렬해주는 것은, 같은 가격의 고기들을 살 때 고중량 고기를 먼저 사겠다는 것임
    meats.sort(reverse=True, key=lambda x: x[0])
    meats.sort(key=lambda x: x[1])

    weightCount = 0
    sameCostCount = 0
    costList = []

    for i in range(N):
        w, c = meats[i]

        weightCount += w
        # 1. 같은 가격인 고기들을 여러 개 살 경우
        if i >= 1 and c == meats[i-1][1]:
            sameCostCount += c
        # 2. 일반적인 경우, 이전 고기보다 현재 고기가 비쌀 경우
        else:
            sameCostCount = c

        if weightCount >= M:
            costList.append(sameCostCount)

            # 2의 경우인데 목표 중량을 달성했을 경우에는 더이상 반복문을 돌릴 필요가 없음
            if sameCostCount == c:
                break

    if costList:
        return min(costList)
    else:
        return -1


if(__name__ == "__main__"):
    # 입력
    N, M = map(int, input().split())

    meats = []
    for _ in range(N):
        meats.append(list(map(int, input().split())))

    # 처리
    minCost = getMinCost(meats)
    print(minCost)
