import sys
import heapq
input = sys.stdin.readline

# 입력
N, K = map(int, input().split())

jewelries = sorted([list(map(int, input().split())) for _ in range(N)])
bags = sorted([int(input()) for _ in range(K)])

# 메인 로직
valueSum = 0  # 출력값
availableJewelries = []  # bag 이하인 보석들을 저장
jewelryIndex = 0

for bag in bags:
    while jewelryIndex <= N-1:
        if jewelries[jewelryIndex][0] > bag:
            break

        heapq.heappush(availableJewelries, (-1)*jewelries[jewelryIndex][1])
        jewelryIndex += 1

    if availableJewelries:
        valueSum += (-1)*heapq.heappop(availableJewelries)

print(valueSum)
